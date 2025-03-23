import pandas as pd
import src.transform.config as config
import time

db = config.db
averages_db = config.averages_db

nba_teams = config.nba_teams 

for team in nba_teams:
    team_name = team['full_name']

    # create new db for each team
    collection_name = f"{team_name}_averages"
    average_collection = averages_db[collection_name]
    print(f"Created {collection_name}")

    # get the current team's db
    curr_team_collection = db[f"{team_name}_db"]

    # for each player in the current team's db, get the averages and add it 
    for player in curr_team_collection.find({}):
        print(f"filling {team_name}'s average collection...")

        all_game_logs = []
        all_game_logs.extend(player["game_logs"])
        all_game_log_df = pd.DataFrame(all_game_logs)
        if len(all_game_log_df) > 0 :
            all_game_log_df = all_game_log_df[config.stats_to_count]
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
        
        print(f"Stored averages for {player['player_name']} ({team_name})")
        time.sleep(0.2)
        

