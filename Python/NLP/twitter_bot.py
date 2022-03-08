#!/usr/bin/env python
# coding: utf-8


import tweepy
import re
import requests

consumer_key = "your consumer key"
consumer_secret = "your consumer secret"
access_token = "your access token"
access_token_secret = "your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# get your location by your public IP address
_res = requests.get('https://ipinfo.io/')
_data = _res.json()
# get my current location via request
CITY = _data['city']
LOCATION = _data['loc'].split(',')
LATTITUDE = LOCATION[0]
LONGITUDE = LOCATION[1]


def get_trend_in_my_loc():
    # get closest location and trending topics in this location
    closest_loc = api.closest_trends(LATTITUDE, LONGITUDE)
    trends = api.get_place_trends(closest_loc[0]['woeid'])
    top10_trend = trends[0]['trends'][:10]
    top10_trend_list = [topic['name'] for topic in top10_trend]
    top10_trend_str = \
        "Trending topic for "+trends[0]['locations'][0]['name']+":\n"+\
        "\n".join(top10_trend_list)
    return trends, top10_trend_str


def get_most_popular_tweet():
    closest_loc = api.closest_trends(LATTITUDE, LONGITUDE)
    trends = api.get_place_trends(closest_loc[0]['woeid'])
    keyword = [topic['name'] for topic in trends[0]['trends']][0]
    text = api.search_tweets(keyword)[0].text
    return text


def get_first_tweet_on_timeline():
    text = api.home_timeline()[0].text
    return text


