import array
import datetime
from nba_api.stats.endpoints import playergamelog, playergamelogs
from nba_api.stats.static import players
import pymongo
import numpy as np
import scipy.stats as st
import time

# player_name = "Spencer Dinwiddie"
# stat_type = "PTS" #PTS, AST, or REB
# max_games = 5

#Function for calculating probability
def get_over_probability(player_stats: np.ndarray, projections: np.ndarray):
    differences = player_stats - projections
    print(differences)
    z_score = (0 - np.mean(differences)) / np.std(differences)
    return st.norm.cdf(z_score)

def get_over_probability2(differences: np.ndarray):
    z_score = (np.mean(differences)) / np.std(differences)
    return 1- st.norm.cdf(z_score)



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

# # Get all players names
# people = []
# collection = db.players
# for doc in collection.find():
#     people.append(doc['name'])
# print(people)

# I think there are too many people and the api kicks me out so splitting them into a few groups
firstperson = ['Jayson Tatum']
people1 = ['Tyrese Haliburton', 'Jaylen Brown', 'Buddy Hield', 'Marcus Smart', 'Bennedict Mathurin', 'Myles Turner', 'Al Horford', 'Aaron Nesmith', 'Robert Williams III', 'Bojan Bogdanovic', 'Jaden Ivey', 'Cole Anthony', 'Franz Wagner', 'Paolo Banchero', 'Killian Hayes', 'Aaron Wiggins', 'Jordan Goodwin', 'Bryce McGowens', 'JT Thor', 'Svi Mykhailiuk']
people2 = ['Isaiah Stewart', 'Gary Harris', 'Jalen Duren', 'Wendell Carter Jr.', 'Markelle Fultz', 'Donovan Mitchell', 'Nikola Jokic', 'Darius Garland', 'Jamal Murray', 'Michael Porter Jr.', 'Caris LeVert', 'Evan Mobley', 'Kentavious Caldwell-Pope', 'Isaac Okoro', 'Jarrett Allen', 'Ja Morant']
people3 = ['Joel Embiid', 'Jaren Jackson Jr.', 'James Harden', 'Desmond Bane', 'Tobias Harris', 'Dillon Brooks', 'Tyrese Maxey', 'Santi Aldama', "De'Anthony Melton", 'Brandon Ingram', 'CJ McCollum', 'Pascal Siakam', 'Fred VanVleet', 'Jonas Valanciunas', 'Scottie Barnes', 'Trey Murphy III', 'Herbert Jones', 'Josh Green', 'Keldon Johnson', 'Kyrie Irving', 'Luka Doncic']
people4 = ['Zach Collins', 'Tim Hardaway Jr.', 'Malaki Branham', 'Jalen Williams', 'Lauri Markkanen', 'Josh Giddey', 'Jordan Clarkson', 'Shai Gilgeous-Alexander', 'Kelly Olynyk', 'Luguentz Dort', 'Walker Kessler', 'Isaiah Joe', 'Kenrich Williams', 'Talen Horton-Tucker', 'Draymond Green', 'LeBron James', 'Jordan Poole', 'Anthony Davis', 'Kevon Looney', 'Klay Thompson', "D'Angelo Russell", 'Malik Beasley', 'Jonathan Kuminga', 'Rui Hachimura', 'Donte DiVincenzo']
people5 = [ 'Dennis Schroder', 'Ty Jerome', 'Austin Reaves', 'Jarred Vanderbilt', "De'Aaron Fox", 'Damian Lillard', 'Domantas Sabonis', 'Harrison Barnes', 'Jerami Grant', 'Keegan Murray', 'Kevin Huerter', 'Cam Reddish', 'Drew Eubanks', 'Malik Monk', 'Zach LaVine', 'Spencer Dinwiddie', 'DeMar DeRozan', 'Mikal Bridges', 'Nikola Vucevic', 'Brook Lopez', 'Jalen Green', 'Aaron Gordon', 'Matisse Thybulle', 'Tyler Herro', 'Caleb Martin', 'John Collins', 'Saddiq Bey', 'Victor Oladipo', 'Onyeka Okongwu', 'Max Strus', 'Bogdan Bogdanovic', 'Kristaps Porzingis', 'James Wiseman']
people6 = ['Marvin Bagley III', 'Delon Wright', 'Isaiah Livers', 'Kelly Oubre Jr.', 'Kevin Porter Jr.', 'Stephen Curry', 'Reggie Bullock', 'Tyus Jones', 'Xavier Tillman', 'Kevin Love', 'Kevin Durant', 'Khris Middleton', 'Grayson Allen', 'Ivica Zubac', 'Terance Mann', 'P.J. Tucker', 'Monte Morris', 'Corey Kispert', 'Deni Avdija', 'Jusuf Nurkic', 'Devin Vassell', 'Troy Brown Jr.', 'Trey Lyles', 'Nick Richards', 'Rodney McGruder', 'Eugene Omoruyi', 'Lamar Stevens', 'Luke Kennard', 'Patrick Williams', 'Tre Jones', 'Keita Bates-Diop', 'Bruce Brown', 'Anfernee Simons', 'Josh Richardson', 'Andrew Nembhard', 'Dennis Smith Jr.', 'Ochai Agbaji']
people7 = ['Sandro Mamukelashvili', 'Jaylin Williams', 'Bobby Portis', 'Joe Ingles', 'Bismack Biyombo', 'Ricky Rubio', "Royce O\'Neale", 'Pat Connaughton', 'Trendon Watford', 'Joe Harris', 'Jeff Green', 'Nicolas Batum', 'Shaedon Sharpe', 'Jordan Nwora', 'T.J. McConnell', 'Kris Dunn', 'Doug McDermott', 'Simone Fontecchio', 'Nassir Little', 'Karl-Anthony Towns', 'Larry Nance Jr.', 'Isaiah Hartenstein', 'Cameron Payne', 'Coby White', 'Skylar Mays']
#'Johnny Davis', 


