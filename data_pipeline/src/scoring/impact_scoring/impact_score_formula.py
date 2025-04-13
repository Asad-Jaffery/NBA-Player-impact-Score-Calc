from src.transform import mongodb_min_max_finder
import globals

all_stats_min, all_stats_max = mongodb_min_max_finder.all_stats_min, mongodb_min_max_finder.all_stats_max

# import global variables
db = globals.db
averages_db = globals.averages_db
stat_weight = globals.STAT_WEIGHTS
positive_stats = globals.positive_stats

def getPlayerImpactScore(player): 
    """Calculates the Impact score of a player based on their average stats"""
    if not player["avg_stats"]:
        return 0
    
    # normalize the player stats (on a 0 - 100 scale)
    normalized_stats = {} 

    for stat in positive_stats:
        if player["avg_stats"][stat] == 0:
            normalized_stats[stat] = 0
        else:
            normalized_stats[stat] = 100 * (player["avg_stats"][stat] - all_stats_min[stat]) / (all_stats_max[stat] - all_stats_min[stat])

    normalized_stats['TOV'] = 100 * (all_stats_max['TOV'] - player["avg_stats"]['TOV']) / (all_stats_max['TOV'] - all_stats_min['TOV'])

    if player["avg_stats"]['PLUS_MINUS'] < 0:
        normalized_stats['PLUS_MINUS'] = 50 - ((player["avg_stats"]['PLUS_MINUS'] - all_stats_min['PLUS_MINUS']) / (all_stats_max['PLUS_MINUS'] - all_stats_min['PLUS_MINUS'] * 50))
    else:
        normalized_stats['PLUS_MINUS'] = 50 + ((player["avg_stats"]['PLUS_MINUS'] - all_stats_min['PLUS_MINUS']) / (all_stats_max['PLUS_MINUS'] - all_stats_min['PLUS_MINUS'] * 50))

    score_stats = {}

    for stat in stat_weight:
        score_stats[stat] = normalized_stats[stat] * stat_weight[stat]
    
    return sum(score_stats.values())




