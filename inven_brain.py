import numpy as np
from collections import Counter
import pandas as pd
import cfg

# also need global key-variables like:
    # product
    # qty

dict_scanner = [
    {'product': 'cabernet', 'qty': 33},
    {'product': 'rose', 'qty': 66},
    {'product': 'bob jones', 'qty': 99}
    ]

dict_tab = [
    {'product': 'mint mobile', 'qty': 100},
    {'product': 'cabernet', 'qty': 200},
    {'product': 'rose', 'qty': 300},
    {'product': 'bob jones', 'qty': 400}
    ]

dict_sync = []

# dictionaries for testing purposes
    # use for testing on dict_parser
dict1 = {'a': 5, 'b': 7}
dict2 = {'a': 3, 'c': 1}
dict3 = []


def dict_sum():

result = {key: dict1.get(key, 0) + dict2.get(key, 0)
          for key in set(dict1) | set(dict2)}
print('dict_test result: ', result)


# task: create a function that iterates through a list of dictionaries -
    # until matching the ('product') of the input dict, then sums their ints and updates
def dict_parser():
    for pair in dict1:
        if

        dict3.append(
            {key: dict1.get(key, 0) + dict2.get(key, 0)
             for key in set(dict1) | set(dict2)}
        )

# note that:
    # dict_live_scanner = sheet2api.get_rows()
    # which means this ledger is constantly being updated to every 3 seconds
    # dict_clone_scanner = the previous clone of the excell sheet as a list of dictionaries
    # aka this is the


# create function as such: excell ledger comparator
    # if dict_live_scanner ==! dict_clone_scanner
        #



