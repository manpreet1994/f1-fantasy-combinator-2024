import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from utils import read_json, write_json
from config import MODEL_PATH, DRIVER_DATA_PATH

def train(model_dict, model_type, driver_name, X, y):
    X_array, y_array = np.array(X), np.array(y)
    match model_type:
        case "svr":
            reg = SVR(kernel="rbf").fit(X_array, y_array)
        case "rf":
            reg = RandomForestRegressor(max_depth=3).fit(X_array, y_array)
        case "ridge":
            reg = Ridge(alpha=1.0).fit(X_array, y_array)
        case "lg":
            reg = LinearRegression().fit(X_array, y_array)
        case "xgb":
            reg = XGBRegressor().fit(X_array, y_array)
    model_dict[driver_name] = reg
    return model_dict

def predict(model_dict, driver_name, X):
    return round(model_dict[driver_name].predict(X)[0]) 

def form_x_y(data_json, feature_set, is_training):
    fp1_array, fp2_array, fp3_array, fp_weighted_mean = get_free_practice_info(data_json, is_training) 
    #transformations
    if is_training:
        fantasy_scores = [x['fantasy_score'] for x in data_json.values()]
        dnf_prob_array = get_previous_dnf_prob(data_json)
        avg_overtake_array = get_previous_avg_overtakes(data_json)
        dotd_prob = get_dotd_probability(data_json)
        previous_score_array = get_previous_fantasy_scores(data_json)
    else:
        fantasy_scores = 0
        dnf_prob_array = get_previous_dnf_prob(data_json)[-1]
        avg_overtake_array = get_previous_avg_overtakes(data_json)[-1]
        dotd_prob = get_dotd_probability(data_json)[-1]
        previous_score_array = get_previous_fantasy_scores(data_json)[-1]

    temp_df = pd.DataFrame({
        "fp1" : fp1_array,
        "fp2": fp2_array,
        "fp3": fp3_array,
        "avg_score" : previous_score_array,
        "avg_overtake": avg_overtake_array,
        "dnf_prob": dnf_prob_array,
        "dotd_prob":dotd_prob,
        "weighted_fp_mean": fp_weighted_mean,
        "y": fantasy_scores
    })
    
    temp_df = temp_df.dropna()
    
    return temp_df[feature_set], temp_df["y"]

def get_free_practice_info(data_json, is_training):
    fp1_array = []
    fp2_array = []
    fp3_array = []
    fp_mean_array = []
    raw_info = [(x['fp1'], x.get('fp2', np.nan), x.get('fp3', np.nan), x.get("sprint_quali", np.nan), x["dnf"]) for x in data_json.values()]
    for fp1, fp2, fp3, sprint_quali, is_dnf in raw_info:
        if not (is_dnf and is_training):
            mean_val = np.nanmean([int(x) for x in [fp1, fp2, fp3, sprint_quali] if not x is np.nan])
            if not sprint_quali is np.nan:
                fp3_array.append(int(np.nan_to_num(sprint_quali, nan= mean_val)))
                fp2_array.append(int(np.nan_to_num(fp1, nan= mean_val)))
                fp1_array.append(int(np.nan_to_num(fp1, nan= mean_val)))
            else:
                fp3_array.append(int(np.nan_to_num(fp3, nan= mean_val)))
                fp2_array.append(int(np.nan_to_num(fp2, nan= mean_val)))
                fp1_array.append(int(np.nan_to_num(fp1, nan= mean_val)))
            fp_mean_array.append(round(np.average([fp1_array[-1], fp2_array[-1], fp3_array[-1]], weights=[2,5,10]),3))
        else:
            fp3_array.append(None)
            fp2_array.append(None)
            fp1_array.append(None)
            fp_mean_array.append(0)

    return fp1_array, fp2_array, fp3_array, fp_mean_array

def calculate_avg_array_from_cumsum(input_cumsum):
    return input_cumsum/np.arange(1,len(input_cumsum)+1)

