from itertools import chain

fruits = {'apple': 10, 'banana': 20}
veggies = {'carrot': 5, 'potato': 45}

print(chain(fruits.items(), veggies.items()))
# for item in chain(fruits.items(), veggies.items()):
# 	print(item)


# There is another way to chain multiple dictionaries
# by using collections.ChainMap method, but it creates a separate object.
# The above method does the same chaining without the extra
# effort of creating an object

from collections import ChainMap

print(type(ChainMap(fruits, veggies)))


# One more way to chain 2 dictionaries are by unpacking them

print(type({**fruits, **veggies}))


'''
In dictionary unpacking, if there is a key duplication
then the right-most value gets the precedence, whereas
in the case of ChainMap, left-most value gets precendence
in the case of key-duplication
'''