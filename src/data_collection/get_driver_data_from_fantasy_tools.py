import requests
import json
import os
from utils import read_json, write_json
from config import fantasy_tools_driver_code_to_driver_mapping as name_mapping
from config import TEAM_DATA_PATH, DRIVER_DATA_PATH


class F1FantasyRecorder:
    def __init__(self,driver_url, constructor_url):
        self.driver_url = driver_url
        self.constructor_url = constructor_url

    def write_value_to_driver_dict(self, driver_code, value_array, json_key):
        for i,value in enumerate(value_array):
            driver_data_json = {}
            race_no = f"race_{i+1}"
            file_name = f"{name_mapping[driver_code]}.json"
            file_path = os.path.join(DRIVER_DATA_PATH,file_name)
            if os.path.isfile(file_path):
                driver_data_json = read_json(file_path)

            should_write = False
                
            if race_no in driver_data_json:
                if json_key not in driver_data_json[f"race_{i+1}"]:
                    driver_data_json[f"race_{i+1}"][json_key] = value
                    should_write = True
            else:
                driver_data_json[f"race_{i+1}"] = {}
                driver_data_json[f"race_{i+1}"][json_key] = value
                should_write = True
            
            if should_write:
                write_json(file_path, driver_data_json)
    
    def write_value_to_constructor_dict(self, team_code, points_array, cost_array, cost_change_array):
        for i, (score, cost, cost_change) in enumerate(zip(points_array, cost_array, cost_change_array)):
            team_data_json = {}
            race_no = f"race_{i+1}"
            file_name = "constructor_info.json"
            file_path = os.path.join(TEAM_DATA_PATH,file_name)

            if os.path.isfile(file_path):
                team_data_json = read_json(file_path)

            if race_no not in team_data_json:
                team_data_json[race_no] = {}
            
            if team_code not in team_data_json[race_no]:
                team_data_json[race_no][team_code] = {"cost": cost, "score": score, "cost_change": cost_change}
                write_json(file_path, team_data_json)

    def get_fantasy_data(self, url):
        resp = requests.get(url, timeout=30)
        content = json.loads(resp.content)
        return content
    
    def parse_fantasy_driver_data(self, content):
        for row in content:
            driver_code = row["abbreviation"]
            print("populating for ", driver_code)
            fantasy_points_array = row["race_results"][0]["results_per_race_list"]
            fantasy_cost_array = row["race_results"][1]["results_per_race_list"]
            cost_change_array = row["race_results"][2]["results_per_race_list"]
            fastest_lap_array = row["race_results"][11]["results_per_race_list"]
            dnf_array = row["race_results"][12]["results_per_race_list"]
            pos_gain_array = row["race_results"][13]["results_per_race_list"]
            overtake_array = row["race_results"][14]["results_per_race_list"]
            dotd_array = row["race_results"][15]["results_per_race_list"]
            
            self.write_value_to_driver_dict(driver_code, fantasy_points_array, "fantasy_score")
            self.write_value_to_driver_dict(driver_code, fantasy_cost_array, "fantasy_cost")
            self.write_value_to_driver_dict(driver_code, cost_change_array, "cost_change")
            self.write_value_to_driver_dict(driver_code, fastest_lap_array, "fastest_lap")
            self.write_value_to_driver_dict(driver_code, dnf_array, "dnf")
            self.write_value_to_driver_dict(driver_code, pos_gain_array, "pos_gained")
            self.write_value_to_driver_dict(driver_code, overtake_array, "overtake")
            self.write_value_to_driver_dict(driver_code, dotd_array, "dotd")

    def parse_fantasy_constructor_data(self, content):
        for row in content:
            team_code = row["abbreviation"].lower()
            print("populating for ", team_code)
            fantasy_points_array = row["race_results"][0]["results_per_race_list"]
            fantasy_cost_array = row["race_results"][1]["results_per_race_list"]
            cost_change_array = row["race_results"][2]["results_per_race_list"]
            self.write_value_to_constructor_dict(team_code, fantasy_points_array, fantasy_cost_array, cost_change_array)

    def populate_fantasy_driver_info(self):
        content = self.get_fantasy_data(self.driver_url)
        self.parse_fantasy_driver_data(content)

    def populate_constructors_info(self):
        content = self.get_fantasy_data(self.constructor_url)
        self.parse_fantasy_constructor_data(content)


    
