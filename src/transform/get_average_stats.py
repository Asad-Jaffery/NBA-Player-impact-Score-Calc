from pymongo import MongoClient
from nba_api.stats.static import teams


# connect to mongo
client = MongoClient("mongodb://localhost:27017/")
db = client["nba_database"]

nba_teams = teams.get_teams()

for team in nba_teams:
    team_name = team['full_name']

    # create new db for each team
    collection_name = f"{team_name}_averages"
    average_collection = db[collection_name]
    print(f"Created {collection_name}")

    curr_team_collection = db[f"{team_name}_db"]

    for player in curr_team_collection.find({}):
        print(player["player_name"])


    # each db has an object for each player 
    # each player's object contains their averate stats
