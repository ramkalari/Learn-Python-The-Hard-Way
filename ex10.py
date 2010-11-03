tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# \\ escapes a backslash
backslash_cat = "I'm \\ a \\cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# \newline is ignored
newline_cat="I'm going to try a new \newline escape sequence."
print newline_cat

# escape single quote
print 'Hi, Isn\'t Python supposed to be easy?'

# escape double quote
print "I'm 5'6\" tall."

# escape for Ascii Bell
print "How does a Ascii Bell look. Is it \a or something else?"

# escape backspace
print "What happens when I have a backspace\b in a string?"

# escape formfeed
print "What the hell is a form \f feed"


fat_single_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print fat_single_cat

#when i will use a triple single quote
bored_cat = ''' Hi there. I'm a bored cat. 
I love """ Inception
Dead Poet's society					
""" 
'''

print bored_cat

print 'I\'m now going to print %s' % 'my friend\'s name'

print 'I\'m now going to print %r' % 'my cousin\'s name'









