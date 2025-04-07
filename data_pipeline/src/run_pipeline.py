import subprocess
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

def run_script(module):
    """Helper function to run a module using `-m` to handle imports properly."""
    try:
        subprocess.run(["python", "-m", module], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {module}: {e}")
        exit(1)  # Exit if any script fails

if __name__ == "__main__":
    print("Deleting Old Data First...")
    client.drop_database("nba_database")
    client.drop_database("nba_averages")
    client.drop_database("scores")

    print("Starting NBA Impact Score Pipeline...")

    print("\n[STEP 1] Extracting raw NBA stats...")
    run_script("src.extract.fetch_nba_data")
    
    print("\n[STEP 2] Fetching averages...")
    run_script("src.transform.get_average_stats")

    print("\n[STEP 3] Scoring and storing impact scores into Mongo...")
    run_script("src.scoring.impact_scoring.load_impact_scores")
