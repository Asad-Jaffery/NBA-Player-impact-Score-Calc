import subprocess
import os

def run_script(script_path):
    """Helper function to run a Python script."""
    script_full_path = os.path.abspath(script_path)
    result = subprocess.run(
        ["python", "-u", script_full_path],  
        check=True  
    )

if __name__ == "__main__":
    print("Starting NBA Impact Score Pipeline...")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    print("\n[STEP 1] Extracting raw NBA stats...")
    run_script(os.path.join(base_dir, "extract/fetch_nba_data.py"))

    print("\n[STEP 2] Fetching averages...")
    run_script(os.path.join(base_dir, "transform/get_average_stats.py"))

    print("\n[STEP 3] Scoring and storing impact scores into Mongo...")
    run_script(os.path.join(base_dir, "scoring/get_impact_scores.py"))
