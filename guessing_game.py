import random

print("-------->   Hello! Welcome to the Number Guessing Game!   <--------")

def start_game():
    user_attempts = 1
    rand_number = random.randrange(1,11)
    number = int(input("Please select a number from 1 to 10.  "))
    while True:
        if number > rand_number:
            print(f"Sorry, the correct number is lower than your guess of {number}. Please try again.")
            user_attempts += 1
            number = int(input("Please select a different number from 1 to 10.  "))
            continue
        elif number < rand_number:
            print(f"Sorry, the correct number is higher than your guess of {number}. Please try again.")
            user_attempts += 1
            number = int(input("Please select a different number from 1 to 10.  "))
            continue
        elif number == rand_number:
            print(f"Congratulations! {number} is the correct number!")
            if user_attempts == 1:
                print(f"It took you {user_attempts} try.")
            else:
                print(f"It took you {user_attempts} tries.")
            break


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
