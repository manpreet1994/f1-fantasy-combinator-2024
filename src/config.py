import os
# config for f1 website
driver_code_to_driver_mapping = {
    "ALB": "wil_driver_1",
    "SAR": "wil_driver_2",
    "VER": "red_driver_1",
    "PER": "red_driver_2",
    "SAI": "fer_driver_2",
    "LEC": "fer_driver_1",
    "RUS": "mer_driver_2",
    "NOR": "mcl_driver_1",
    "HAM": "mer_driver_1",
    "PIA": "mcl_driver_2",
    "ALO": "ast_driver_1",
    "STR": "ast_driver_2",
    "ZHO": "kck_driver_2",
    "MAG": "haa_driver_2",
    "RIC": "vrb_driver_2", 
    "TSU": "vrb_driver_1",  
    "HUL": "haa_driver_1", 
    "OCO": "alp_driver_2",
    "GAS": "alp_driver_1",
    "BOT": "kck_driver_1",
    "COL": "wil_driver_2",
    "LAW": "vrb_driver_2",
}

substitute_drivers = {
    "DOO": {"great-britain":"alp_driver_1", "canada":"alp_driver_2", "abu-dhabi":"alp_driver_2"},
    "BEA": {"saudi-arabia":"fer_driver_2", "emilia-romagna":"haa_driver_2", "spain":"haa_driver_1", 
            "great-britain":"haa_driver_2", "hungary":"haa_driver_1", "azerbaijan": "haa_driver_2", "mexico":"fer_driver_1",
            "brazil": "haa_driver_2"},
    "IWA": {"japan":"vrb_driver_2", "abu-dhabi":"vrb_driver_1"},
    "HAD": {"great-britain":"red_driver_2", "abu-dhabi":"red_driver_1"},
    "SHW": {"netherlands":"kck_driver_1", "mexico":"kck_driver_2"},
    "ANT": {"italy": "mer_driver_2", "mexico":"mer_driver_1"},
    "OWA": {"mexico":"mcl_driver_1"},
    "DRU": {"mexico": "ast_driver_1", "abu-dhabi":"ast_driver_2"},
    "HIR": {"abu-dhabi":"mcl_driver_2"},
    "LEL": {"abu-dhabi":"fer_driver_2"},
    "BRO": {"abu-dhabi":"wil_driver_1"},
}

all_races = [
    "bahrain",
    "saudi-arabia",
    "australia",
    "japan",
    "china",
    "miami",
    "emilia-romagna",
    "monaco",
    "canada",
    "spain",
    "austria",
    "great-britain",
    "hungary",
    "belgium",
    "netherlands",
    "italy",
    "azerbaijan",
    "singapore",
    "united-states",
    "mexico",
    "brazil",
    "las-vegas",
    "qatar",
    "abu-dhabi",
]

#config for fantasy toolsdriver_code_to_driver_mapping = 
fantasy_tools_driver_code_to_driver_mapping ={
    "ALB": "wil_driver_1",
    "SAR": "wil_driver_2",
    "VER": "red_driver_1",
    "PER": "red_driver_2",
    "SAI": "fer_driver_2",
    "LEC": "fer_driver_1",
    "RUS": "mer_driver_2",
    "NOR": "mcl_driver_1",
    "HAM": "mer_driver_1",
    "PIA": "mcl_driver_2",
    "ALO": "ast_driver_1",
    "STR": "ast_driver_2",
    "ZHO": "kck_driver_2",
    "MAG": "haa_driver_2",
    "RIC": "vrb_driver_2", 
    "TSU": "vrb_driver_1",  
    "HUL": "haa_driver_1", 
    "DOO": "alp_driver_2",
    "GAS": "alp_driver_1",
    "BOT": "kck_driver_1",
    "COL": "wil_driver_2",
    "LAW": "vrb_driver_2",
}

constructor_code_to_name = {
    "fer" : "Ferrari",
    "ast" : "Aston",
    "mer": "Mercedes",
    "mcl": "Mclaren",
    "wil" : "William",
    "vrb" : "Vcarb",
    "kck" : "Sauber",
    "alp": "Alpine",
    "haa" : "Haas",
    "red" : "Redbull"
}
UI_NAME_DICT = {**{v:k for k,v in driver_code_to_driver_mapping.items()}, **constructor_code_to_name}

#model considerations
MODEL_TYPE = "rf"
FEATURE_SET = ['fp1', 'fp2', 'fp3', 'avg_score', 'dnf_prob', 'dotd_prob', "weighted_fp_mean"]

F1_FANTASY_DRIVER_URL = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/driver?season=2024"
F1_FANTASY_CONSTRUCTOR_URL = "https://f1fantasytoolsapi-szumjzgxfa-ew.a.run.app/race-results/constructor?season=2024"

YEAR_OF_USAGE = "2024"
DRIVER_DATA_PATH = os.path.join("data_collection", "data", YEAR_OF_USAGE, "driver")
TEAM_DATA_PATH = os.path.join("data_collection", "data", YEAR_OF_USAGE, "constructor")
MODEL_PATH = os.path.join("model_training", "model", YEAR_OF_USAGE)
PREDICTION_PATH = os.path.join("model_training", "predictions", YEAR_OF_USAGE)
PREDICTION_HTML_PATH = os.path.join("webpages", "prediction_pages", YEAR_OF_USAGE)

DOMINANT_DRIVERS = ["red_driver_1", "red_driver_2", "mcl_driver_1", "mcl_driver_2", "fer_driver_1", "fer_driver_2", "mer_driver_1", "mer_driver_2"]