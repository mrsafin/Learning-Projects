import random
import math

print("Welcome to the Number Guessing Game!\n")

# Input Upper and Lower bound from the user
lower = int(input("Write the lower bound: "))
upper = int(input("Write the upper bound: "))

# Choose a random number between the range
random = random.randint(lower, upper)

# Calculate the guesses
min_gusses = int(math.log2(upper - (lower + 1)))
print(f"You have {min_gusses} guesses")

game_over = True
while game_over:

    # if there is no guesses left, finish the game
    if min_gusses == 0:
        print("\nYou don't have any gusses left. \nBetter Luck Next Time!")
        break
    
    # Input user guessed number
    guess = int(input("\nGuesse a number between your range: "))

    # if the gussed number is grater than the random number
    if guess > random:
        print("\nTry Again! You guessed too high")
        min_gusses -= 1
        print(f"You have {min_gusses} guesses left")

    # if the gussed number is smaller than the random number
    elif guess < random:
        print("\nTry Again! You guessed too small")
        min_gusses -= 1
        print(f"You have {min_gusses} guesses left")

    # If user gussed the right number 
    else:
        print("\nCongratulation! You guessed the right number")
        game_over = False
