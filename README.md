NBA Player Statistics Analysis

Overview

This Python project allows users to analyze NBA player statistics over multiple seasons. The program fetches data from the NBA stats API, processes it using Pandas, and visualizes player performance with Matplotlib.


Features

Fetch and store NBA player statistics for seasons ranging from 2014-15 to 2024-25.

Compare players based on their Efficiency (EFF) and Ranking (RANK).

Track the evolution of a player's performance over multiple seasons.

View individual player statistics for a selected season.

Interactive selection of players for comparison and analysis.


Requirements

To run this project, you need the following Python libraries:

pip install matplotlib pandas requests openpyxl


Usage

1. Run the script

Execute the Python script to start the program:

python script.py

2. Choose an action

After launching the program, you will be prompted to choose an action:

1: View a player's statistics.

2: Track a player's performance over seasons.

3: Compare two players based on Efficiency.

4: Compare two players based on Ranking.

3. Follow the prompts

If you choose to view a player's statistics, enter the player's name.

If you choose to track or compare players, provide the required input as prompted.

The program will generate and display visual charts where applicable.


Data Source

The data is retrieved from the NBA Stats API and stored in an Excel file (League_Leaders_Per_Points.xlsx) for efficient processing.


Example Outputs

Player performance evolution: Line chart displaying PTS, EFF, and RANK over seasons.

Player comparison: Scatter plot comparing two players based on PTS vs EFF or PTS vs RANK.


Notes

Ensure your internet connection is active when fetching data.

The dataset is stored locally after fetching; re-running the script will use the existing file unless modified.
