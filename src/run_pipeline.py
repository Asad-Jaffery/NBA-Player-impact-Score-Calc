import subprocess

def run_script(module_name):
    """Helper function to run a module using `-m` to handle imports properly."""
    try:
        subprocess.run(["python", "-m", module_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {module_name}: {e}")
        exit(1)  # Exit if any script fails

if __name__ == "__main__":
    print("Starting NBA Impact Score Pipeline...")

    print("\n[STEP 1] Extracting raw NBA stats...")
    run_script("src.extract.fetch_nba_data")

    print("\n[STEP 2] Fetching averages...")
    run_script("src.transform.get_average_stats")

    print("\n[STEP 3] Scoring and storing impact scores into Mongo...")
    run_script("src.scoring.impact_scoring.load_impact_scores")
