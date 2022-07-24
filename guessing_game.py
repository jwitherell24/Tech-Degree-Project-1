import random


def start_game():
    print("-------->   Hello! Welcome to the Number Guessing Game!   <--------")
    rand_number = random.randrange(1,11)
    number = int(input("Please select a number from 1 to 10.  "))
    if number > rand_number:
        print(f"Sorry, the correct number is lower than your guess of {number}. Please try again.")
        number = int(input("Please select a different number from 1 to 10.  "))
    elif number < rand_number:
        print(f"Sorry, the correct number is higher than your guess of {number}. Please try again.")
        number = input(int("Please select a different number from 1 to 10.  "))


    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()
