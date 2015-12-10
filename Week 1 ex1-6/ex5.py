# -*- coding: utf-8 -*-
# Setting variable to my name as a string to insert into a future print out
my_name = 'Richard'

# Variable to age , height, weight.
my_age = 28
my_height = 68.0 # In inches
my_weight = 180.0 # In lbs

# Setting variables to come out as string (since they are not numbers) to my eyes, teeth, and hair.
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

# Extra credit (convert the inches and pounds to centimeters and kilos)
conv_weight = my_weight * 0.453
conv_height = my_height * 0.083 


# I'm call %s (unknown) after the string is done I set it to call my_name I am assuming %s is because its a string.
# in the previous comment I used quotes which messed with the enconding and gave an error (pep-0263)

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height

# r is a very useful one. Its like saying print this no matter what

print "He's %r pounds heavy" % my_weight
print "Actually that's not too heavy!"
print "He's go %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." %(
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print "My weight intro kilograms is equal to %d" % conv_weight
print "My height converted to feet is equal to %d" % conv_height

# https://docs.python.org/2.4/lib/typesseq-strings.html
# String and Unicode objects have one unique built-in operation: the % operator (modulo)
# https://www.python.org/dev/peps/pep-0263/