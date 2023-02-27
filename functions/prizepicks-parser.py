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

file = open('temp-projections/projections2-25.json', encoding="utf-8")
data = json.load(file)

#This is me trying to parse through the data.
predictions = []
stats = {'Rebounds', "Points", "Assists"}
num=0
for entry in data['data']:
    try:

        if entry['type'] != "projection":
            continue
        attributes = entry['attributes']
        if attributes['projection_type'] != 'Single Stat':
            continue
        if attributes['stat_type'] not in stats:
            continue 
        if entry['relationships']['league']['data']['id'] != "7":
            continue

        values = []
        values.append(str(attributes['line_score']))
        values.append(str(attributes['stat_type']))
        #print(entry['relationships']['new_player']['data']['id'])
        player = next(item for item in data['included'] if (item["type"] == "new_player" and item['id'] == entry['relationships']['new_player']['data']['id']))
        values.append(player['attributes']['name'])
        predictions.append(values)
        #print(" ".join(string))
        num +=1
    except:
        continue

print(num)
print(predictions)
