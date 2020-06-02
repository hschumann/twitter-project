"""
Author: Hans Schumann
BIG COLAB: Sawyer Randles

Date: #Quarantine2020

This is currently the main script for pulling tweets until this project is cleaned up and has a direction.
Right now this script does nothing except pull some tweets based on simple criteria.
"""

# imports external packages
import GetOldTweets3 as got
import pandas as pd

# import local scripts
from tools import data_manipulation

search_words = "#blm"
date_since = "2020-05-23"

# set up some criteria for the tweets
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_words).setMaxTweets(3)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# print the tweets we found
for tweet in tweets:
    print(tweet.text + '\n')

# convert those tweets into a pandas dataframe
tweets_df = data_manipulation.tweets_to_df(tweets)

print(tweets_df)



