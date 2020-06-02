"""
This script contains functions for data manipulation.

1. tweets_to_df

"""

import pandas as pd


def tweets_to_df(tweets):
    """
    Takes in a list of tweets and returns a pandas dataframe of them.
    Columns used are the same as the object for a single tweet.
    :param: tweets - list of Tweet Objects
    :return: pandas dataframe
    """
    df = pd.DataFrame([tw.__dict__ for tw in tweets], columns=tweets[0].__dict__.keys())
    return df

