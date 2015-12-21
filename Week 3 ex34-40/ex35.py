from sys import exit
# system import exit which is a special function

def gold_room():
	print "This room id full of gold. \nHow much do you take?"

	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		# function dead is defined below

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
		# exit is a system function that was imported at the top
		# 0 is a code for an error-free exit (vs. 2, 16, 89, etc.)
	else:
		dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    # bear_moved is a boolean variable (means true or false)

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
            # function gold_room was defined above
        else:
            print "I got no idea what that means."
            # may want to add prompts to give ideas


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
    	# This looks at the text you enered and if the keyword
    	# flee appears in it anywhere, it does this command
    	start()
    	# function start is defined below
    elif "head" in choice:
    	# Check for keywword head anywhere in enered text
    	dead("Well that was tasty!")
    	# function dead is called
    else:
    	cthulhu_room()
    	# Returns user to the start of this function


def dead(why):
  	print why, "Good job!"
  	exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
    	bear_room()
    elif choice == "right":
    	cthulhu_room()
    else:
    	dead("You stumble around the room until you starve")


start()