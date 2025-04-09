from config import driver_code_to_driver_mapping as name_mapping, substitute_drivers

def get_filename_based_on_driver_code(driver_code, race_name):
    if driver_code not in name_mapping.keys():
        file_name = f"{substitute_drivers[driver_code][race_name]}.json"
    else:
        file_name = f"{name_mapping[driver_code]}.json"
    return file_name

def transform_data_json_to_dataframe():
    pass


