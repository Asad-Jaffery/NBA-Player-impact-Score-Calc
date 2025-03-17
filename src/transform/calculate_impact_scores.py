import pandas as pd
from pymongo import MongoClient
from transform.config import STAT_WEIGHTS


client = MongoClient("mongodb://localhost:27017/")
db = client["nba_database"]

impact_scores_collection = db["impact_scores"]


