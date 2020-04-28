prices = {'apple': 0.25, 'orange': 0.50, 'kiwi': 0.75}

from itertools import cycle
num_items = 10

for item in cycle(prices.items()):
	if num_items == 0:
		break

	num_items -= 1
	print(item)

# This method cycles through a dictionary
# for a fixed number of times.
# Usually not used in real-time applications