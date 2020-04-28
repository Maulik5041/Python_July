# Operators and built-in functions in Dictionary


MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

IPL_teams = dict(
	Delhi='Delhi Kings',
	Mumbai='Mumbai Indians',
	Chennai='Chennai Super Kings',
	Kolkata='Kolkata Knight Riders'
	)

print('Milwaukee' in MLB_team)

print('Toronto' in MLB_team)

print('Toronto' not in MLB_team)

# In case of multiple conditions, if the first 
# condition is not met, there would be short-circuit 
# evaluation and would not even check for the remaining
# conditions

print('Toronto' in MLB_team and MLB_team['Toronto'])


# Built-in Dictionary Methods

'''
d.clear() - Clears dictionary
d.get(<key>) - Returns the value of the key if exists
d.items() - Returns the list of tuples of key-value pairs
d.keys() - Returns a list of all keys
d.values() - Returns a list of all values and the duplicate
				values will be returned as many they occur

d.pop() - Removes the key if present
d.popitem() - Removes a random key-value pair

d.update(<obj>) - Merges a dictionary with another
'''

print(MLB_team.get('Colorado'), '\n')

print(MLB_team.items(), '\n', '\n')

print(MLB_team.popitem(),  '\n')

(MLB_team.update(IPL_teams))

print(MLB_team)