i = 0
numbers = []
# Create an empty list similar to an array in other languages

# For while-loops, structures is similar to (def, if, and for-loops)
# with colon at end of first line, then indent

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	# Can also be writtes as i += 1
	# Note: In other languages you can write i++ but that
	# doesnt work in python
	# On the last loop, the increment raises i to 6 but it
	# doesn't get added to the list or get printed because
	# it happens after the print and append but before the
	# loop returns to (while i < 6) which stops the loop
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num 

# Study drills

# 1. Convert this while-loop to a function 
# that you can call, and replace 6 in the test (i < 6) with a variable.

print "\nConverting while-loop to function, drill_1"
def drill_1(n):
	i = 0
	numbers1 = [ ]
	while i < n:
		print "Item: %d" % i
		numbers1.append(i)
		i = i + 1
	print numbers1

# 2. Now use this function to rewrite the script to try different numbers.

print "\nUsinig drill_1 with n = 3"
drill_1(3)

print "\nUsing drill_1 with n = 8"
drill_1(8)

# 3. Add another variable to the function arguments that you can pass in 
#  that lets you change the + 1 on line 8 so you can change how much it increments by.

print "\nCreating function drill_3 to allow variable step size"
def drill_3(n, s):
	i = 0
	numbers3 = [ ]
	while i < n:
		print "Item %d" % i 
		numbers3.append(i)
		i = i + s
	print numbers3

# 4. Rewrite the script again to use this function to see what effect that has. 

print "\nUsing drill_3with n = 12 and s = 3"
drill_3(12, 3)

# 5. Write it to use for-loops and range. Do you need the incrementor in the 
#    middle anymore? What happens if you do not get rid of it?

print "\ndrill_5 uses a for-loop and range instead"
def drill_5(n, s):
	numbers5 = range(0, n, s)
	# Need to specify starting point of 0 so python
	# reads the other elements correctly
	for i in numbers5:
		print "Item: %d" % i 
	print numbers5 

drill_5(14, 4)
