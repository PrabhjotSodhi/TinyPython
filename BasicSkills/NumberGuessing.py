import random
import math

# Taking Inputs
lower = int(input("Emter Lower bound: ")) 
upper = int(input("Enter Upper bound: ")) 

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print(f"You have {round(math.log(upper - lower + 1, 2))} chances to guess the integer!")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1
	# taking guessing number as input
	guess = int(input("Guess a number: "))
	# Condition testing
	if x == guess:
		print(f"Congratulations you did it in {count} tries!")
		# Once guessed, loop will break 
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses, 
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print(f"The number is {x}")
	print("Better Luck Next time!")