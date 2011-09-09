tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

slim_cat = """My name is %s. \nI'm a slim cat.
I'll never be tabby""" % ("jeffrey")

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print slim_cat

print "%r" % "I'm 5'7\" tall"

