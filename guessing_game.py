import random

print("-------->   Hello! Welcome to the Number Guessing Game!   <--------")

def start_game():
    user_attempts = 1
    rand_number = random.randrange(1,11)

    try:
        number = int(input("Please select a number from 1 to 10.  "))

    except ValueError:
        print("Sorry, that is not a valid value. Please guess again.")

    else:
        while True:
            if number > rand_number:
                print(f"Sorry, the correct number is lower than your guess of {number}. Please try again.")
                user_attempts += 1
                try:
                    number = int(input("Please select a different number from 1 to 10.  "))
                except ValueError:
                    print("Sorry, that is not a valid value. Please guess again.")
                continue
            elif number < rand_number:
                print(f"Sorry, the correct number is higher than your guess of {number}. Please try again.")
                user_attempts += 1
                try:
                    number = int(input("Please select a different number from 1 to 10.  "))
                except ValueError:
                    print("Sorry, that is not a valid value. Please guess again.")
                continue
            elif number == rand_number:
                print(f"Congratulations! {number} is the correct number!")
                if user_attempts == 1:
                    print(f"Wow!!! It only took you {user_attempts} try. You must be psychic!")
                else:
                    print(f"It took you {user_attempts} tries.")
                print("Thank you for playing the number guessing game!")
                break

start_game()
