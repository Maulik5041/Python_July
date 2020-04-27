# Merging 2 dictionaries

Father = {'Name': "Suresh", 'age': 56, "Marital Status": "Married"}
Uncle = {'Color': "Brown", 'Wife': "Ragini", "Employment": "Retired"}

Couple = dict(list(Father.items()) + list(Uncle.items()))

print(Couple)