# player_list = players.find_players_by_full_name("Jayson Tatum")
# print(player_list)
# stats = playergamelog.PlayerGameLog(player_id=player_list[0]['id']).get_data_frames()[0]

# Check points table for a player's stats

def run_points(people):
    points= []
    collection = db.points
    for player in people:
        projections = []
        query = {"data": {"name": player}}
        for doc in collection.find(query).sort('date', 1):
            # print(doc)
            projections.append([doc['date'], doc['line'], player])
        print(projections)
        player_list = players.find_players_by_full_name(player)
        if len(player_list) > 0 and len(projections) > 0:
            stats = playergamelog.PlayerGameLog(player_id=player_list[0]['id']).get_data_frames()[0]
            
            player_stats = stats.loc[30:0:-1, ["GAME_DATE", "PTS", "AST", "REB"]].to_numpy()
            print(player_stats)
            #convert dates to date type object
            for game in player_stats:
                game[0] = datetime.datetime.strptime(game[0], '%b %d, %Y')


            gameIndex = 0
            for projection in projections:
                date = projection[0].strftime("%b %d")
                print(date)

                if (date == "2 24" or date == "Feb 24"):
                    continue

                #Find the right date
                while player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
                    if (gameIndex == len(player_stats)-1) or (projection[0] > player_stats[gameIndex][0] and projection[0] < player_stats[gameIndex+1][0]):
                        break
                    gameIndex = gameIndex+1
                if player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
                    continue                            
                
                if len(points) == 0 or len(points) == 1:
                    points.append({
                            "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][1])-float(projection[1])},
                            "date":projection[0],
                            "probability": 0.5
                        })
                else:
                    differences = []
                    if len(points) <= 4:
                        for point in points:
                            differences.append(point["data"]["overUnder"])
                    else:
                        for point in points[-5:]:
                            differences.append(point["data"]['overUnder'])
                    # print(differences)
                    probability = get_over_probability2(differences)
                    # print(projection)
                    # print(player_stats)
                    points.append({
                            "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][1])-float(projection[1])},
                            "date":projection[0],
                            "probability": probability
                        })
        time.sleep(0.5)
    print(points)
    return points

