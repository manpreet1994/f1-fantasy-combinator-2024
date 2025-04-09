import argparse
import os
import pandas as pd
from config import MODEL_PATH, DRIVER_DATA_PATH, TEAM_DATA_PATH, PREDICTION_PATH, FEATURE_SET
from model_training.find_optimal_team import form_driver_cost_score_dict, update_constructor_with_predicted_fantasy_score, find_top_k_teams, find_team_cost
from model_training.training import predict_fantasy_score_from_practice_model as predict_score, prediction_for_first_race
from utils import read_json, write_json, read_pickle

def make_race_predictions(race_no):
    race_no_array = []
    driver_array = []
    predicted_fantasy_points_array = []
    fantasy_cost_array = []
    dnf_array = []
    race_name_array = []
    cost_change_array = []

    for driver_file in os.listdir(DRIVER_DATA_PATH):
        driver_name = driver_file.split(".")[0]
        driver_json = read_json(os.path.join(DRIVER_DATA_PATH, driver_file))
        
        # if this is first race, dont train anything directly predict using free practice
        if race_no == 1:
            race_1_prediction_dict = prediction_for_first_race()
            predicted_fantasy_points_array.append(race_1_prediction_dict[driver_name])
        else:
            # predict for nth race
            model_dict = read_pickle(os.path.join(MODEL_PATH,"model_dict.pkl"))
            # model_dict = read_json(os.path.join(MODEL_PATH,"model_dict.json"))
            predicted_fantasy_points = predict_score(model_dict, FEATURE_SET, driver_name, race_no)
            predicted_fantasy_points_array.append(predicted_fantasy_points)
        
        race_no_array.append(race_no)
        race_name_array.append(driver_json[f"race_{race_no}"]["race_name"])
        driver_array.append(driver_name)
        fantasy_cost_array.append(driver_json[f"race_{race_no}"]["fantasy_cost"])
        dnf_array.append(driver_json[f"race_{race_no}"]["dnf"])
    
    prediction_df = pd.DataFrame({
    "race_no" : race_no_array,
    "race_name": race_name_array,
    "driver": driver_array,
    "dnf": dnf_array,
    "predicted_fantasy_points": predicted_fantasy_points_array,
    "fantasy_cost" : fantasy_cost_array,
    })
    prediction_df["team"] = prediction_df.driver.apply(lambda x: x.split("_")[0])
    return prediction_df

def find_optimal_team():
    parser = argparse.ArgumentParser()
    parser.add_argument("--race_no", type=int)
    args = parser.parse_args()
    race_no = args.race_no

    constructor_dict = read_json(os.path.join(TEAM_DATA_PATH, "constructor_info.json"))
    race_prediction_df = make_race_predictions(race_no)
    
    master_dict = {}
    master_dict["driver"] = form_driver_cost_score_dict(race_prediction_df)
    master_dict["team"] = update_constructor_with_predicted_fantasy_score(constructor_dict[f"race_{race_no}"], race_prediction_df)
    if race_no==1:
        previous_team = []
        previous_team_cost = 100
    else:
        previous_team = read_json(os.path.join(PREDICTION_PATH, f"race_{race_no-1}_predictions.json"))
        previous_team_cost = find_team_cost(previous_team["prediction"], master_dict)

    predicted_best_team_df = find_top_k_teams(master_dict, previous_team_cost, 1, previous_team)
    
    predicted_best_team = predicted_best_team_df["team"].values[0]
    driver_2x = predicted_best_team_df["2x_driver"].values[0]

    output_json = {"prediction": predicted_best_team, "2x_driver":driver_2x, "race_name": race_prediction_df["race_name"].values[0]}
    write_json(os.path.join(PREDICTION_PATH, f"race_{race_no}_predictions.json"), output_json)

    return predicted_best_team, driver_2x

def update_optimal_team_actual_fantasy_score():
    pass

if __name__== "__main__":
    print(find_optimal_team())