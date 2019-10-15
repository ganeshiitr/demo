import sys
import os
import ast
import re
import configparser
import importlib
from collections import defaultdict
import logging
import pandas as pd

def get_config(path):
    if os.path.exists(path):
        logging.info("Reading Config File %s"%path)
        app_config = configparser.SafeConfigParser(allow_no_value=True)
        app_config.read(path)
        config_values = defaultdict(dict)

        for section in app_config.keys()[1:]:
            config_values[section] = defaultdict(dict)
            for item in app_config[section].keys():
                value = app_config.get(section, item, raw=True)
                if value and len(value) > 0 and value[0] in ("[", "{", "("): #This Handles all Data Structure Too
                    config_values[section][item] = ast.literal_eval(value)
                else:
                    try:
                        config_values[section][item] = ast.literal_eval(value)
                    except Exception as e:
                        config_values[section][item] = value
                        
        return config_values
    else:
        logging.critical("Config File Not Found! Location Provided : %s"%path)
        sys.exit(1)


config_dict = get_config("router_config.ini")

mod_list = []
for key in config_dict['rules']:
    temp_list = key.split(".") + [config_dict['rules'][key]]
    mod_list.append(temp_list)
    
rule_table = pd.DataFrame(
    mod_list,
    columns=["customer", "country", "state", "city", "server"]
) 

def find_route(temp_str):
    temp_list = temp_str.split(".")
    cust_list = set(rule_table['customer'])
    country_list = set(rule_table['country'])
    state_list = set(rule_table['state'])
    city_list = set(rule_table['city'])

    filter_dict = {}

    if temp_list[0] in cust_list:
        filter_dict['customer'] = temp_list[0] 
    else:
        filter_dict['customer'] = '*'
    if temp_list[1] in country_list:
        filter_dict['country'] = temp_list[1] 
    else:
        filter_dict['country'] = '*'
    if temp_list[2] in state_list:
        filter_dict['state'] = temp_list[2]
    else:
        filter_dict['state'] = '*'
    if temp_list[3] in city_list:
        filter_dict['city'] = temp_list[3] 
    else:
        filter_dict['city'] = '*'
    query = " & ".join(["{}=='{}'".format(k, v) for k, v in filter_dict.items()])
    res = rule_table.query(query)
    return res

print find_route("customer1.us.ca.sfo")

print find_route("customer1.us.ca.sjc")

print find_route("customer2.us.tx.dfw")

print find_route("customer2.cn.tw.tai")

print find_route("customer10.us.ny.nyc")
