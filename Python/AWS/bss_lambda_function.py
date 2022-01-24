#!/usr/bin/env python
# coding: utf-8

# define required dependencies in requirements.txt
# conduct cash flow analysis in another .py file called bss_aws in the same directory and import here
import bss_aws as bss
import json


def lambda_handler(event=None, context=None):
    '''
    Handles request to the API and return the simulation result
    
    :param event: the data from the event that triggered the function
    :param context: the data about the execution environment of the function
    :return response: the simulation result in a list object
    '''
    
    bank_acct_list = event['bank_accounts']
    principal = float(event['offer_amount'])
    interest = float(event['interest_rate'])/100
    term = float(event['term'])
    fico = float(event['pg_fico'])
    officer_compensations = float(0)

    simulation = bss.main(bank_acct_list, principal, interest, term, fico, officer_compensations)
    
    response = {
        "status": 200,
        "total_payments": simulation[0],
        "default_rate": simulation[1],
        "expected_return": simulation[2], 
        "loss_given_default": simulation[3],
    }
    return response

