# Import argv from the sys module
from sys import argv

# Assign the name of the file as an argument to argv
script, filename = argv

# Open the file and assign the result to txt
txt = open(filename)

# Prints name of file and what is in the file
print "Here's your file %r:" % filename
print txt.read()

# Pompt asking for the file name again using > to indicate where to answer
print "Type the filename again:"
file_again = raw_input("> ")

# Opens the file
txt_again = open(file_again)

# Print the contents of the file
print txt_again.read()

txt.close()
txt_again.close()