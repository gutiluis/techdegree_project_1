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
	print("#"*20)
	print("          ######################### Welcome Player! ##############################")
	print("#"*20)
	print(" "*10, "#"*20)
	time.sleep(1)
	random_number = random.randint(1,10)
	guesses = 0
	secret_number = True
	while secret_number != random_number:
		try:
			secret_number = int(input("Please guess a number between 1 and 10:    "))
			if secret_number < random_number:
				print("It's higher. Try again...")
				guesses += 1
			if secret_number > random_number:
				print("It's lower. Try again...")
				guesses += 1
		except ValueError as err:
			print("Value entered not valid. Try again with integers only from 1 through 10.")
			print("({})".format(err))
	secret_number = random_number
	guesses += 1
	print("Congratulations it took you",str(guesses),"attempts. The random number is",(secret_number),)
start_game()

def continue_game():
	continue_game = input("Try again?")
	if continue_game == ("Yes", "y", "yes"):
		start_game()
	else: 
		continue_game == ("no", "n")
		print("Game Over.")
		sys.exit()
continue_game()


main()

