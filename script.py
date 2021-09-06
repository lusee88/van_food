from ast import Str
import numpy as np
import pandas as pd
import argparse
from typing import List, Dict, Tuple, NewType
import random

NAME_COL = 0
FOOD_TYPE_COL = 1
LOC_COL = 2
DETAILS_COL = 3
PRIORITY_COL = 7

def process_data(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    food_categories = data[:,FOOD_TYPE_COL]
    locations = data[:,LOC_COL]

    return food_categories, locations

def prioritize(priority: np.ndarray) -> Tuple[str, str]:
    min_arr = min(priority.values())
    min_val = min_arr[0]
    min_list = []
    for key, val in priority.items():
        if val[0] == min_val:
            min_list.append([key, val[1]])
    z = random.randint(0, len(min_list) - 1)

    return min_list[z][0], min_list[z][1]

def filter_search(data: np.ndarray, food_type: str, location: str) -> Tuple[str, str]:
    priority_arr = {}
    for res_info in data:
        if food_type in res_info and location in res_info[LOC_COL]:
            priority_arr[res_info[NAME_COL]] = [float(res_info[PRIORITY_COL]), res_info[DETAILS_COL]]
    return prioritize(priority_arr)

if __name__ == "__main__":
    df = pd.read_excel(r'food_places.xls')
    # print(pd.read_excel(r'food_places.xls', usecols='A'))
    data = df.values # this is a numpy.ndarray type

    food_categories, locations = process_data(data)
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("Display", help="Display either food categories, locations, or descriptions")

    food_type = input("What type of food are you looking for? ")
    while food_type not in food_categories:
        print("That food category is invalid, please select from the following: ")
        print(set(food_categories))
        food_type = input("Pick a valid food category: ")
    
    location = input("Where would you like to eat? ")
    while location not in locations:
        print("That location is invalid, please select from the following: ")
        print(set(locations))
        location = input("Pick a valid location: ")
    
    print(filter_search(data, food_type, location))
    



