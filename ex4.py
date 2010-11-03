# Assigns the value 100 to a variable cars
cars = 100
# Assigns the float value 4.0 to space_in_a_car.
space_in_a_car=4.0
# Assigns the value 30 to the variable drivers
drivers = 30
# Assigns the value 90 to the variable passengers
passengers = 90
# computes the number of cars not driven and assigns it to the variable cars_not_driven
cars_not_driven = cars - drivers
# assigns the number of cars driven to be the same as number of drivers
cars_driven = drivers
# computes the total capacity of the fleet of cars and assigns it to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# computes the average passengers per car and sets it to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# prints the number of cars available
print "There are", cars, "cars available."
# prints the number of drivers available
print "There are only", drivers, "drivers available."
# prints the number of empty cars
print "There will be", cars_not_driven, "empty cars today."
# prints the total capacity of the car fleet
print "We can transport", carpool_capacity, "people today."
# prints the number of passengers
print "We have", passengers, "to carpool today."
# prints the number of passengers per car
print "We need to put about", average_passengers_per_car, "in each car."





