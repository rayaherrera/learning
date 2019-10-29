# September 30
# this is an octothrope -- it makes a comment (the line is ignored by the computer)
# this prints the text in green
print("hello world")
# this prints the text in green
print("Howdy' y'all")
# this prints the text in green
print("I like typing this.")
# this prints the text in green
print("This is fun.")

# math skills demo
# this displays the text, but also displays the number 2
print("I will now count my chickens", 2)
# this line completes a mathematical function
print("Hens: ", 25+30/6)
# this line calculates the function inside the parenthesis
print("Roosters: ", 100 - 25 * 3 % 4)
# this line prints the text and then displays line 3
print("Now I will count the eggs", 7)
# this line calculates the function inside the parenthesis
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# this line displays that the statement in the parenthesis is false
print(3 + 2 < 5 - 7)
print("I will now count the cows")
print(35.0 - 25.0 + 10.0 - 15.0)

# October 3
# Variables and some of their powers
cars = 100
space_in_car = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = space_in_car * cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("there are", drivers, "drivers available today.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put approximately", average_passengers_per_car, "in each car.")

# a story using variables
teams = 10
number_of_games = 100
games_per_team = number_of_games / teams
player_to_a_team = 9
players = 120
players_that_can_play = teams * player_to_a_team
players_who_cannot_play = players - players_that_can_play


print("There are", teams, "teams available.")
print("There will be", players_who_cannot_play, "who will not make a team.")
print("There will be", players_that_can_play, "as a whole.")
print("")

# More variables and playing with output
myName = "Ray"
myAge = "18"
myColor = "pink"

print("Let's talk about %s." % myName)
print("His favorite color is %s. " % (myColor))
print("And he's %s years old!." % (myAge))
