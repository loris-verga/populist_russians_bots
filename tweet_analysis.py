import numpy as np
import csv
import datetime
from constants import *


def _get_tweet_count_per_day_for_one_file(input_file, date_array, filter_function=None, category=None):
    """
    This function counts the number of tweets per day, optionally applying a filter to each tweet.

    :param input_file: The file containing tweet data with dates and text.
    :param date_array: An array of datetime64 objects representing each day within the desired date range.
    :param filter_function: A function that takes a tweet's text and returns True if the tweet should be counted,
                            or None if all tweets should be counted.
    :return: An array of integers where each element represents the number of tweets for the corresponding day in
    the date_array.
    """

    # Initialize an array to store the number of tweets per day
    tweet_count_per_day = np.zeros(date_array.shape)


    # Open the input file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:


        reader = csv.reader(infile)

        # Read the header row to skip it
        next(reader)

        # Process each row in the input file
        for row in reader:

            # If a filter function is provided, use it to determine if the tweet should be counted
            if filter_function and not filter_function(row[1]):
                continue

            # check if we need to filter with the type of troll and if yes, check if it is the right category of troll
            if not (not category or (category and row[2] == category)):
                continue

                # Extract the year, month, and day from the row
            year = int(row[3])
            month = int(row[4])
            day = int(row[5])

            # Create a date object from the extracted year, month, and day
            date = datetime.date(year, month, day)

            # Convert the date object to a numpy datetime64 object
            numpy_date = np.datetime64(date)

            # Find the index of the numpy_date in the date_array
            index = np.where(date_array == numpy_date)

            # Increment the tweet count for that specific day
            tweet_count_per_day[index] += 1

    return tweet_count_per_day


def _get_number_of_tweet_each_day_for_one_file(input_file, date_array, category=None):
    """
    This method calculates the number of tweets for each day within the given date array.

    :param input_file: The file containing tweet data with dates.
    :param date_array: An array of datetime64 objects representing each day within the desired range.
    :return: An array of integers where each element represents the number of tweets for the corresponding day
    in the date_array.
    """
    return _get_tweet_count_per_day_for_one_file(input_file, date_array, category=category)


def _get_number_of_tweets_per_day_with_at_least_one_word__for_one_file(input_file, dictionary, date_array,
                                                                       category=None):
    """
    This function counts the number of tweets per day that contain at least one word from a given dictionary.

    :param input_file: The file containing tweet data with dates and text.
    :param dictionary: A set of words to search for within each tweet.
    :param date_array: An array of datetime64 objects representing each day within the desired date range.
    :return: An array of integers where each element represents the number of tweets containing at least one
     word from the dictionary
             for the corresponding day in the date_array.
    """

    def contains_any_word(text):
        return contains_any_substring(text, dictionary)

    return _get_tweet_count_per_day_for_one_file(input_file, date_array, contains_any_word, category=category)


def contains_any_substring(text, substring_set):
    """
    This function checks if any of the substrings in the given set are present in the provided text.

    :param text: The text in which to search for substrings.
    :param substring_set: A set of substrings to look for in the text.
    :return: True if any of the substrings are found within the text, otherwise False.
    """

    # Iterate over each substring in the set
    for substring in substring_set:
        # Check if the current substring is present in the text
        if substring in text:
            # Return True if any substring is found
            return True

    # If no substrings are found in the text, return False
    return False


def dataset_analysis(dictionary, date_array, category=None):
    """
    This function aggregates the number of tweets per day that contain at least one word from a given dictionary,
    across multiple datasets.

    :param category: A filter for category of tweet: example RightTroll
    :param dictionary: A set of words to search for within each tweet.
    :param date_array: An array of datetime64 objects representing each day within the desired date range.

    :return: An array of integers where each element represents the total number of tweets containing at least one word
             from the dictionary for the corresponding day in the date_array, summed across all datasets.
    """

    # Initialize an array to store the cumulative number of tweets per day across all datasets
    nb = np.zeros(date_array.shape)

    # Loop over the datasets, assuming there are 13 datasets with filenames following a specific pattern
    import time
    t = time.time()
    for i in range(1, 14):
        print("processing file {}".format(i))
        print(time.time() - t)
        # Generate the filename for the current dataset
        file_path = PRE_PROCESSED_DATA_PATH.format(i)

        # Get the number of tweets per day for the current dataset that contain at least one word from the dictionary
        nb += _get_number_of_tweets_per_day_with_at_least_one_word__for_one_file(file_path, dictionary, date_array,
                                                                                 category=category)

    # Return the cumulative number of tweets per day across all datasets
    return nb


def get_nb_of_tweets_per_day(date_array, category=None):
    """
    This function calculates the total number of tweets per day across all datasets.
    :param category: A filter for category of tweet: example RightTroll
    :param category:
    :param date_array: An array of datetime64 objects representing each day within the desired date range.
    :return: An array of integers where each element represents the total number of tweets for the corresponding day
             in the date_array, summed across all datasets.
    """

    # Initialize an array to store the cumulative number of tweets per day across all datasets
    total_tweets = np.zeros(date_array.shape)

    # Loop over the datasets, assuming there are 13 datasets with filenames following a specific pattern

    for i in range(1, 14):
        # Generate the filename for the current dataset
        file_path = PRE_PROCESSED_DATA_PATH.format(i)

        # Get the total number of tweets per day for the current dataset
        total_tweets += _get_number_of_tweet_each_day_for_one_file(file_path, date_array, category=category)

    # Return the cumulative number of tweets per day across all datasets
    return total_tweets
