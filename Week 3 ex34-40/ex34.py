animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print animals
for i in animals:
	print i

print ""
print "First, Second, third are ordinal numbers but we"
print "need to count by cardinal numbers : 1, 2, 3,"
print "With lists, you start at 0."
print ""

# To access a particular item in a list, put the list
# name and then index number in square brackets

for i in range(len(animals)):
	print "Index %d in the list is %s" % (i, animals[i])

# for i which is variable animals. 
# len means length (however long it is do it that many times)

print "\n"
print animals[4]