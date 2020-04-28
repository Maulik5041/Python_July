# Defining a dictionary

MLB_team = {
	'Colorado' : 'Rockies',
	'Boston' : 'Red Sox',
	'Minnesota' : 'Twins',
	'Milwaukee' : 'Brewers',
	'Seattle' : 'Mariners'
}

LaLiga_team = dict([
	('Madrid', 'Real Madrid'),
	('Barcelona', 'FC Barcelona')
	])

# Only if the key values are simple strings
# If the keys are integers then it will raise a Syntax Error

IPL_teams = dict(
	Delhi='Delhi Kings',
	Mumbai='Mumbai Indians',
	Chennai='Chennai Super Kings',
	Kolkata='Kolkata Knight Riders'
	)

# To delete a key value from the dictionary

del MLB_team['Boston']

print(MLB_team, '\n')

print(LaLiga_team, '\n')

print(IPL_teams, '\n')

# While creating a dictionary, even the built-in types can be used

d = {int: 1, float: 2, bool: 3}

print(d)

print(d[float])


# The keys can only be immutable
# Integer, float, string, boolean, tuple

# a = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}

# print(a)

# Mutable data types like lists and dictionaries are not allowed

# b = {[1, 1]: 1, {2: 'Hello'}: 3}

# print(b)

'''
The main reason of an immutable data type being a key value
is mainly because they are hashable. Python can take an object
and hash it to a simpler fixed-size value. The mutable objects like,
lists and dictionaries, are not hasable and hence cannot be the keys
'''

print(hash((1,1)))

print(hash(1), '\n')

print(hash('Python is the best language'))

# print(hash([1, 2, 3]))

print(hash((1, 1)))


# There are absolutely no restrictions on dictionary values in Python