import config

db = config.db
averages_db = config.averages_db

all_stats_min = {}
all_stats_max = {}

# Iterate through all collections
for collection_name in averages_db.list_collection_names():
    collection = db[collection_name]
    
    # Fetch all documents from the collection
    for document in collection.find():

        stats_dict = document.get('avg_stats', {})
        
        # Update min and max for each stat
        for stat_name, stat_value in stats_dict.items():
            
            # Initialize if this is the first time seeing this stat
            if stat_name not in all_stats_min:
                all_stats_min[stat_name] = stat_value
                all_stats_max[stat_name] = stat_value
            else:
                # Update min and max
                all_stats_min[stat_name] = min(all_stats_min[stat_name], stat_value)
                all_stats_max[stat_name] = max(all_stats_max[stat_name], stat_value)

del all_stats_min["Player_ID"]
del all_stats_max["Player_ID"]

print("Minimum values for each stat:")
for stat, value in all_stats_min.items():
    print(f"{stat}: {value}")

print("\nMaximum values for each stat:")
for stat, value in all_stats_max.items():
    print(f"{stat}: {value}")