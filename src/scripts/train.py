import argparse
import os
from config import MODEL_PATH, DRIVER_DATA_PATH, MODEL_TYPE, FEATURE_SET
from model_training.training import train_fantasy_score_from_practice_model as train
from utils import read_json, write_json, save_pickle, read_pickle


def train_a_model():
    model_file_path = os.path.join(MODEL_PATH,"model_dict.pkl")
    parser = argparse.ArgumentParser()
    parser.add_argument("--race_no", type=int)
    args = parser.parse_args()
    till_race_no = args.race_no
    if till_race_no!=1:
        # read previously present model
        if os.path.exists(model_file_path):
            model_dict = read_pickle(model_file_path) 
        else:
            model_dict = {}
        for driver_file in os.listdir(DRIVER_DATA_PATH):
            driver_name = driver_file.split(".")[0]
            driver_json = read_json(os.path.join(DRIVER_DATA_PATH, driver_file))
            model_dict = train(model_dict, MODEL_TYPE, FEATURE_SET, driver_name, driver_json, till_race_no)
        save_pickle(model_file_path, model_dict)
        return "Model Updated"
    else:
        return "First race, no data to train"


if __name__== "__main__":
    print(train_a_model())
