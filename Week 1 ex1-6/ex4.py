
# creating variables by nameOfVariable=Value
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# using a previous variable we call them into making a variable
cars_not_driven = cars - drivers
cars_driven = drivers

# we can multiply/divide variable and use one variable name to call it
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars availabe"
print "There are only", drivers, "drivers availabe."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport,",carpool_capacity, "people today."
print "We have,",passengers, "to carpool today."
print "We need to put about",average_passengers_per_car, "in each car."