import requests
import json
import pymongo
import datetime
import pprint

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

file = open('temp-projections/projections2-28.json', encoding="utf-8")
data = json.load(file)

#This is me trying to parse through the data.
predictions = []
stats = {'Rebounds', "Points", "Assists"}
num=0
point_predictions = []
rebound_predictions = []
assist_predictions = []
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
        #print(values)

        #For presaved projections
        if values[1] == "Points":
            point_predictions.append({
                "data": {"name": values[2]},
                "date":datetime.datetime(2023, 2, 28, 0, 0),
                "line":values[0]
            })
        if values[1] == "Rebounds":
            rebound_predictions.append({
                "data": {"name": values[2]},
                "date":datetime.datetime(2023, 2, 28, 0, 0),
                "line":values[0]
            })
        if values[1] == "Assists":
            assist_predictions.append({
                "data": {"name": values[2]},
                "date":datetime.datetime(2023, 2, 28, 0, 0),
                "line":values[0]
            })    
        

        num +=1
    except:
        continue

print(num)
#print(predictions)



# Connection to MongoDB
conn_str = "mongodb+srv://vincent:nbaprizepicks@cs4440.s5kkhzs.mongodb.net/test?retryWrites=true&w=majority"

try:
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
except Exception:
    print("Unable to connect to the server.")

try:
    db = client.prizepicks
except Exception:
    print("oops something went wrong in the connection")

collection = db.points
# pprint.pprint(collection.find_one())
collection.insert_many(point_predictions)
collection = db.assists
collection.insert_many(assist_predictions)
collection = db.rebounds
collection.insert_many(rebound_predictions)



