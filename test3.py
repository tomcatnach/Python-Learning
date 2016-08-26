import json

with open('example_call.json') as json_file:
    array = json.load(json_file)
    json_string = str(array, 'utf8')

data  = json.loads(json_string)
print (data['basket'])