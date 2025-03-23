import pandas as pd
from nba_api.stats.endpoints import playergamelog, commonteamroster
from nba_api.stats.static import teams
from pymongo import MongoClient
import time 

# User input
selected_season_id = "2024-25"  

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["nba_database"]

# Get all NBA teams
nba_teams = teams.get_teams()

for team in nba_teams:
    team_id = team['id']
    team_name = team['full_name']

    # create new db collection for team 
    collection_name = f"{team_name}_db"
    team_collection = db[collection_name]
    print(f"Created {collection_name}")

    print(f"Fetching data for {team_name}...")

    # Get the team roster
    try:
        roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=selected_season_id)
        roster_df = roster.get_data_frames()[0]
    except Exception as e:
        print(f"Skipping {team_name} due to error: {e}")
        continue

    for player in roster_df.itertuples(index=False):
        player_id = player.PLAYER_ID
        player_name = player.PLAYER

        # Get player's game logs
        try:
            gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=selected_season_id)
            gamelog_df = gamelog.get_data_frames()[0]

            # Store raw player stats in MongoDB
            team_collection.insert_one({
                "player_id": player_id,
                "player_name": player_name,
                "team_id": team_id,
                "team_name": team_name,
                "season": selected_season_id,
                "game_logs": gamelog_df.to_dict(orient="records")
            })

            print(f"Stored data for {player_name} ({team_name})")

        except Exception as e:
            print(f"Skipping {player_name} due to error: {e}")

        # to avoid getting blocked by the nba api
        time.sleep(0.2)

print("All NBA data saved to MongoDB")
