import numpy as np
import os
import csv


def csv_to_numpy(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            data.append(row)
    # return np.array(data)

def get_all_files_path_in_directory(directory):
    return [directory + "/" + f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_all_files_path(): 
    return get_all_files_path_in_directory("./data/original_data")

def get_number_of_line_in_csv(csv_file):
    """Return the number of line in a csv file"""
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        return sum(1 for row in csv_reader)

def get_number_of_column_in_csv(csv_file):
    """Return the number of column in a csv file"""
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        return len(next(csv_reader))
    
def get_all_unique_values_in_column(csv_file, column):
    result = set()
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            result.add(row[column])
    return result

def get_all_uniques_values_in_column_in_all_files(directory, column):
    result = set()
    for file in get_all_files_path_in_directory(directory):
        result = result.union(get_all_unique_values_in_column(file, column))
    return result


def get_unique_values(data):
    return set(data[:, 13])

def get_number_of_tweet_in_german_in_all_files(directory):
    result = 0
    for file in get_all_files_path_in_directory(directory):
        with open(file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[4] == "German":
                    result += 1
    return result

# function that extract year from string like 12/22/2015 15:16
def extract_year(date):
    return date.split(" ")[0].split("/")[2]

def get_number_of_tweet_in_german_of_each_year(directory): 
    result = {}
    for file in get_all_files_path_in_directory(directory):
        with open(file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[4] == "German":
                    year = extract_year(row[5])
                    if year not in result:
                        result[year] = 0
                    result[year] += 1
    return result




print(get_number_of_tweet_in_german_in_all_files("./data/original_data"))
print(get_number_of_tweet_in_german_of_each_year("./data/original_data"))


# print(get_unique_values(csv_to_numpy("./data/original_data/IRAhandle_tweets_1.csv")))

# print(get_number_of_line_in_csv("./data/original_data/IRAhandle_tweets_1.csv"))
# print(get_number_of_column_in_csv("./data/original_data/IRAhandle_tweets_1.csv"))
# print(get_all_uniques_values_in_column_in_all_files("./data/original_data", 13))
# print(get_all_uniques_values_in_column_in_all_files("./data/original_data", 4))