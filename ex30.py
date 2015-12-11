# Create 3 variables and assigned values

people = 30
cars = 40
trucks = 15

# elif is short for else if and it is used for
# additional conditions, while else is used to
# cover anything not specifically addressed.

if cars > people:
    # 40 > 30 is true so this will print and
    # skip the elif and else
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide."

if trucks > cars:
    # 15 < cars so the first line was skipped
    print "That's too many trucks."
elif trucks < cars:
    # 15 < 40 is true so this line will print and else will be skipped
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    # 30 > 15 is true so this will print and skip else
    print "Alright, lets just take the trucks."
else:
    print "Fine, let's stay home then."