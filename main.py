import matplotlib.pyplot as plt
import pandas as pd
import requests
import time

def compare_players(column):
    players = []
    for i in range(2):
        name = input(f"Enter the name of player {i + 1}: ")
        name_search = dataset[dataset["PLAYER"] == name]
        if name_search.empty:
            print(f"Player '{name}' not found.")
        else:
            players.append(name_search)

    if players:
        selected_players = pd.concat(players, ignore_index=True)
        unique_players = selected_players["PLAYER"].unique()
        colors = plt.cm.get_cmap("tab10", len(unique_players))

        for i, player in enumerate(unique_players):
            player_data = selected_players[selected_players["PLAYER"] == player]
            x_values = player_data["PTS"].values
            y_values = player_data[column].values
            color = colors(i)
            plt.scatter(x_values, y_values, label=player, color=color)
            for j in range(len(x_values)):
                plt.text(x_values[j], y_values[j] - 0.5, f"{player} ({player_data['Season'].values[j]})",
                         ha='center', va='bottom', fontsize=9, color=color)

        plt.title(f"Points by {column}")
        plt.xlabel("PTS")
        plt.ylabel(column)
        plt.legend()
        plt.show()


def track_player_performance():
    name = input("Enter the name of the player you want to track: ")
    player_data = dataset[dataset["PLAYER"] == name]

    if player_data.empty:
        print("Player not found.")
        return

    player_data = player_data.sort_values(by="Season")

    plt.figure(figsize=(10, 6))
    plt.plot(player_data["Season"], player_data["PTS"], marker='o', linestyle='-', label="Points Per Game",
             color="blue")
    plt.plot(player_data["Season"], player_data["EFF"], marker='s', linestyle='--', label="Efficiency",
             color="red")
    plt.plot(player_data["Season"], player_data["RANK"], marker='^', linestyle='-.', label="Ranking", color="green")

    for i in range(len(player_data)):
        plt.text(player_data["Season"].values[i], player_data["PTS"].values[i] + 0.5, str(player_data["PTS"].values[i]),
                 ha='center', color="blue")
        plt.text(player_data["Season"].values[i], player_data["EFF"].values[i] + 0.5, str(player_data["EFF"].values[i]),
                 ha='center', color="red")
        plt.text(player_data["Season"].values[i], player_data["RANK"].values[i] + 0.5,
                 str(player_data["RANK"].values[i]), ha='center', color="green")

    plt.title(f"Evolution of {name} performance (Points, Efficiency, Ranking)")
    plt.xlabel("Season")
    plt.ylabel("Value")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


#URL manipulation


season_2014_2015_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2014-15&SeasonType=Regular%20Season&StatCategory=PTS"
response_2014_2015 = requests.get(url=season_2014_2015_url).json()
table_headers = response_2014_2015["resultSet"]["headers"]

'''print(response_2017_2018["resultSet"])
print(response_2017_2018['resultSet']["rowSet"][0])
print(pd.DataFrame(response_2017_2018["resultSet"]["rowSet"], columns=table_headers))'''


'''begin_loop = time.time()
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

print("1. Observe a player stats \n2. Observe the evolution of a player\n3. Compare two players by name \n4. Compare two players by ranking")
choice = 0
while choice not in [1, 2, 3,4]:
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
    track_player_performance()
elif choice == 3:
    compare_players("EFF")
elif choice == 4:
    compare_players("RANK")




