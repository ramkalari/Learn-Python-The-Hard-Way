name = 'Sriram  Balasubramanian'
age = 34 # not a lie
height = 65 # inches
weight = 158 # pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

height_in_cms= 2.54 * height
weight_in_kgs = 0.454 * weight 

print "Let's talk about %s." % name
print "He is %d inches tall" % height
print "He is %d lbs heavy" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)

print  "I want to print %r irrespective of what type it is" % age

print "My weight in kgs is %d" % weight_in_kgs
print "My height in cms is %d" % height_in_cms

# Common mistakes:forgetting the % character before the variable name and adding a , between the string and the % character




