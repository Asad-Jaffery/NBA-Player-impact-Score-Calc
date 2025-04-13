import time
from src.scoring.impact_scoring.impact_score_formula import getPlayerImpactScore
import globals


client = globals.client
averages_db = globals.averages_db


scores = client["scores"]
impact_scores = scores["impact_scores"]

# get impact score for every player 
for collection_name in averages_db.list_collection_names():

    print(f"Calculating impact scores for {collection_name}...")

    collection = averages_db[collection_name]

    for player in collection.find():
        score = getPlayerImpactScore(player)
        player["impact_score"] = score

        impact_scores.insert_one(player)
        print(f"Stored impact score for {player['player_name']}")
        time.sleep(0.3)