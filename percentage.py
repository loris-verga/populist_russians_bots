import numpy as np


def safe_percentage(a, b):
    if b == 0:
        return 0
    else:
        return 100 * (a / b)


def percentage_of_tweets(result, nb_of_tweets):
    vectorized_function = np.vectorize(safe_percentage)

    return vectorized_function(result, nb_of_tweets)
