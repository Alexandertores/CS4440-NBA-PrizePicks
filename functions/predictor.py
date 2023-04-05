from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pymongo
import numpy as np
import scipy.stats as st

#Predictor Parameters
player_name = "Spencer Dinwiddie"
stat_type = "PTS" #PTS, AST, or REB
max_games = 5

#Function for calculating probability
def get_over_probability(player_stats: np.ndarray, projections: np.ndarray):
    differences = player_stats - projections
    print(differences)
    z_score = (0 - np.mean(differences)) / np.std(differences)
    return st.norm.cdf(z_score)

# Connection to MongoDB
conn_str = "mongodb+srv://vincent:nbaprizepicks@cs4440.s5kkhzs.mongodb.net/test"

try:
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
except Exception:
    print("Unable to connect to the server.")

try:
    db = client.prizepicks
except Exception:
    print("oops something went wrong in the connection")

#Collect prizepicks projections
if stat_type == "PTS":
    collection = db.points
elif stat_type == "AST":
    collection = db.assists
elif stat_type == "REB":
    collection = db.rebounds
else:
    print("Invalid stat type entered. Please enter valid stat type")
    client.close()
    exit()

projections = []
query = {"data": {"name": player_name}}
for doc in collection.find(query).sort('date', -1):
    print(doc)
    projections.append(doc['line'])
    if len(projections) >= max_games:
        break
client.close()

if len(projections) == 0:
    print("Sorry, no prizepicks projects for this player yet. Try a different player")
    exit()
projections = np.array(projections).astype(float)
print(projections)

#Collect player stats
#TODO Solve edge cases where invalid name, or multiple players with same name
player_list = players.find_players_by_full_name(player_name)
if len(player_list) > 0:
    stats = playergamelog.PlayerGameLog(player_id=player_list[0]['id']).get_data_frames()[0]
    print(stats.loc[0:len(projections)-1, ['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']])
    player_stats = stats.loc[0:len(projections)-1, stat_type].to_numpy()
    print(player_stats)

#Calculate the probability for hitting the over
probability = get_over_probability(player_stats, projections)
print('Probability of hitting the over: ', probability)