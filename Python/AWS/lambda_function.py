#!/usr/bin/env python
# coding: utf-8

# define required dependencies in requirements.txt
# imaginary home price prediction work flow
# call predict method in another .py file called home_price in the same directory and return result
import home_price as hp
import json


def lambda_handler(event=None, context=None):
    '''
    Handles request to the API and return the prediction result
    
    :param event: the data from the event that triggered the function
    :param context: the data about the execution environment of the function
    :return response: the prediction result in float format
    '''
    
    sqft_living = float(event['sqft_living'])
    sqft_lot = float(event['sqft_lot'])
    bathrooms = int(event['bathrooms'])
    bedrooms = int(event['bedrooms'])
    highway = int(event['highway'])
    waterfront = int(event['waterfront'])
    age = 2022-int(event['yr_built'])
    zipcode = str(event['zipcode'])

    result = hp.predict(sqft_living, sqft_lot, bathrooms, bedrooms, highway, waterfront, age, zipcode)
    
    response = {
        "status": 200,
        "home_price": result,
    }
    return response

