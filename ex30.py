people = 50
cars = 60
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide"

if buses > cars:
	print "There's too many buses."
elif buses < cars:
# this block is executed only when buses < cars. 
	print "Maybe we could take the buses."
else:
# this block is executed when buses = cars.
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

if cars > people and buses < cars:
	print "Number of cars exceeds people as well as buses."
	


