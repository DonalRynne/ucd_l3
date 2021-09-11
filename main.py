# Donal Rynne Data Analytics for Business - Final Project

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_medals_dict():
    with open('Country_Medals_New.csv', mode='r') as infile:
        next(infile)  # skip header
        reader = csv.reader(infile)
        # Key is Country_Code & Year as integer value is each of the medal counts. Return True where Country_Name same as Host_country
        return {tuple([rows[1][1:-1], int(rows[0])]): [rows[5], rows[6], rows[7], rows[2] == rows[4]] for rows in
                reader}


#def get_gdp_dict():
def get_combined_dict():
    with open('gdp.csv', mode='r') as infile: #
        next(infile) #skip header
        reader = csv.reader(infile)
        combined_dict = {}
        for rows in reader:
            #year = get_closest_olympic_year(int(rows[1]))
            #gdp_dict[tuple([rows[0], year])] = [rows[2]]
            #if rows[0] is not None and rows[1] is not None:
            #gdp_dict[tuple([rows[0], int(rows[1])])] = [rows[2]]
            combined_dict[rows[0]] = [(rows[5]), (rows[6])]
        return combined_dict


def get_population_dict():
    with open('pop.csv', mode='r') as infile:
        next(infile)  # skip header
        reader = csv.reader(infile)
        return {tuple([rows[0], int(rows[5])]): [rows[6]] for rows in reader}


print(get_medals_dict())
print(get_population_dict())
print(get_combined_dict())
