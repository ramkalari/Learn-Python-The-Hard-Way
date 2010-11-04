from sys import argv

script, user_name, age = argv
prompt = '>'

print "Hi %s, I'm the script %s" %(user_name, script)
print "You are only %r years old. It's not too late to learn programming" % age
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


