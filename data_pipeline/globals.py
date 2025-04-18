from pymongo import MongoClient
from nba_api.stats.static import teams
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()  

# setup mongo
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["nba_database"]
averages_db = client["nba_averages"]

selected_season_id = "2024-25"

STAT_WEIGHTS = {
    'MIN': 0.05,
    'FG_PCT': 0.15,
    'REB': 0.10,
    'AST': 0.15,
    'PTS': 0.20,
    'STL': 0.05,
    'BLK': 0.05,
    'TOV': -0.05,
    'PLUS_MINUS': 0.25
}

stats_to_count = ['Player_ID','MIN','FG_PCT','REB','AST','PTS','STL','BLK','TOV','PLUS_MINUS']
positive_stats = ['MIN','FG_PCT','REB','AST','PTS','STL','BLK']

nba_teams = teams.get_teams()



