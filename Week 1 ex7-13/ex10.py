# \t will tab  \n is a new line
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm splt\non a line."

# double backslash will print a single backslash
backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat 

# Escaping a percent requires a percent sign.
# %r prints everthing while the %s print the formatted
print "The very literal tabby cat uses %%r and says: '%r'" %tabby_cat
print "the formatted tabby cat uses %%s and says: '%s'" %tabby_cat