def get_previous_avg_overtakes(race_before_json):
    overtakes = [x['overtake'] for x in race_before_json.values()]
    overtake_cumsum = np.cumsum(overtakes)
    avg_overtake_points_array = calculate_avg_array_from_cumsum(overtake_cumsum) #overtake_cumsum/np.arange(1,len(overtake_cumsum)+1)
    return avg_overtake_points_array

def get_dotd_probability(race_before_json):
    dotd = [x['dotd'] for x in race_before_json.values()]
    dotd_cumsum = np.cumsum(dotd)
    avg_overtake_points_array = calculate_avg_array_from_cumsum(dotd_cumsum) #dotd_cumsum/np.arange(1,len(dotd_cumsum)+1)
    return avg_overtake_points_array

def get_previous_fantasy_scores(race_before_json):
    fantasy_scores = [x['fantasy_score'] for x in race_before_json.values()]
    fantasy_cumsum = np.cumsum(fantasy_scores)
    avg_fantasy_points_array = calculate_avg_array_from_cumsum(fantasy_cumsum) #fantasy_cumsum/np.arange(1,len(fantasy_cumsum)+1)
    return avg_fantasy_points_array

def get_previous_dnf_prob(race_before_json):
    is_dnf = [x['dnf'] for x in race_before_json.values()]
    dnf_cumsum = np.cumsum(is_dnf)
    dnf_prob_array = calculate_avg_array_from_cumsum(dnf_cumsum) #dnf_cumsum/np.arange(1,len(dnf_cumsum)+1)
    return dnf_prob_array

def train_fantasy_score_from_practice_model(model_dict, model_type, feature_set, driver_name, data_json, till_race_no):
    race_before_json = {}
    for i in range(1,till_race_no):
        race_before_json[f"race_{i}"] = data_json[f"race_{i}"]
    
    X, y = form_x_y(race_before_json, feature_set, is_training=True)

    model_dict = train(model_dict, model_type, driver_name, X, y)
    return model_dict

def predict_fantasy_score_from_practice_model(model_dict, feature_set, driver_name, race_no):
    driver_json = read_json(os.path.join(DRIVER_DATA_PATH, f"{driver_name}.json"))
    ##filter driver_json for specific race
    input_json = {}
    # race_before_json = {}
    input_json[f"race_{race_no}"] = driver_json[f"race_{race_no}"]
    
    # for i in range(1,race_no):
    #     race_before_json[f"race_{i}"] = driver_json[f"race_{i}"]
    
    X, _ = form_x_y(input_json, feature_set, is_training=False)
    # X = np.array(get_free_practice_info(input_json))
    return predict(model_dict, driver_name, np.array(X))

def prediction_for_first_race():
    heuristic_scores = [40, 30, 25, 20, 20] + list(range(15,0,-1))
    fp1_array = []
    fp2_array = []
    fp3_array = []
    driver_array = []
    for driver_file in os.listdir(DRIVER_DATA_PATH):
        if ".json" in driver_file:
            driver_name = driver_file.split(".")[0]
            driver_array.append(driver_name)
            driver_json = read_json(os.path.join(DRIVER_DATA_PATH, driver_file))
            race1_json = driver_json["race_1"]
            fp1_array.append(int(race1_json["fp1"]))
            fp2_array.append(int(race1_json["fp2"]))
            fp3_array.append(int(race1_json["fp3"]))
    race_1_df = pd.DataFrame({
        "driver" : driver_array,
        "fp1" : fp1_array,
        "fp2" : fp2_array,
        "fp3": fp3_array
    })
    race_1_df["weighted_fp_mean"] = race_1_df.apply(lambda x : round(np.average([x.fp1, x.fp2, x.fp3], weights=[2,5,10]),2), axis=1)
    race_1_prediction_dict = dict(zip(race_1_df.sort_values(by="weighted_fp_mean")["driver"].to_list(), heuristic_scores))
    return race_1_prediction_dict