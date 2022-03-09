#!/usr/bin/env python
# coding: utf-8


import googlemaps # pip install googlemaps
from bs4 import BeautifulSoup


def get_1st_location(query):
    try:
        API_KEY = "Your API Key"
        map_client = googlemaps.Client(API_KEY)
        response = map_client.places(query=query)
        # get the 1st result
        result = response.get('results')[0]
        return result
    except Exception as e:
        print(e)
        return None


if __name__=="__main__":
    result = get_1st_location("trader joes")
    html_text = result['photos'][0]['html_attributions'][0]
    soup = BeautifulSoup(html_text, 'html.parser')
    print("Photo link: "+soup.find('a').get('href'))
    if 'establishment' in result['types']:
        print("Name: "+result['name'])
        print("Address: "+result['formatted_address'])
        print("Opening hours: "+"open now" if result['opening_hours']['open_now'] else "closed now")
        print("Rating: "+str(result['rating']))
        print("Price_level: "+"$"*int(result['price_level']))
    else:
        print("Not an establishment, unable to print results.")


