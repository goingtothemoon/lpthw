# Variable x is calling the %d (signed interger decimal) which is equal to 10
x = "There are %d types of people." %10
# Variable binary is equal to binary
binary = "binary"
# Variable do_not is equal to don't
do_not = "don't"
# Variable y has a string anf within it is calling for %s (String) which outside of the string is equal to binary and do_not where do_not is called upon which equals don't
y = "Those who know %s and those who %s" %(binary, do_not) #1

# Prints variable x and y
print x
print y

# print string folowed by using %r (calls string not matter what) and I call for the variable x
print "I said: %r." % x #2
# Same as above but for y
print "I also said: '%s'." % y #3
# Variable hillarious set to false
hilarious = False
# Variable joke_evaluation is set to a string ending with %r 
joke_evaluation = "Isn't that joke so funny?! %r" #4
# Calling joke_evaluation we print the string and I let the variable know to use hilarious for %r
print joke_evaluation % hilarious

# Setting variables w and e to print a string
w = "This is the left side of..."
e = "a string with a right side."

# Adding both variables together giving us a sentence
print w + e #5

