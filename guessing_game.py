"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random, time, sys

def start_game():
	print("############################################################")
	print("          ######################### Welcome Player! ##############################")
	print("############################################################")
	print("          ########################################################################")
	time.sleep(1)
	random_number = random.randint(1,10)
	guesses = 1
	secret_number = int(input("Enter a number between 1 and 10:    "))
	while secret_number != random_number:
		if secret_number < random_number:
			secret_number = int(input("It's higher:  "))
			guesses += 1
		else: 
			secret_number > int(input("It's lower:  "))
			guesses += 1
	print("Congratulations it took you",str(guesses), "attempts. The secret number is" ,(secret_number),)
	continue_game = input("Play again?")
	while continue_game.lower() == "y":
		start_game()
	else:
		print("end of game")
		sys.exit()


start_game()

