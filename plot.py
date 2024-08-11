import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_result(date_array, result, start_date, end_date):
    """
    This function plots the results (e.g., the number of tweets per day) within a specified date range.

    :param date_array: An array of datetime64 objects representing a continuous range of dates.
    :param result: An array of integers representing the data to be plotted, corresponding to each date in the date_array.
    :param start_date: The start date for the plot (inclusive).
    :param end_date: The end date for the plot (inclusive).
    """

    # Convert the start and end dates to numpy datetime64 objects
    f_start_date = np.datetime64(start_date)
    f_end_date = np.datetime64(end_date)

    # Find the indices of the start and end dates within the date_array
    start_index = np.where(date_array == f_start_date)[0][0]
    end_index = np.where(date_array == f_end_date)[0][0]

    # Slice the date_array and result array to get the data within the specified date range
    data_axis_x = date_array[start_index:end_index + 1]
    data_axis_y = result[start_index:end_index + 1]



    # Plot the data
    plt.plot(data_axis_x, data_axis_y)
    plt.xlabel('Date')
    plt.ylabel('Number of Tweets')
    plt.title('Number of Tweets per Day')

    plt.show()
