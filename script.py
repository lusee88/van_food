from ast import Str
import numpy as np
import pandas as pd
import argparse
from typing import List, Dict, Tuple, NewType
import random
# from openpyxl import load_workbook

NAME_COL = 0
FOOD_TYPE_COL = 1
LOC_COL = 2
DETAILS_COL = 3
PRIORITY_COL = 7
VISITED_COL = 8

def process_data(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    '''
    This function is to simply parse through the data in the excel 
    and extract the columns we need. 
    '''

    food_categories = data[:,FOOD_TYPE_COL]
    locations = data[:,LOC_COL]

    return food_categories, locations


def prioritize(priority: np.ndarray) -> Tuple[str, str]:
    '''
    This function takes a list that matches the user input
    and randomizes an index from that list and returns 
    the name of the restaurant and the description about it
    '''

    min_arr = min(priority.values())
    min_val = min_arr[0]
    min_list = []
    for key, val in priority.items():
        if val[0] == min_val:
            min_list.append([key, val[1]])
    
    # This gives a randomized index
    z = random.randint(0, len(min_list) - 1)

    return min_list[z][0], min_list[z][1]


def filter_search(data: np.ndarray, food_type: str, location: str) -> Tuple[str, str]:
    '''
    This function takes all the inputs given by the user and creates a list
    of possible restaurants that meet the requirements
    '''
    priority_arr = {}
    for res_info in data:
        if food_type in res_info and location in res_info[LOC_COL] and res_info[VISITED_COL] == 0:
            priority_arr[res_info[NAME_COL]] = [float(res_info[PRIORITY_COL]), res_info[DETAILS_COL]]
    return prioritize(priority_arr)
    

if __name__ == "__main__":
    df = pd.read_excel(r'food_places.xls')
    data = df.values # this is a numpy.ndarray type

    food_categories, locations = process_data(data)

    # this flag is used to allow us to re-pick if we don't like the results
    exiting = False
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("Display", help="Display either food categories, locations, or descriptions")

    while not exiting:
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

        exit_bool = input("Are you satisfied with this result (y/n)? ")

        if exit_bool == 'y':
            exiting = True

    print("Thank you for randomizing with us \U0001F371")  
    



