import json

with open('covid_cases.json') as json_file:
    covid = json.loads(json_file.read())