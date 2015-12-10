from sys import argv
# A way of importing or adding code also called a module (libararies)
# argv is the argument variable thats holds variables that you send in or pass to python

#script, first, second, third = argv
# This line unpacks argv into four variables

#print "This script is called:", script
#print "Your first variable is:", first
#print "Your second variable is", second
#print "Your third variable is", third

script, age, height, weight = argv

#print "This script is called:", script
#print "First variable:", first
#print "Second variable", second
#print "Third variable", third
#print "Fourth variable", fourth

# Mixed raw input with argv. 

age = raw_input ("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input ("How much do you weight? ")

print "So, you're %s old, %s tall and %s heavy" % (
	age, height, weight)

