import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.ndimage import gaussian_filter1d

def plot_result(date_array, result, start_date, end_date,
                ylabel="Number of Tweets",
                title="Number of Tweets per Day",
                smoothing_window=20):
    """
    This function plots the results within a specified date range
    and also adds a smoothed line to the plot.

    :param date_array: An array of datetime64 objects representing a continuous range of dates.
    :param result: An array of integers representing the data to be plotted, corresponding to each date in the date_array.
    :param start_date: The start date for the plot.
    :param end_date: The end date for the plot.
    :param ylabel: The name of the label of the y-axis.
    :param title: The title of the plot.
    :param smoothing_window: The window size for calculating the rolling average.
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

    # Plot the original data with some transparency
    plt.plot(data_axis_x, data_axis_y, color="black",  alpha=0.4, label='Results')

    # Apply smoothing using rolling average
    smoothed_y_rolling = pd.Series(data_axis_y).rolling(window=smoothing_window, center=True).mean()

    # Plot the smoothed data (rolling average)
    plt.plot(data_axis_x, smoothed_y_rolling, color='black', linewidth=2, label='Rolling Average')

    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()

    # Show the plot
    plt.show()