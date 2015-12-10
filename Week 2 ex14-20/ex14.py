from sys import argv

#added new argument last_name
script, first_name, last_name = argv
# Prompt will let me change where the user will put information into for the raw_input
prompt = ' Answer me!: '

print "Hi %s %s, I'm the %s script." % (first_name, last_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s %s?" % (first_name, last_name)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (first_name, last_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)




print """
Alright so you said %r about liking me.
You live in %r. Not sure where that is.
and you have a %r computer. Nice.
""" % (likes, lives, computer)