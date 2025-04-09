import argparse
from config import F1_FANTASY_CONSTRUCTOR_URL, F1_FANTASY_DRIVER_URL
from data_collection.get_driver_data_from_f1 import F1DataRecorder
from data_collection.get_driver_data_from_fantasy_tools import F1FantasyRecorder
parser = argparse.ArgumentParser()

parser.add_argument("--race_no")
parser.add_argument("--f1_url")
parser.add_argument("--sprint_weekend", type=int)
args = parser.parse_args()
print(args.race_no)
f1_url = args.f1_url
race_name = f1_url.split("/")[-2]
f1_recorder = F1DataRecorder(f1_url, args.race_no, race_name)
f1_fantasy_recorder = F1FantasyRecorder(F1_FANTASY_DRIVER_URL, F1_FANTASY_CONSTRUCTOR_URL)
print(f"fetching data for race no {args.race_no}")
if args.sprint_weekend:
    print("Assuming sprint weekend")
else:
    print("Assuming normal race weekend")
f1_recorder.data_collection_using_f1_website(args.sprint_weekend or 0)
f1_fantasy_recorder.populate_fantasy_driver_info()
f1_fantasy_recorder.populate_constructors_info()



