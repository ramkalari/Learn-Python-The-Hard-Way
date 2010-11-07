from sys import argv

script, filename = argv

print "Reading file %r ..." %filename

file = open(filename)
print file.read()
