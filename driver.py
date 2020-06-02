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

search_words = "#blm"
date_since = "2020-05-23"


tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_words).setMaxTweets(3)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
for tweet in tweets:
    print(tweet.text + '\n')

print(tweets[0].__dict__)



