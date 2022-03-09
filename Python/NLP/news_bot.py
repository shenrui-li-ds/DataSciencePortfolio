#!/usr/bin/env python
# coding: utf-8


import requests
from gnewsclient import gnewsclient  #!pip install gnewsclient


# get your location by your public IP address
_res = requests.get('https://ipinfo.io/')
_data = _res.json()
# get my current location via request
CITY = _data['city']
LOCATION = _data['loc'].split(',')
LATTITUDE = LOCATION[0]
LONGITUDE = LOCATION[1]


# import module
def get_1st_news(query=CITY):
    # declare a NewsClient object
    client = gnewsclient.NewsClient(language='en', location=query, topic='Nation', max_results=5)
    # get news feed
    news_feed = client.get_news()
    # return the first on the feed
    return news_feed[0]


if __name__=="__main__":
    news = get_1st_news("United States")
    print("Title: "+news['title'])
    print("Link: "+news['link'])


