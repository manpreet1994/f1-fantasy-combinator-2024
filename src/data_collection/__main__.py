from .get_driver_data_from_f1 import F1DataRecorder
from .get_driver_data_from_fantasy_tools import F1FantasyRecorder
from . import SPRINT_WEEK, ALL_URLS
from config import F1_FANTASY_CONSTRUCTOR_URL, F1_FANTASY_DRIVER_URL

def data_collection_using_f1_website(url, race_no, race_name, is_sprint_weekend):
    f1_recorder = F1DataRecorder(url, race_no, race_name)
    if is_sprint_weekend:
        f1_recorder.record_driver_race_position()
        f1_recorder.record_driver_quali_position()
        f1_recorder.record_practice_1()
        f1_recorder.record_sprint_quali()
    else:
        f1_recorder.record_driver_race_position()
        f1_recorder.record_driver_quali_position()
        f1_recorder.record_practice_1()
        f1_recorder.record_practice_2()
        f1_recorder.record_practice_3()
    print(f"processed f1 website data collection for {race_name}")

# def data_collection_using_fantasy_tool():
#     fantasy_url = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/driver?season=2024"
#     f1_fantasy_recorder = F1FantasyRecorder(fantasy_url)
#     f1_fantasy_recorder.populate_fantasy_driver_info()

# def data_collection_for_contructors():
#     fantasy_url = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/constructor?season=2024"
#     f1_fantasy_recorder = F1FantasyRecorder(fantasy_url)
#     f1_fantasy_recorder.populate_constructors_info()

def data_collection_for_whole_season():
    race_counter=1
    for url, is_sprint_weekend in zip(ALL_URLS, SPRINT_WEEK):
        race_name = url.split("/")[-2]
        f1_recorder = F1DataRecorder(url, race_counter, race_name)
        f1_recorder.data_collection_using_f1_website(is_sprint_weekend)
        # data_collection_using_f1_website(url, race_counter, url.split("/")[-2], is_sprint_weekend)
        race_counter+=1
    f1_fantasy_recorder = F1FantasyRecorder(F1_FANTASY_DRIVER_URL, F1_FANTASY_CONSTRUCTOR_URL)
    f1_fantasy_recorder.populate_fantasy_driver_info()
    f1_fantasy_recorder.populate_constructors_info()

data_collection_for_whole_season()

