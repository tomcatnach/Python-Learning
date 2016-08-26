import random
import sys
import os
import json
from pprint import pprint

with open('example_call.json') as json_file:
    data = json.load(json_file)

# print len(basket)

a = len(data["basket"])
b = len(data["stores"][0]["products"])
c = len(data["stores"][1]["products"])

if a == b and a == c :
    print ("Test 3")
elif (a == b and a != c) or (a == c and a != b):
    print ("Test 2")
else:
    print ("Test 1")

y = 0
x = 1

for store in (data["stores"]):
    for product in (data["stores"][y]["products"]):
        print (product)

print (data["basket"])