# Assigning values to variables
# assign 100 to variable cars
cars = 100
# how much space is in a car
space_in_a_car = 4
# how many drivers there are.
drivers = 30
# How many passengers there are.
passengers = 90
# Subtracting total # of cars(100) from total # of drivers and assigning that difference to cars_not_driven.
cars_not_driven = cars - drivers
# Number drivers assigned to cars driven
# cars need drivers. No driver == cars_not_driven
cars_driven = drivers
# How many people who are not drivers.
carpool_capacity = cars_driven * space_in_a_car
# Dividing the number of passengers by cars driven.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."
