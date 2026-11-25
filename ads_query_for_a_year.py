#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 16:01:34 2025

@author: maks
"""
# import the requests package and set your token in a variable for later use
import requests
import json

token="OpYQsx2xrRyJs4EonKrM6I61VQSL8c89Zu1pHhbd"

from urllib.parse import urlencode, quote_plus

encoded_query = urlencode({"q": "year:[2025]  full:,Ukraine ",
                           "fl": "title,author,bibcode,citation_count,year,ack,aff,arxiv_class,keyword,read_count",
                           "fq": "database:astronomy",
                           "sort": "citation_count desc",
                           "rows": 2000,
                          })
results = requests.get("https://api.adsabs.harvard.edu/v1/search/query?{}".format(encoded_query), \
                       headers={'Authorization': 'Bearer ' + token})


data = results.json()
file_path = '2025.json'
with open(file_path, 'w') as json_file:
    # 3. Use json.dump() to write the data to the file
    json.dump(data, json_file, indent=4) 

print(f"Data successfully saved to {file_path}")
