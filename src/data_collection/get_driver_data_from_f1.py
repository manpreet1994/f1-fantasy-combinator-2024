import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import read_json, write_json
from .utils import get_filename_based_on_driver_code
from config import DRIVER_DATA_PATH

class F1DataRecorder:
    def __init__(self, url, race_no, race_name):
        self.base_url = url
        self.race_no = race_no
        self.race_name = race_name
    
    def parse_table_elements(self, table_element_soup, no_of_elements_in_a_row):
        driver_array = []
        array_of_interest = []
        counter=1
        for table_element in table_element_soup:
            table_content = table_element.text
            if counter%no_of_elements_in_a_row == 1:
                array_of_interest.append(table_content)
            elif counter%no_of_elements_in_a_row == 3:
                driver_array.append(table_content[-3:])
            counter+=1
        return driver_array, array_of_interest

    def write_value_to_driver_dict(self, driver_array, value_array, json_key):
        for driver, value in zip(driver_array[:20], value_array[:20]):
            file_name = get_filename_based_on_driver_code(driver, self.race_name)
            file_path = os.path.join(DRIVER_DATA_PATH,file_name)
            race_no = f"race_{self.race_no}"
            if os.path.isfile(file_path):
                driver_data_json = read_json(file_path)
            else:
                driver_data_json = {}

            should_write_data = False

            if race_no in driver_data_json:
                if json_key not in driver_data_json[race_no]:
                    driver_data_json[f"race_{self.race_no}"]["race_name"] = self.race_name
                    driver_data_json[f"race_{self.race_no}"][json_key] = value
                    should_write_data = True
            else:
                driver_data_json[f"race_{self.race_no}"] = {"race_name": self.race_name}
                driver_data_json[f"race_{self.race_no}"][json_key] = value
                should_write_data = True
            
            if should_write_data:
                write_json(file_path, driver_data_json)

    def record_driver_race_position(self):
        url = urljoin(self.base_url, "race-result")
        html_info = requests.get(url)
        if html_info.status_code == 200:
            soup = BeautifulSoup(html_info.text, features="html.parser")
            table_with_data_html=soup.find_all(class_="f1-table f1-table-with-data w-full")[0]

            driver_array, race_position_array = self.parse_table_elements(table_with_data_html.find_all("td"), 7)

            self.write_value_to_driver_dict(driver_array, race_position_array, "race_pos")

    def record_driver_quali_position(self):
        url = urljoin(self.base_url, "qualifying")
        html_info = requests.get(url)
        if html_info.status_code == 200:
            soup = BeautifulSoup(html_info.text, features="html.parser")
            table_with_data_html=soup.find_all(class_="f1-table f1-table-with-data w-full")[0]
            driver_array, quali_position_array = self.parse_table_elements(table_with_data_html.find_all("td"), 8)

        self.write_value_to_driver_dict(driver_array, quali_position_array, "quali_pos")

    
    def record_practice_1(self):
        url = urljoin(self.base_url, "practice/1")
        html_info = requests.get(url)
        if html_info.status_code == 200:
            soup = BeautifulSoup(html_info.text, features="html.parser")
            table_with_data_html=soup.find_all(class_="f1-table f1-table-with-data w-full")[0]
            driver_array, fp1_position_array = self.parse_table_elements(table_with_data_html.find_all("td"), 7)
            self.write_value_to_driver_dict(driver_array, fp1_position_array, "fp1")

    def record_practice_2(self):
        url = urljoin(self.base_url, "practice/2")
        html_info = requests.get(url)
        if html_info.status_code == 200:
            soup = BeautifulSoup(html_info.text, features="html.parser")
            table_with_data_html=soup.find_all(class_="f1-table f1-table-with-data w-full")[0]
            driver_array, fp2_position_array = self.parse_table_elements(table_with_data_html.find_all("td"), 7)

            self.write_value_to_driver_dict(driver_array, fp2_position_array, "fp2")

    def record_practice_3(self):
        url = urljoin(self.base_url, "practice/3")
        html_info = requests.get(url)
        if html_info.status_code == 200:
            soup = BeautifulSoup(html_info.text, features="html.parser")
            table_with_data_html=soup.find_all(class_="f1-table f1-table-with-data w-full")[0]
            driver_array, fp3_position_array = self.parse_table_elements(table_with_data_html.find_all("td"), 7)
            self.write_value_to_driver_dict(driver_array, fp3_position_array, "fp3")

    def record_sprint_quali(self):
        url = urljoin(self.base_url, "sprint-qualifying")
        html_info = requests.get(url)
        if html_info.status_code == 200:
            soup = BeautifulSoup(html_info.text, features="html.parser")
            table_with_data_html=soup.find_all(class_="f1-table f1-table-with-data w-full")[0]
            driver_array, sprint_quali_array = self.parse_table_elements(table_with_data_html.find_all("td"), 8)
            self.write_value_to_driver_dict(driver_array, sprint_quali_array, "sprint_quali")

    def data_collection_using_f1_website(self, is_sprint_weekend):
        if is_sprint_weekend:
            self.record_driver_race_position()
            self.record_driver_quali_position()
            self.record_practice_1()
            self.record_sprint_quali()
        else:
            self.record_driver_race_position()
            self.record_driver_quali_position()
            self.record_practice_1()
            self.record_practice_2()
            self.record_practice_3()