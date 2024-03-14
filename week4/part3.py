import pickle
from pathlib import Path
# Given dictionary
team_data = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

import pickle

def pickle_it(data=team_data, filename='team_data.pkl'):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(f"Dictionary pickled and saved to {filename}")
    except Exception as e:
        print(f"Error pickling dictionary: {e}")

def unpickle_it(filename='team_data.pkl'):
    try:
        with open(filename, 'rb') as file:
            loaded_data = pickle.load(file)
            print("Unpickled dictionary:")
            #return loaded_data
            print(loaded_data)
    except Exception as e:
        print(f"Error unpickling dictionary: {e}")
        return None
def move_pickle():
    Path("team_data.pkl").rename("client/team_data.pkl")
    


#pickle_dictionary(team_data , 'team_data.pkl')

#input('continue after transfer')

#loaded_teams = unpickle_dictionary('team_data.pkl')
#if loaded_teams:
#    print("Unpickled dictionary:")
#    print(loaded_teams)




