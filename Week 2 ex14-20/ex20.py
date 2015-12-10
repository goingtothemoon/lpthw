# import argv from sys
from sys import argv

# get arguments
script, input_file = argv

# define print_all function, which takes 1 argument (f)
# file. "f" is just a variable name for the file
def print_all(f):
	# define the contents of f using the operator .read
	print f.read(0)

# define rewind function, which takes 1 argument (f)
# creating a function to go to the beginning of a file ex byte 0
def rewind(f):
	# move the file pointer back to the beginning of file f
	# for the object f do thsi method/function seek the 0 is just bytes (go to the beginning)
	f.seek(0)

# define the print_a_line function, which takes 2 arguments (line_count, f)
def print_a_line(line_count, f):
	# print line_count then a line from f useing another method/fuctions .readline (one line at a time)
    print line_count, f.readline()

# set current_file variable to a file pointer to input_file
# = is the assignment operator
current_file = open(input_file)

# print string
print "First let's print the whole file:\n"

# call print_all function with current_file as an argument
print_all(current_file)

# print string
print "Now let's rewind, kind of like a tape."

# call rewind function with current_file as an argument
rewind(current_file)

# print a string
print "Let's print three lines:"

# set current_line to 1
current_line = 1

# call print_a_line to current_line and current_file as arguments
print_a_line(current_line, current_file)

# current line is now equal to current line + 1 (called a incrementing function using the + 1)
current_line = current_line + 1

# call print_a_line to current_line and current_file as arguments
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)