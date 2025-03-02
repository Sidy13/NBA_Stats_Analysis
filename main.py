import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import requests
import time



#URL manipulation
'''
season_2014_2015_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2014-15&SeasonType=Regular%20Season&StatCategory=PTS"
season_2015_2016_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2015-16&SeasonType=Regular%20Season&StatCategory=PTS"
season_2016_2017_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2016-17&SeasonType=Regular%20Season&StatCategory=PTS"
season_2017_2018_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2017-18&SeasonType=Regular%20Season&StatCategory=PTS"
season_2018_2019_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2018-19&SeasonType=Regular%20Season&StatCategory=PTS"
season_2019_2020_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2019-25&SeasonType=Regular%20Season&StatCategory=PTS"
season_2020_2021_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2020-25&SeasonType=Regular%20Season&StatCategory=PTS"
season_2021_2022_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2021-25&SeasonType=Regular%20Season&StatCategory=PTS"
season_2022_2023_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2022-25&SeasonType=Regular%20Season&StatCategory=PTS"
season_2023_2024_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-25&SeasonType=Regular%20Season&StatCategory=PTS"
season_2024_2025_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2024-25&SeasonType=Regular%20Season&StatCategory=PTS"


response_2014_2015 = requests.get(url=season_2014_2015_url).json()
response_2015_2016 = requests.get(url=season_2015_2016_url).json()
response_2016_2017 = requests.get(url=season_2016_2017_url).json()
response_2017_2018 = requests.get(url=season_2017_2018_url).json()
response_2018_2019 = requests.get(url=season_2018_2019_url).json()
response_2019_2020 = requests.get(url=season_2019_2020_url).json()
response_2020_2021 = requests.get(url=season_2020_2021_url).json()
response_2021_2022 = requests.get(url=season_2022_2023_url).json()
response_2022_2023 = requests.get(url=season_2022_2023_url).json()
response_2023_2024 = requests.get(url=season_2023_2024_url).json()
response_2024_2025 = requests.get(url=season_2024_2025_url).json()'''

season_2014_2015_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2014-15&SeasonType=Regular%20Season&StatCategory=PTS"
response_2014_2015 = requests.get(url=season_2014_2015_url).json()
table_headers = response_2014_2015["resultSet"]["headers"]

'''print(response_2017_2018["resultSet"])
print(response_2017_2018['resultSet']["rowSet"][0])
print(pd.DataFrame(response_2017_2018["resultSet"]["rowSet"], columns=table_headers))'''

'''headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "if-modified-since": "Sun, 02 Mar 2025 16:56:59 GMT",
    "if-none-match": '"6bfda48f79dbbf167a49bbb63220a0a1"',
    "origin": "https://www.nba.com",
    "priority": "u=1, i",
    "referer": "https://www.nba.com/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
begin_loop = time.time()
df_columns = ["Season"]+ table_headers
df = pd.DataFrame(columns = df_columns)
seasons = ["2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
for season in seasons:
    season_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season="+season+"&SeasonType=Regular%20Season&StatCategory=PTS"
    response = requests.get(url=season_url).json()
    df1 = pd.DataFrame(response["resultSet"]["rowSet"], columns=table_headers)
    df2 = pd.DataFrame({"Season": [season for i in range(len(df1))]})
    df3 = pd.concat([df2, df1], axis=1)
    df = pd.concat([df, df3], axis=0)

print("Process completed, total time:", time.time()-begin_loop)
df_excel = df.to_excel("league_Leaders_Per_Points.xlsx", index=False)'''

dataset = pd.read_excel("League_Leaders_Per_Points.xlsx")

'''rank_1 = dataset[dataset["RANK"]==1]
print(rank_1)

x_values = rank_1["PTS"].values
y_values = rank_1["EFF"].values
player_names = rank_1["PLAYER"].values
seasons = rank_1["Season"].values

plt.scatter(x_values, y_values)

for i in range(len(x_values)):
    plt.text(x_values[i], y_values[i]-0.5, f"{player_names[i]} ({seasons[i]})", ha='center', va='bottom')
plt.title("PTS by EFF")
plt.xlabel("PTS")
plt.ylabel("EFF")
plt.show()'''




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.float_format', '{:.2f}'.format)

print("1. Observe a player stats \n2. Compare two players by name \n3. Compare two players by ranking")
choice = 0
while choice not in [1, 2, 3]:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")


if choice == 1:
    name = input("Enter the name of the player whose stats you want to see: ")
    name_search = dataset[dataset["PLAYER"] == name]
    if name_search.empty:
        print("Player not found")
    else:
        print(name_search.to_string(index=False))
elif choice == 2:
        players = []

        for i in range(2):
            name = input(f"Enter the name of player {i + 1}: ")
            name_search = dataset[dataset["PLAYER"] == name]
            if name_search.empty:
                print(f"Player '{name}' not found.")
            else:
                players.append(name_search)
                print(f"Player '{name}' added successfully.")

        if players:
            selected_players = pd.concat(players, ignore_index=True)
        else:
            print("No players selected.")
            selected_players = None

        if selected_players is not None:
            unique_players = selected_players["PLAYER"].unique()
            colors = plt.cm.get_cmap("tab10", len(unique_players))

            for i, player in enumerate(unique_players):
                player_data = selected_players[selected_players["PLAYER"] == player]
                x_values = player_data["PTS"].values
                y_values = player_data["EFF"].values
                color = colors(i)
                plt.scatter(x_values, y_values, label=player, color=color)

                seasons = player_data["Season"].values
                for j in range(len(x_values)):
                    plt.text(x_values[j], y_values[j] - 0.5, f"{player} ({seasons[j]})",
                             ha='center', va='bottom', fontsize=9, color=color)

            plt.title("Points by efficiency")
            plt.xlabel("PTS")
            plt.ylabel("EFF")
            plt.legend()
            plt.show()
elif choice == 3:
        players = []

        for i in range(2):
            name = input(f"Enter the name of player {i + 1}: ")
            name_search = dataset[dataset["PLAYER"] == name]
            if name_search.empty:
                print(f"Player '{name}' not found.")
            else:
                players.append(name_search)
                print(f"Player '{name}' added successfully.")

        if players:
            selected_players = pd.concat(players, ignore_index=True)
        else:
            print("No players selected.")
            selected_players = None

        if selected_players is not None:
            unique_players = selected_players["PLAYER"].unique()
            colors = plt.cm.get_cmap("tab10", len(unique_players))


            for i, player in enumerate(unique_players):
                player_data = selected_players[selected_players["PLAYER"] == player]
                x_values = player_data["PTS"].values
                y_values = player_data["RANK"].values
                color = colors(i)
                plt.scatter(x_values, y_values, label=player, color=color)

                seasons = player_data["Season"].values
                for j in range(len(x_values)):
                    plt.text(x_values[j], y_values[j] - 0.5, f"{player} ({seasons[j]})",
                             ha='center', va='bottom', fontsize=9, color=color)

            plt.title("Points by ranking")
            plt.xlabel("PTS")
            plt.ylabel("RANK")
            plt.legend()
            plt.show()