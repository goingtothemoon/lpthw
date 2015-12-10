#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()
#print "So, you're %r old, %r tall and %r heavy." % (
#	age, height, weight)

# The comma (,) tells python not to end the line with a new line and goes to the next


age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# Again the %r gives everything while the %s gives the formatted
print "So you're %r old, %r tall and %r heavy" % (age, height, weight)
print "More nicely, you're %s old, %s tall and %s heavy" % (age, height, weight)

# Simply put %r for programmers %s for customers. %r is better to find errors in code
