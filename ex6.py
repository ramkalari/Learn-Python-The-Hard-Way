# the value 10 is substituted for %d and assigned to the variable x
x= "There are %d types of people." % 10
# the value binary is assigned to a name binary
binary = "binary"
# the string don't is assigned to the variable do_not
do_not = "don't"
# the values of the variables binary and do_not are substituted into the string and assigned to y.
y = "Those who know %s and those who %s." % (binary, do_not) # 2 times
# prints the value of x
print x
# prints the value of y
print y
# substitutes the string x surrounded by single quotes for % r and print the resulting value
print "I said: %r." %x # 3rd time
# substitutes y for %s and print the resulting value
print "I also said: '%s'." %y # 4th time. since '%s' is also a string it should be 5 times
# assigns the boolean value False to a name hilarious
hilarious = False
# assigns the string to a name joke evaluation. If a format value is specified, it will replace the %r
joke_evaluation = "Isn't that joke so funny?! %r"
# replaces %r of joke_evaluation with the value of the variable hilarious
print joke_evaluation % hilarious
# assigns the string to a var w
w = "This is the left side of ..."
# assigns the string to a variable e
e = "a string with a right side."
# print the concatenation of w and e 
print w + e


