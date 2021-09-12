# Donal Rynne - Data Analytics for Business - Final Project (Project Rubric)


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# write all Olympic years to identify same
olympic_year_list = [1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012,
                     2016, 2020]


# import olympic medals base data
def get_medals_dict():
    with open('Country_Medals_New.csv', mode='r') as infile:
        next(infile)  # skip header
        reader = csv.reader(infile)
        # key is Country_Code & Year as integer value with each of medal count. Return True where country is host
        return {tuple([rows[1][1:-1], int(rows[0])]): [rows[5], rows[6], rows[7], rows[2] == rows[4]] for rows in
                reader}


# def get_gdp_dict()
def get_gdp_dict():
    with open('gdp.csv', mode='r') as infile:  #
        next(infile)  # skip header
        reader = csv.reader(infile)
        combined_dict = {}
        for rows in reader:
            get_closest_olympic_year(int(rows[5]))
            if rows[0] is not None and rows[1] is not None:
                combined_dict[rows[0]] = [(rows[5]), (rows[6])]
        return get_gdp_dict


def get_population_dict():
    with open('pop.csv', mode='r') as infile:
        next(infile)  # skip header
        reader = csv.reader(infile)
        return {tuple([rows[0], int(rows[5])]): [rows[6]] for rows in reader}


# apply reusable logic to matching olympic years, subject to defined olympic year list
def get_closest_olympic_year(year):
    count = 0
    while count + 1 < len(olympic_year_list) and year >= olympic_year_list[count + 1]:
        count += 1
    return olympic_year_list[count]


def merge_dictionaries(d1, d2):
    for key, value in d1.items():
        if key in d2:
            value.extend(d2[key])
        else:
            value.extend([None])
    return d1


def write_results(output_dict):
    with open('mycsvfile.csv', 'w') as f:
        w = csv.DictWriter(f, output_dict.keys())
        w.writeheader()
        w.writerow(output_dict)
    dataframe = pd.DataFrame(output_dict)
    dataframe.transpose().to_csv('output.csv')


def run():
    #gdp = get_gdp_dict()
    #pop = get_population_dict()
    merged_dictionaries = merge_dictionaries(get_gdp_dict, get_population_dict)

    #merged_dictionaries = get_gdp_dict()
    #merged_dictionaries =  get_combined_dict()

    medals = get_medals_dict()
    for key, value in medals.items():
        #if key[0] in merged_dictionaries:
            #if len(key[0]) == 3:
        #        value.extend(merged_dictionaries[key[0]])
            #else:
            #    print(key[0])
        #else:
        #    value.extend([None, None])
        value.extend(merged_dictionaries[key[0]] if key[0] in merged_dictionaries else [None, None]) #add population and gdp

    write_results(medals)


run()





print(get_medals_dict())
print(get_population_dict())
print(get_combined_dict())

