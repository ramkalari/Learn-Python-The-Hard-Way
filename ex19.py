# defines a function with the name cheese_and_crackers. The function accepts 2 arguments cheese_count and box_of_crackers
def cheese_and_crackers(cheese_count, box_of_crackers):
	# prints the number of cheeses
	print "You have %d cheese!" % cheese_count
	# prints the number of boxes of crackers
	print "You have %d boxes of crackers!" % box_of_crackers
	# prints the string "Man, that's enough for a party"
	print "Man that's enough for a party"
	# prints the string "Get a blanket." and a newline
	print "Get a blanket.\n"

# prints the string "We can give the function just numbers directly:"
print "We can give the function just numbers directly:"
# calls the function cheese_and_crackers with the arguments as 20 and 30.
cheese_and_crackers(20, 30)
# prints the string enclosed in double quotes
print "OR, we can use variables from our script:"
# assigns the value 10 to the name amount_of_cheese
amount_of_cheese = 10
# assigns the value 50 to the name amount_of_crackers
amount_of_crackers = 50
# calls the function with the variables defined above as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print the enclosed string
print "We can even do math inside too:"
# calls the function with the computed argument values.
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# calls the function where the computation combines variables and numbers.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)







