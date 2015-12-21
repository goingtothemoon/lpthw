from sys import exit
import random

prompt = "-> "

# Using https://github.com/ianthiel/LPTHW_ex36_escape/blob/master/ex36.py
# as an example for this ex.

# details for prison cell
print """
		So you want to hear my story celly...

		I did 4 years, 9 months, and 16 days in new york state prisons
		for a crime I committed when I was 18, a month before I graduated 
		from...

		*You hear a man's voice and turn your head away from conversation*

		What your name bruh?

		... I am :

"""

name = raw_input(prompt)

print " 'See you on the outside %s!" % name

def hallway_start():
	print """
		You are in a hallway outside your cell.
	You see three doors: one to your left, one straight ahead, and one to your right.
	The door on your left is made of iron.
	To your right, the door is ornate and glass.
	Ahead, the door is most plain.
	
	What do you do?
	
	1. Walk through door on left.
	2. Walk through door straight ahead.
	3. Walk through door on right.
	4. Wait.

	"""
	choice = int(raw_input(prompt))
	
	if choice == 1:
		guard_room()
	elif choice == 2:
		dark_room()
	elif choice == 3:
		mirrors_room()
	elif choice == 4:
		dead("Two guards arrive and kill you.")
	else:
		dead("Confused, you took your meds... and died. *name on bottle Ted*")	

	# if choice == 1:
	# 	guard_room()
	# elif choice == 2:
	# 	dark_room():
	# elif choice == 3:
	# 	mirrors_room()
	# elif choice == 4:
	# 	dead("Two guards take you to solitary.")
	# else:
	# 	dead("Confused, you took your meds... and died. *name on bottle Ted*")

#details for mirror room
def mirrors_room():
	print """
	You are in a bright room full of mirrors.
	You grow confused and frightened.
	You feel as if you're being watched.
	
	What do you do?
	
	1. Shatter the nearest mirror with your fist.
	2. Study the room further.
	3. Turn back.
	
	"""

	# choice = int(raw_input(prompt))
	
	# if choice == 1:
	# 	dead("You shatter the nearest and turn to glass. A voice laughs. You are dead.")
	# elif choice == 2:
	# 	print "You realize the room is a puzzle. You are determined to solve it."
	# 	intelligence = random.randint(1,6)
	# 	print "Your intelligence is %s." % intelligence
		
	# 	if intelligence > 3:
	# 		print "You successfully navigate the maze."
	# 		print "Ahead, there is a large wooden door. You open it."
	# 		stables()
	# 	else:
	# 		dead("You are unable to navigate the maze. Mad, you die of starvation.")
	# elif choice == 3:
	# 	hallway_start()
	# else:
	# 	dead("Confused, you kill yourself somehow.")

	choice = int(raw_input(prompt))

	if choice == 1:
		dead("This isnt a movie.. you shatter the glass and bleed out.")
	elif choice == 2:
		print "Why is this room a puzzle... how can I solve this."
		intelligence = random.randit(1,10)
		print "Your intelligence is %s out of 10" % intelligence

		if intelligence >3:
			print "All that time in the library paid off"
			print "You find yourself infront of a wooden door... you open it."
			stables()
		else:
			dead("Maybe you should of hit the books harder. Try again.")
	elif choice == 3:
			hallway_start()
	else:
			dead("Confused you take your meds.")

#details for guard room
def guard_room():
	print """
	You enter a small room.
	On the wall ahead there hangs a rack of swords.
	To your right is a door.
	To your left is a square table.
	Seated there are two guards.
	They notice you and begin to stand.
	
	What do you do?
	
	1. Fight!
	2. Run through the door on your right.
	3. Turn back, quickly!
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		print "Ready to throw down.. you lunge at a guard!"
		strength = random.randit(1,10)
		print "Your strength is %s. " % strength
		if strength > 3:
			print "Gym time paid off you walk to the door."

			boat(room)
		else:
			dead(" The guards gotcha.")
	elif choice == 2:
		dead("The guards gotcha")
	elif choice == 3:
		hallway_start()
	else:
		dead("Guard gotcha.")

# details for boat room

def boat_room():
	print """
	You enter a large, humid room.
	You can smell the sea.
	To your right you see a large, wide door.
	Straight ahead, you see a single small boat is moored.
	Your pulse quickens.
	
	What do you do?
	
	1. Use the boat to escape.
	2. Use the door to your right.
	3. Turn back.
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		escape("You push off from the dock just as guards arrive. You are free.")
	elif choice == 2:
		stables()
	elif choice == 3:
		dead("You turn around to leave the room. Two guards arrive and kill you.")
	else:
		dead("Confused, you fall into the water and drown.")

# details for stables
def stables():
	print """
	You enter a large room where many horses are stabled.
	You entered loudly, and the horses are startled.
	To your right is an ornate glass door.
	To your left, a large door is open to the outside world.
	Sunshine flows in.
	
	What do you do?
	
	1. Mount a horse and ride off.
	2. Open the ornate glass door.
	3. Turn back.
	
	"""
	
	choice = int(raw_input(prompt))
	
	if choice == 1:
		dead("You are pursued and killed by two guards on horseback.")
	elif choice == 2:
		mirrors_room()
	elif choice == 3:
		dead("A single guard arrives and kills you.")
	else:
		dead("Confused, you are kicked in the head by a horse and killed.")

# details for dark room
def dark_room():
	print """
	You are in a dark room. The door to the hallway is closed.
	The room is pitch black. You see nothing.
	
	What you do?
	
	1. Wait.
	2. Move forward.
	3. Go back.
	
	"""
	choice = int(raw_input(prompt))
	
	if choice == 1:
		dark_room()
	elif choice == 2:
		print """
	You stumble forward and feel two doors.
	One on your left, another on your right.
	
	What do you do?
	
	1. Go through the left door.
	2. Go through the right door.
	3. Wait.
	
		"""
		choice = int(raw_input(prompt))
		if choice == 1:
			boat_room()
		elif choice == 2:
			stables()
		elif choice == 3:
			dead("Four guards arrive and kill you.")
		else:
			dead("Confused, you trip and die.")
	elif choice == 3:
		hallway_start()
	else:
		dead("Confused, you trip and die.")

# details for dead function
def dead(why):
	print why, "Nice job... well not really %s." % name
	exit(0)

# details for escape
def escape(why):
	print why, "Congrats %s!!!" % name
	exit(1)

hallway_start()