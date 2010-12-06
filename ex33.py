i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num



def print_range(limit, step):
	i = 0
	while i < limit:
		print "Item: %d" % i
		i = i + step

def print_range_using_for(limit, step):
	elements = range(0, limit, step)
	for item in elements:
		print "Item: %d" % item

print_range(6, 2)
print_range_using_for(6, 2)

