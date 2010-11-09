# imports the identifier argv from the module sys
from sys import argv

# unpacks argv
script, input_file = argv

# defines a function called print_all that accepts a file as argument and prints the contents of the file
def print_all(f):
	print f.read()

# defines a function rewind that rewinds the given file to the beginning
def rewind(f):
	f.seek(0)

# defines a function print_a_line that takes the line_count and a file as arguments and print the current linenumber and line
def print_a_line(line_count, f):
	print line_count, f.readline()

# opens the input file
current_file = open(input_file)

print "First, let's print the whole file:\n"

# calls the function print_all with the input file as argument
print_all(current_file)

print "Now, let's rewind, kind of like a tape."

# rewinds current_file to the beginning
rewind(current_file)

print "Let's print three lines."

current_line = 1
# prints the first line of current_file
print_a_line(current_line, current_file)

current_line = current_line + 1
# prints the second line of current_file
print_a_line(current_line, current_file)

current_line = current_line + 1
# prints the 3rd line of current file
print_a_line(current_line, current_file)





