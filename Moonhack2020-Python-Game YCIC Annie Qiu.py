#!/bin/python3

# import  library
import random

# create a list of events

events = [
	("You are beginning to smell, do you take a shower?", 200, 0),
	("You hear a hissing sound, do you investigate?", 50, 100),  # yes -100 , #no -500
	("A lump of ice has fallen from the sky nearby,\
  do you retrieve it?", -150, 0),
	("You watched a YouTube video about the best lawns in the solar system. \
  Do you decide to try and grow a lawn in the desolate Martian soils?", \
	 10, 0),
	("Your cousin Harold has mysteriously appeared.\
  Do you send him away?", 20, 0),
	("Mmm, salty food. Do you eat it?", 30, -15),
	("You spot an oasis off in the distance, do you investigate?", -100, 0),
	("Your plants are dying, should you water them?", 15, 5),
]


def game():
	water: int = 1000
	day = 1
	# player's beginning amt.
	while water > 0:
		while True:
			water -= 10  # if water is greater than zero, it subtracts 10L everyday
			print("Day" + str(day) + "." + "Your Water" + str(water) + "L")  # amt of water per day and day
			if water >= 0:  # restart this part
				event = random.choice(events)  # taking a random choice of events
				response = input(event[0] + "(yes/no):").lower()  # let the user answer yes or no in lowercase
				while response not in ['yes', 'no']:
					print ('Please provide yes or no answer')
					response = input(event[0] + "(yes/no):").lower()
				if response == "yes":
					if water >= event[1]:
						water -= event[1]  # If yes then add the first number and then break
						break
					else:
						print('You are running out of water!')
						water -= event[1]
						return False
				elif response == "no":
					if water >= event[2]:
						water -= event[2]  # If no then add the second number and then break
						break
					else:
						print('You are running out of water!')
						water -= event[2]
						return False



		day += 1  # say how many days you lasted
		print("you lasted " + str(day) + " days")

	print("You have lost this round :(")

	return water


water_left = game()
if water_left <= 0:
	restart_game = input("Do you want to restart the game? yes or no?").lower()
	while restart_game not in ['yes', 'no']:
		print ('Please provide yes or no answer')
		restart_game = input("Do you want to restart the game? yes or no?").lower()
	if restart_game == "no":
		print("Thanks for playing!")
	elif restart_game == "yes":
		water_left = game()

print(water_left)
# while water_left  = 0
