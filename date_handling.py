import numpy as np


def get_date_array(start_date, end_date):
    """
    This method generates an array of dates between a given start date and end date, inclusive.
    :param start_date: The starting date of the date range.
    :param end_date: The ending date of the date range.
    :return: An array of datetime64 objects representing each day from START_DATE to END_DATE.
    """

    # Calculate the number of days between start and end dates, inclusive.
    num_days = (end_date - start_date).astype(int) + 1

    # Create an array of integers representing each day from 0 to num_days - 1
    timedelta_array = np.arange(num_days)

    # Convert the timedelta array to a datetime array by adding it to the start date
    # np.timedelta64(1, 'D') ensures that the addition is done in terms of days
    date_array = start_date + timedelta_array * np.timedelta64(1, 'D')

    return date_array
