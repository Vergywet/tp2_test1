import pandas as pd
football= pd.read_csv("C:\\Users\\User\\Downloads\\dataset - 2020-09-24.csv")
print(football.head(7))

first_5_players = football.head(5)
nationality_column = first_5_players['Nationality']
club_column = first_5_players['Club']

print("Nationality: ", nationality_column)
print("Club: ", club_column)

tenth_player = football.loc[9]
print(tenth_player)

players_100_110 = football.loc[100:110]
goals_column = players_100_110['Goals']
appearances_column = players_100_110['Appearances']

print("Goals: ", goals_column)
print("Appearances: ", appearances_column)

football['Goals per Appearance'] = football['Goals'] / football['Appearances']
first_5_rows_updated = football.head(5)
print(first_5_rows_updated)

arsenal_players = football[football['Club'] == 'Arsenal']
print(arsenal_players)

high_goal_scorers = football[football['Goals'] > 5]
print(high_goal_scorers)