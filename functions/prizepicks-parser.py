import requests
import json
# link = "https://api.prizepicks.com/projections"
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}


# r = requests.get(link, headers=headers)
# print(r.status_code)
# print(r.text)

# I can't scrape prize picks api normally due to cloudwatch rules so the below is a workaround but I only get 1000 free calls to the API so don't spam it :)
# response = requests.get(
#   url='https://proxy.scrapeops.io/v1/',
#   params={
#       'api_key': '762bb554-8720-4a69-963c-e0b91b9fe07e',
#       'url': 'https://api.prizepicks.com/projections', 
#   },
# )

# data = response.json()
# print(data)

file = open('temp-projections/projections2-23.json')
data = json.load(file)

#This is me trying to parse through the data. still in progress.
for entry in data['data']:
    if entry['type'] != "projection":
        continue
    attributes = entry['attributes']
    if attributes['projection_type'] != 'Single Stat':
        continue
    if attributes['stat_type'] != 'Rebounds' & attributes['state_type'] != 'Points' & attributes['state_type'] != 'Assists' 