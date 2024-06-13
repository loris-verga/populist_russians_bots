import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
import csv

start_date = datetime.date(2014, 7, 1)
end_date = datetime.date(2018, 6, 30)

delta_days = (end_date - start_date).days + 1  

date_array = np.array([start_date + datetime.timedelta(days=i) for i in range(delta_days)])

number_of_tweets_per_day = np.zeros(delta_days)

# Number of tweets per day
def get_number_of_tweet_each_day(input_file):
    # Open the input file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        
        # Read the header
        header = next(reader)
        
        # Process each row in the input file
        for row in reader:
            year = int(row[3])
            month = int(row[4])
            day = int(row[5])
            date = datetime.date(year, month, day)

            # find the index of the date in the date_range
            print(date)
            index = np.where(date_array == date)

            # Increment the number of tweets for that day
            number_of_tweets_per_day[index] += 1
            
           
print(date_array)

for i in range(1, 14):
    get_number_of_tweet_each_day("./data/filtered_data/IRAhandle_tweets_" + str(i) + ".csv")


print(np.sum(number_of_tweets_per_day, axis=0))
plt.plot(date_array, number_of_tweets_per_day)
plt.show()

