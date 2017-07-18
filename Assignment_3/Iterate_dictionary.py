# Iterate over the dictionaries using for loops

jargon = {'apple': 1000, 'windows': 300, 'samsung': 650, 'xiomi': 500}

for key in jargon.items():
    print(key, "corresponds to mobile companies")

# DO UTILIZE BOTH, KEY AND VALUE, WE CAN USE

for key, value in jargon.items():
    print(key, "corresponds to", jargon[key])