def run_assists(people):
    assists= []
    collection = db.assists
    for player in people:
        projections = []
        query = {"data": {"name": player}}
        for doc in collection.find(query).sort('date', 1):
            # print(doc)
            projections.append([doc['date'], doc['line'], player])
        if len(projections) == 0:
            continue
        print(projections)
        player_list = players.find_players_by_full_name(player)
        if len(player_list) > 0 and len(projections) > 0:
            stats = playergamelog.PlayerGameLog(player_id=player_list[0]['id']).get_data_frames()[0]
            
            player_stats = stats.loc[30:0:-1, ["GAME_DATE", "PTS", "AST", "REB"]].to_numpy()
            print(player_stats)
            #convert dates to date type object
            for game in player_stats:
                game[0] = datetime.datetime.strptime(game[0], '%b %d, %Y')


            gameIndex = 0
            for projection in projections:
                date = projection[0].strftime("%b %d")
                print(date)
                # date February 24th accidentally has 2 values, so ignore it
                if (date == "2 24" or date == "Feb 24" ):
                    continue

                #Find the right date
                while player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
                    if (gameIndex == len(player_stats)-1) or (projection[0] > player_stats[gameIndex][0] and projection[0] < player_stats[gameIndex+1][0]):
                        break
                    gameIndex = gameIndex+1
                if player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
                    continue                            
                
                if len(assists) == 0 or len(assists) == 1:
                    assists.append({
                            "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][2])-float(projection[1])},
                            "date":projection[0],
                            "probability": 0.5
                        })
                else:
                    differences = []
                    if len(assists) <= 4:
                        for assist in assists:
                            differences.append(assist["data"]["overUnder"])
                    else:
                        for assist in assists[-5:]:
                            differences.append(assist["data"]['overUnder'])
                    # print(differences)
                    probability = get_over_probability2(differences)
                    # print(projection)
                    # print(player_stats)
                    assists.append({
                            "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][2])-float(projection[1])},
                            "date":projection[0],
                            "probability": probability
                        })
        time.sleep(0.5)
    print(assists)
    return assists

def run_rebounds(people):
    rebounds= []
    collection = db.rebounds
    for player in people:
        projections = []
        query = {"data": {"name": player}}
        for doc in collection.find(query).sort('date', 1):
            # print(doc)
            projections.append([doc['date'], doc['line'], player])
        if len(projections) == 0:
            continue
        print(projections)
        player_list = players.find_players_by_full_name(player)
        if len(player_list) > 0 and len(projections) > 0:
            stats = playergamelog.PlayerGameLog(player_id=player_list[0]['id']).get_data_frames()[0]
            
            player_stats = stats.loc[30:0:-1, ["GAME_DATE", "PTS", "AST", "REB"]].to_numpy()
            print(player_stats)
            #convert dates to date type object
            for game in player_stats:
                game[0] = datetime.datetime.strptime(game[0], '%b %d, %Y')


            gameIndex = 0
            for projection in projections:
                date = projection[0].strftime("%b %d")
                print(date)
                # date February 24th accidentally has 2 values, so ignore it
                if (date == "2 24" or date == "Feb 24"):
                    continue

                #Find the right date
                while player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
                    if (gameIndex == len(player_stats)-1) or (projection[0] > player_stats[gameIndex][0] and projection[0] < player_stats[gameIndex+1][0]):
                        break
                    gameIndex = gameIndex+1
                if player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
                    continue                            
                
                if len(rebounds) == 0 or len(rebounds) == 1:
                    rebounds.append({
                            "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][3])-float(projection[1])},
                            "date":projection[0],
                            "probability": 0.5
                        })
                else:
                    differences = []
                    if len(rebounds) <= 4:
                        for rebound in rebounds:
                            differences.append(rebound["data"]["overUnder"])
                    else:
                        for rebound in rebounds[-5:]:
                            differences.append(rebound["data"]['overUnder'])
                    # print(differences)
                    probability = get_over_probability2(differences)
                    # print(projection)
                    # print(player_stats)
                    rebounds.append({
                            "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][3])-float(projection[1])},
                            "date":projection[0],
                            "probability": probability
                        })
        time.sleep(0.5)
    print(rebounds)
    return rebounds


calculations = run_assists(people7)

try:
    db = client.calculations
except Exception:
    print("oops something went wrong in the connection")


