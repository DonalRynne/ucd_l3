# Donal Rynne - Data Analytics for Business - Final Project (Project Rubric)


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import olympic medals base data
def get_medals_dict():
    with open('Country_Medals_New.csv', mode='r') as infile:
        next(infile)  # skip header
        reader = csv.reader(infile)
        # key is Country_Code & Year as integer value with each of medal count. Return True where country is host
        return {tuple([rows[1][1:-1], int(rows[0])]): [rows[5], rows[6], rows[7], rows[2] == rows[4]] for rows in
                reader}


# identify all Olympic years
olympic_year_list = ['1952', '1956', '1960', '1964', '1968', '1972', '1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012',
                     '2016', '2020']


# Extract a GDP figure for the nearest Olympic year
def get_gdp_dict():
    with open('gdp.csv', mode='r') as infile: #
        next(infile) #skip header
        reader = csv.reader(infile)
        gdp_dict = {}
        for rows in reader:
            year = get_closest_olympic_year(rows[5])
            gdp_dict[tuple([rows[0], year])] = (int(rows[6]))
            if rows[0] is not None and rows[6] is not None:
                gdp_dict[tuple([rows[0], int(rows[5])])] = (int(rows[6]))
        return gdp_dict


# Extract a Population figure for the nearest Olympic year
def get_pop_dict():
    with open('pop.csv', mode='r') as infile: #
        next(infile) #skip header
        reader = csv.reader(infile)
        pop_dict = {}
        for rows in reader:
            year = get_closest_olympic_year(rows[5])
            pop_dict[tuple([rows[0], year])] = (int(rows[6]))
            if rows[0] is not None and rows[6] is not None:
                pop_dict[tuple([rows[0], int(rows[5])])] = (int(rows[6]))
        return pop_dict


# apply reusable logic to matching up olympic years, subject to defined olympic year list
def get_closest_olympic_year(year):
    count = 0
    while count + 1 < len(olympic_year_list) and year >= olympic_year_list[count + 1]:
        count += 1
    return olympic_year_list[count]


# write results in useful format to an output .CSV file
def write_results(output_dict):
    with open('mycsvfile.csv', 'w') as f:
        w = csv.DictWriter(f, output_dict.keys())
        #w.writeheader()
        #w.writerow(output_dict)
    dataframe = pd.DataFrame(output_dict)
    dataframe.transpose().to_csv('output.csv')


#def merge_dictionaries(d1, d2):
    #for key, value in d1.items():
        #if key in d2:
            #value.extend(d2[key])
        #else:
            #value.extend([None])
    #return d1


def run():
    gdp = get_gdp_dict()
    pop = get_pop_dict()
    merged_dictionaries = (gdp, pop)
    #merged_dictionaries = merge_dictionaries(gdp, pop)

    medals = get_medals_dict()
    for key, value in medals.items():
        if key[0] in merged_dictionaries:
            if len(key[0]) == 3:
                value.extend(merged_dictionaries[key[0]])
            else:
                print(key[0])
        else:
            value.extend(['Monkey', 'Bananas'])
            #value.extend(merged_dictionaries[key[0]] if key[0] in merged_dictionaries else [None, None]) #add population and gdp

    #print(merged_dictionaries)
    #print(medals)
    write_results(medals)

run()

print("Processing Completed")



