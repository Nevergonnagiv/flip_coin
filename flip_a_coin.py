import random as r
import time as t # A new library to learn

# Heads'n'tails
sides = ["heads", "tails"]

# User's side 
user_side = input("Choose your side: ").lower()

# Function for the game itself
def flipTheCoin():
    # Random side
    flipping = r.choice(sides)
    # Calculating the side of the computer
    if user_side == "heads":
        comp_side = "tails"
        print("The computer is " + comp_side)
        print()
    elif user_side == "tails":
        comp_side = "heads"
        print("The computer is " + comp_side)
        print()
    else:
        # If the user's isn't on the sides list, exit the program with an "Error" message
        print("Error")
        exit()
    
    # If the user chose the right side, the player won
    if user_side == flipping:
        print("Flipping...")
        t.sleep(2)
        print(f"The coin flipped {flipping}. You won!")
    # If the user chose the wrong side, the computer won
    elif comp_side == flipping:
        print("Flipping...")
        t.sleep(2)
        print(f"The coin flipped {flipping}. The computer won!")

# Let the game begin
flipTheCoin()