print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'
# Line is in single quotes to any single quotes or apostrophes
# need to be escaped with a backslash. Note that blank spaces
# after newlines and tabs print as such

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Triple quotes for extended text,
# as well as newline and tab commands.
# From "Common Student Questions"


print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jard = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# These are the variable names WITHIN the function
# and are known as local variables (as opposed to
# global variables). They can be diffrent outside 
# the function (but they dont have to be).


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# This calls the function and fills the three variables.
# beans is used instead of jelly_beans but it doesn't 
# matter. The variables could be called X, Y, Z if you
# wanted. The function just fills them in with the return 
# values in the order that they are listed.

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)
# We use the variable names as defined above
# and not the variable names within the function

start_point = start_point / 10
# Reassigns start_point with a new value baed on the old one

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
# This version calls on the function and fills in the values
# directly without creating intermediate varible outside
# the function.