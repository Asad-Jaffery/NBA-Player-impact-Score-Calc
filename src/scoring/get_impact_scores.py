import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from pymongo import MongoClient
from transform.calculate_impact_scores import getPlayerImpactScore

client = MongoClient("mongodb://localhost:27017/")

scores = client["scores"]
averages_db = client["nba_averages"]

impact_scores = scores["impact_scores"]

# get impact score for every player 
for collection_name in averages_db.list_collection_names():
    collection = averages_db[collection_name]

    for player in collection.find():
        score = getPlayerImpactScore(player)
        player["impact_score"] = score

        impact_scores.insert_one(player)


