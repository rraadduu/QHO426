#A dict is a 'bag' of values, each with its own label
#Add elements to a label with square brackets
dict_car = {"brand": "Ferrari","model": "SP1","year": 2008,"year":2012,"colours":["red","white","blue"]}#will print the latest element thats why is underlined
print(dict_car)

x = dict_car["model"]
print(x)

y = dict_car["colours"]
print(y)

z = dict_car.keys()#show all the labels using .keys()
print(z)