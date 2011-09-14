# import the module argv
from sys import argv

# unpacks argv into the two variables
script, filename = argv

# opens the given file and returns a file object
txt = open(filename)

print "Here's your file %r:" % filename
# reads the contents of the file and prints it
print txt.read()

txt.close()

print "Type the file name again:"
# gets the filename as a rawinput
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()


