import pickle

# Given dictionary
team_data = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

# Pickle the dictionary and save it to a file
with open('team_data.pkl', 'wb') as file:
    pickle.dump(team_data, file)

print("Dictionary pickled and saved to 'team_data.pkl'")
