"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random, time, sys



def main():
	start_game()
	continue_game()

def start_game():
	print("############################################################")
	print("          ######################### Welcome Player! ##############################")
	print("############################################################")
	print("          ########################################################################")
	time.sleep(1)
	random_number = random.randint(1,10)
	guesses = 0
	secret_number = True
	while secret_number != random_number:
		try:
			secret_number = int(input("Please enter a number between 1 and 10:    "))
			if secret_number < random_number:
				print("It's higher")
				guesses += 1
			if secret_number > random_number:
				print("It's lower")
				guesses += 1
		except ValueError:
			print("not valid")
	secret_number = random_number
	guesses += 1
	print("Congratulations it took you",str(guesses),"attempts. The secret number is",(secret_number),)
start_game()

def continue_game():
	continue_game = input("Play again?  ")
	while continue_game.lower() == "y":
		start_game()
	else:
		continue_game.lower() == ("no", "n")
		print("Game Over")
		sys.exit()
continue_game()
#		sys.exit()

main()

