"""
Evan Dong
Sep 28, 2026
Lab 7: API and data collection
"""
import pandas as pd

# ----------------------------
# 1. Example DataFrame
# ----------------------------

dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}

df = pd.DataFrame(dict_)

print(df.head())
print(df.mean())

# ----------------------------
# 2. Get NBA teams
# ----------------------------

from static import get_teams
nba_teams = get_teams()

print(f"First 2 teams: {nba_teams[:2]}")

df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

df_warriors = df_teams[df_teams["nickname"] == "Warriors"]
print(df_warriors)

id_warriors = df_warriors[["id"]].values[0]
print(id_warriors)

# ----------------------------
# 3. Working with external API
# ----------------------------
import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

file_name = "Golden_State.pkl"

print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
        print("Download Complete.")
else:
    print("Download failed.")

games = pd.read_pickle(file_name)
print("\nGames data from pickle file: ")
print(games.head())

warriors_vs_raptors = games[games["MATCHUP"].str.contains("TOR")]

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains("vs.")]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains("@")]

home_avg_plus = gsw_home_vs_raptors["PLUS_MINUS"].mean()
away_avg_plus = gsw_away_vs_raptors["PLUS_MINUS"].mean()
home_avg_pts = gsw_home_vs_raptors["PTS"].mean()
away_avg_pts = gsw_away_vs_raptors["PTS"].mean()

print(f"Warriors home average {home_avg_plus}")
print(f"Warriors away average {away_avg_plus}")

import matplotlib.pyplot as plt

metrics = ['PLUS_MINUS', 'PTS']
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x], home_values,
width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values,
width=bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title('Golden State Warriors vs. Raptors — Home vs Away Comparison')
plt.ylabel('Average Value')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)

input("Press Enter to close...")

# ----------------------------
# EXERCISE
# ----------------------------

url1 = "https://datahub.io/core/english-premier-league/r/season-2324.csv" 

file_name1 = "epl_matches.csv"
response1 = requests.get(url1)
if response1.status_code == 200:
    with open(file_name1, 'wb') as f:
        f.write(response1.content)
    print(f"Downloaded complete")
else:
    print("Download failed.")

matches = pd.read_csv(file_name1)
print(matches.head())

burnley_vs_man_city = matches[matches["HomeTeam"].str.contains("Burnley")]
burnley_away_vs_man_city = matches[matches["AwayTeam"].str.contains("Burnley")]
man_city_vs_burnley = matches[matches["AwayTeam"].str.contains("Man City")]
man_city_away_vs_burnley = matches[matches["HomeTeam"].str.contains("Man City")]

home_avg_burnley_plus = burnley_vs_man_city["FTHG"].mean()
away_avg_burnley_points = burnley_away_vs_man_city["FTAG"].mean()
home_avg_man_city_plus = man_city_vs_burnley["FTHG"].mean()
away_avg_man_city_points = man_city_away_vs_burnley["FTAG"].mean()
print(f"Burnley home average {home_avg_burnley_plus}")
print(f"Burnley away average {away_avg_burnley_points}")
print(f"Man City home average {home_avg_man_city_plus}")
print(f"Man City away average {away_avg_man_city_points}")

import matplotlib.pyplot as plt

metrics = ['FTAG', 'FTHG']
home_values = [home_avg_burnley_plus, home_avg_man_city_plus]
away_values = [away_avg_burnley_points, away_avg_man_city_points]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x], home_values,width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values,width=bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title('Burnley vs Man City — Home vs Away Comparison')
plt.ylabel('Average Value')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)

input("Press Enter to close...")