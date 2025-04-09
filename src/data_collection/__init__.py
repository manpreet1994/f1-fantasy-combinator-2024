import os
from . import get_driver_data_from_f1

base_website = "https://www.formula1.com/en/results/2024/races"
ALL_URLS = [
    f"{base_website}/1229/bahrain/",
    f"{base_website}/1230/saudi-arabia/",
    f"{base_website}/1231/australia/",
    f"{base_website}/1232/japan/",
    f"{base_website}/1233/china/",
    f"{base_website}/1234/miami/",
    f"{base_website}/1235/emilia-romagna/",
    f"{base_website}/1236/monaco/",
    f"{base_website}/1237/canada/",
    f"{base_website}/1238/spain/",
    f"{base_website}/1239/austria/",
    f"{base_website}/1240/great-britain/",
    f"{base_website}/1241/hungary/",
    f"{base_website}/1242/belgium/",
    f"{base_website}/1243/netherlands/",
    f"{base_website}/1244/italy/",
    f"{base_website}/1245/azerbaijan/",
    f"{base_website}/1246/singapore/",
    f"{base_website}/1247/united-states/",
    f"{base_website}/1248/mexico/",
    f"{base_website}/1249/brazil/",
    f"{base_website}/1250/las-vegas/",
    f"{base_website}/1251/qatar/",
    f"{base_website}/1252/abu-dhabi/",
]

SPRINT_WEEK = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
__all__ = [
    "get_driver_data_from_f1"
]

