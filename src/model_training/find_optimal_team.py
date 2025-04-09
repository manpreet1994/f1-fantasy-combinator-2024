import pandas as pd
from itertools import combinations, product
from config import DOMINANT_DRIVERS

def update_constructor_with_predicted_fantasy_score(input_dict, input_df):
    team_sum = input_df.groupby("team", as_index=False).sum()[["team","predicted_fantasy_points"]]
    for team_name, team_predicted_score in zip(team_sum.team, team_sum.predicted_fantasy_points):
        input_dict[team_name]["predicted_score"] = team_predicted_score
    return input_dict

def form_driver_cost_score_dict(race_df):
    output_dict = {}
    for driver, cost, predicted_score in zip(race_df.driver, race_df.fantasy_cost, race_df.predicted_fantasy_points):
        output_dict[driver] = {"cost": cost, "predicted_score":predicted_score}
    return output_dict

def find_team_score_based_on_predicted_scores(team_combo, master_dict, driver_2x):
    team_score = 0
    for team_member in team_combo:
        if team_member in master_dict["driver"]:
            driver_score = master_dict["driver"][team_member]["predicted_score"]
            team_score+=driver_score
        else:
            team_score+=master_dict["team"][team_member]["predicted_score"]

    return team_score + master_dict["driver"][driver_2x]["predicted_score"]

def find_team_cost(team_combo, master_dict):
    team_cost = 0
    for team_member in team_combo:
        if team_member in master_dict["driver"]:
            team_cost+=master_dict["driver"][team_member]["cost"]
        else:
            team_cost+=master_dict["team"][team_member]["cost"]
    return team_cost

def how_many_drivers_differ(driver_list_1, driver_list_2):
    differing_number = 0
    for driver in driver_list_1:
        if driver not in driver_list_2:
            differing_number+=1
    return differing_number

def find_top_k_teams(master_dict, budget, top_k, previous_team):
    team_cost_array = []
    team_predicted_score_array = []
    selected_team_array = []
    driver_2x_array = []
    penalty_for_additional_team_change_array = []

    for combo_driver,combo_team  in product(combinations(master_dict["driver"].keys(), 5), combinations(master_dict["team"].keys(), 2)):
        penalty_for_additional_team_change = 0
        combo = combo_driver + combo_team
        team_cost = find_team_cost(combo, master_dict)
        if team_cost > budget:
            continue
        
        if len(previous_team)!=0:
            additional_changes = max((how_many_drivers_differ(previous_team, combo) - 2), 0)
            penalty_for_additional_team_change = 10*additional_changes

        #finding 2x driver
        driver_order_based_on_predicted_score = [(master_dict["driver"][x]["predicted_score"], x) for x in combo_driver]
        predicted_driver_2x = max(driver_order_based_on_predicted_score)[1]

        ## recalibrating 2x driver
        for driver_order in driver_order_based_on_predicted_score:
            if driver_order[1] in DOMINANT_DRIVERS:
                predicted_driver_2x = driver_order[1]
                break
        
        # driver_2x = max([(master_dict["driver"][x]["predicted_score"], x) for x in combo_driver])[1]
        # real_team_score = find_team_score_in_reality(combo, master_dict)
        predicted_team_score = find_team_score_based_on_predicted_scores(combo, master_dict, predicted_driver_2x) - penalty_for_additional_team_change
        
        # print(combo, team_cost, team_score)
        driver_2x_array.append(predicted_driver_2x)
        team_cost_array.append(team_cost)
        selected_team_array.append(list(combo))
        # team_real_score_array.append(real_team_score)
        team_predicted_score_array.append(predicted_team_score)
        penalty_for_additional_team_change_array.append(penalty_for_additional_team_change)

    top_team_df = pd.DataFrame({
        "team" : selected_team_array,
        "cost": team_cost_array,
        "predicted_score": team_predicted_score_array,
        # "real_score": team_real_score_array,
        "2x_driver": driver_2x_array,
        "additional_change_penalty": penalty_for_additional_team_change_array
    })

    return top_team_df.sort_values(by="predicted_score", ascending=False)[:top_k]