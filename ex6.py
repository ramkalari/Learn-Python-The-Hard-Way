# replaces %d with 10
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
# replaces the first %s with binary and the second one with don't
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# replaces %r with the value of x encosed in single quotes
print "I said %r."  %x

#replaces %s with the value of y
print "I also said: '%s'. " %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

