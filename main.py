import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import requests



#URL manipulation
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
response_2024_2025 = requests.get(url=season_2024_2025_url).json()

print(response_2017_2018['resultSet']["rowSet"])



