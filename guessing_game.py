"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

#input and output:

#conditional branching:
#loops:
#exception handling:
#import libraries:

######
import random
import time
import sys



def start_game():
	print("############################################################")
	print("          ######################### Welcome Player! ##############################")
	print("############################################################")
	print("          ########################################################################")
	time.sleep(1)
	random_number = random.randint(1, 10)
	guesses = 1
	secret_number = input("Guess a number between 1 and 10: ")
	#enter error for not integer
	#error for numbers out of range text. exception handling for numbers out of range	
	while random_number != secret_number:
		if secret_number < 10:
			print("Its Higher")
			time.sleep(5)
			guesses = guesses + 1
		elif secret_number > 0:
			print("It's Lower")
			time.sleep(.5)
			guesses = guesses + 1			
	random_number = secret_number
	print("Congratulations it took you",str(guesses), "attempts. The secret number is" ,(secret_number),)
	continue_game = (input("Play again?"))
	continue_game = "yes", "Yes"
	while continue_game == ("yes", "Yes"):
		start_game()
	continue_game = ("no", "No")
	print("Congratulations it took you",str(guesses), "attempts. The secret number is" ,(secret_number),)  
	print("Game Over")
	
	#####
	def out_range(int):
		try:
			if secret_number > 10:
				raise ValueError("not valid")
			if secret_number < 0:
				raise ValueError("not valid")
		except ValueError:
			print("not valid")
	
start_game()
sys.exit("end of game")

#handle error and exceptions. how to
#raising exceptions is for the out of range
#


# Import the random module.

# Create the start_game function.
# Write your code inside this function.
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.


# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.

