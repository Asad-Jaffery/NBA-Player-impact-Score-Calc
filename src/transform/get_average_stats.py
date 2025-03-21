from pymongo import MongoClient
from nba_api.stats.static import teams
import pandas as pd
from config import stats_to_count


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

    # get the current team's db
    curr_team_collection = db[f"{team_name}_db"]

    # for each player in the current team's db, get the averages and add it 
    for player in curr_team_collection.find({}):
        print(f"filling {average_collection}...")

        all_game_logs = []
        all_game_logs.extend(player["game_logs"])
        all_game_log_df = pd.DataFrame(all_game_logs)
        if len(all_game_log_df) > 0 :
            all_game_log_df = all_game_log_df[stats_to_count]
        else:
            all_game_log_df = pd.DataFrame()
        player_averages = pd.DataFrame(all_game_log_df).mean().to_dict()
        
        average_collection.insert_one({
            "player_id": player["player_id"],
            "player_name": player["player_name"],
            "team_id": player["team_id"],
            "team_name": player["team_name"],
            "avg_stats": player_averages
            })
