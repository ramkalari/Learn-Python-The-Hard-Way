cities = {'CA': 'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(map, state):
	if state in map:
		return map[state]
	else:
		return map[found]

cities['_find'] = find_city

while True:
	print "State? (ENTER to quit)",
	state = raw_input("> ")
	
	if not state: break

	city_found = cities['_find'](cities, state)
	print city_found

# shallow copy of cities
copy_of_cities = cities.copy()

# clears all the items
cities.clear()

print cities

print copy_of_cities

for item in copy_of_cities:
	print item, copy_of_cities[item]

for state, city in copy_of_cities.items():
	print state,city



