# Merge 2 dictionaries

x = {'a' : 1, 'b' : 2}
y = {'c' : 3, 'd' : 4}

z = dict(list(x.items()) + list(y.items()))

print("After merging", dict(list(x.items())), "and", dict(list(y.items())), "we get,", z)