collection = db.assists
for calculation in calculations:
    if calculation["date"].strftime("%b") != "Apr":
        continue
    if int(calculation["date"].strftime("%d"))>9:
        continue
    collection.insert_one(calculation)
    print(calculation)
# collection.insert_many(calculations)
print("Successful")
    

client.close()


# player_list = players.find_players_by_full_name('Jayson Tatum')
# if len(player_list) > 0:
#     stats = playergamelog.PlayerGameLog(player_id=player_list[0]['id']).get_data_frames()[0]
#     # print(stats)
    
#     player_stats = stats.loc[20:0:-1, ["GAME_DATE", "PTS", "AST", "REB"]].to_numpy()
#     # print(player_stats)
#     for game in player_stats:
#         game[0] = datetime.datetime.strptime(game[0], '%b %d, %Y')
#     # print(player_stats)

#     projections = [[datetime.datetime(2023, 2, 23, 0, 0), '29.5', 'Jayson Tatum'], [datetime.datetime(2023, 2, 25, 0, 0), '29.5', 'Jayson Tatum'], [datetime.datetime(2023, 2, 27, 0, 0), '31.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 1, 20, 9, 5, 684000), '27.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 3, 20, 8, 40, 603000), '28.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 5, 20, 8, 54, 685000), '28.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 8, 20, 8, 40, 23000), '29.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 11, 20, 8, 42, 342000), '29.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 13, 20, 8, 39, 751000), '29.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 15, 20, 8, 50, 9000), '29', 'Jayson Tatum'], [datetime.datetime(2023, 3, 17, 20, 8, 41, 180000), '28.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 18, 20, 8, 40, 991000), '28.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 21, 20, 8, 39, 435000), '29.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 24, 20, 8, 47, 135000), '30.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 28, 20, 8, 40, 460000), '28.5', 'Jayson Tatum'], [datetime.datetime(2023, 3, 30, 20, 10, 28, 796000), '28.5', 'Jayson Tatum'], [datetime.datetime(2023, 4, 4, 20, 8, 41, 739000), '30.5', 'Jayson Tatum']]
#     points = []
#     gameIndex = 0
#     for projection in projections:
#         # print(type(projection[0]))
#         date = projection[0].strftime("%b %d")
#         print(date)
#         if (date == "2 24"):
#             continue
#         # print(type(player_stats[gameIndex][0]))
#         while player_stats[gameIndex][0].strftime("%b %d") != projection[0].strftime("%b %d"):
#             gameIndex = gameIndex+1
#         # print(gameIndex)
        
#         if len(points) == 0 or len(points) == 1:
#             points.append({
#                     "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][1])-float(projection[1])},
#                     "date":projection[0].strftime("%b %d"),
#                     "probability": 0.5
#                 })
#         else:
#             differences = []
#             if len(points) <= 4:
#                 for point in points:
#                     differences.append(point["data"]["overUnder"])
#             else:
#                 for point in points[-5:]:
#                     differences.append(point["data"]['overUnder'])
#             print(differences)
#             probability = get_over_probability2(differences)
#             # print(projection)
#             # print(player_stats)
#             points.append({
#                     "data": {"name": projection[2], "overUnder": float(player_stats[gameIndex][1])-float(projection[1])},
#                     "date":projection[0].strftime("%b %d"),
#                     "probability": probability
#                 })
#     print(points)




    # player_stats = stats.loc[0:len(projections)-1, stat_type].to_numpy()
    # print(player_stats)

# date
# over-under-probability
# data(name, actual over under?)



# #Collect prizepicks projections
# if stat_type == "PTS":
#     collection = db.points
# elif stat_type == "AST":
#     collection = db.assists
# elif stat_type == "REB":
#     collection = db.rebounds
# else:
#     print("Invalid stat type entered. Please enter valid stat type")
#     client.close()
#     exit()



# if len(projections) == 0:
#     print("Sorry, no prizepicks projects for this player yet. Try a different player")
#     exit()
# projections = np.array(projections).astype(float)
# print(projections)

# #Collect player stats
# #TODO Solve edge cases where invalid name, or multiple players with same name


# #Calculate the probability for hitting the over
# probability = get_over_probability(player_stats, projections)
# print('Probability of hitting the over: ', probability)