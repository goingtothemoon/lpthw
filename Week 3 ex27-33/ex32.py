the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# In python these collections of data are called lists
# In many other languages they are called arrays

# For for-loopsm structure is similar to def and if
# with colon at the end of first line, then indent

# this first kind of for-loop goes through a list
for number in the_count:
	# The first variable (right after for) can use
	# any name you like, although i (integer or index) is common
	print "This is count %d" %number
	# %d because these are numbers (or digits) (%d decimal)

# same as above
for fruit in fruits:
	# Just don't use the same name twice
	print "A fruit of type: %s" % fruit
	# %s because the fruit names are strings


# also we can go through mixed list too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	# The %s specifier converts the object using str(), and %r converts it using repr()
	# Data has diffrent types

# we can also build lists, first start with an empty one 
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	# Range starts at first number (inclusive) but
	# stops at 1 less than second number (exclusive)
	# This is how items in a list are numbered
	# But 0 as first number is default, so this can
	# also be written as "range(6)"
	# Can also specify whether range foes up or down
	# and size of steps.
	print "Adding %d to the list." % i
	# append is a finction that lists understand
	elements.append(i)
	# This adds the numbers to the list one at a time

# now we can print them out too
for i in elements:
	print "Elements was: %d" % i

# Here is an easier way
elements2 = range(6)
for i in elements2:
	print "elements2 item was: %d" %i

