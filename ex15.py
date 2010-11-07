# imports argv from the sys module
from sys import argv

# unpacks argv into script and filename
script, filename = argv

# opens the file with the name filenam and assigns the resulting file to the variable txt
txt = open(filename)

# prints the name of the file
print "Here's your file %r:" % filename
# prints the contents of the file
print txt.read()
# closes the file
txt.close()
# asks the user to type a filename again
print "I'll also ask you to type it again:"
#assigns the filename to the varaible file_again
file_again = raw_input("> ")
# opens the file with the name file_again
txt_again = open(file_again)

# print txt_again.readlines()

#prints the contents of the file file_again
print txt_again.read()
print txt_again.fileno()
print txt_again.isatty()
print txt_again.seek(0)
print txt_again.read()
txt_again.close()
# print txt_again.read()


