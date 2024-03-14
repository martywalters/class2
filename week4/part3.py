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
#with open('team_data.pkl', 'wb') as file:
#    pickle.dump(team_data, file)

#print("Dictionary pickled and saved to 'team_data.pkl'")

import pickle

def pickle_dictionary(data, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(f"Dictionary pickled and saved to {filename}")
    except Exception as e:
        print(f"Error pickling dictionary: {e}")

def unpickle_dictionary(filename):
    try:
        with open(filename, 'rb') as file:
            loaded_data = pickle.load(file)
            return loaded_data
    except Exception as e:
        print(f"Error unpickling dictionary: {e}")
        return None

pickle_dictionary(team_data , 'teams.pickle')

loaded_teams = unpickle_dictionary('teams.pickle')
if loaded_teams:
    print("Unpickled dictionary:")
    print(loaded_teams)




