#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas.testing as tm


match_data = pd.read_csv("international_matches.csv")

comp = 11
season_id = 41


home_team = 'Australia'
away_team = 'American Samoa'
match_id = None
score = None


for match in match_data:
    home_team_value = (match['home_team'] == home_team)
    away_team_value = (match['away_team'] == away_team)

    if home_team_value and away_team_value:
        match_id = match['match_id']
        score = str(match['home_score']) + ' : ' + str(match['away_score'])


if match_id != None:
    print('{} vs {} has match id: {}'.format(home_team, away_team, match_id))
    print('Score: {}'.format(score))
else:
    print('No match found')


for match in match_data:
    home_team_value = match['home_team']
    away_team_value = match['away_team']

    if home_team_value == home_team or away_team_value == home_team:
        score = str(match['home_score']) + ' : ' + str(match['away_score'])
        print('{} vs {}, score: {}'.format(
            home_team_value, away_team_value, score))
