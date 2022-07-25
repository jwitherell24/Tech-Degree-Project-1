import random

print("-------->   Hello! Welcome to the Number Guessing Game!   <--------")

def start_game():
    user_attempts = 1
    rand_number = random.randrange(1,11)
    rand_range_low = 1
    rand_range_high = 10

    while True:
        try:
            number = int(input(f"Please select a number from {rand_range_low} to {rand_range_high}.  "))
        except ValueError:
            print("Sorry, that is not a valid value. Please guess again.")
        else:
            if number != rand_number:
                user_attempts += 1
            if number < rand_range_low:
                print(f"Sorry, that number is not within the range of {rand_range_low} and {rand_range_high}. Please guess again.")
                continue
            if number > rand_range_high:
                print(f"Sorry, that number is not within the range of {rand_range_low} and {rand_range_high}. Please guess again.")
                continue
            elif number > rand_number:
                print(f"Sorry, the correct number is lower than your guess of {number}. Please try again.")
                continue
            elif number < rand_number:
                print(f"Sorry, the correct number is higher than your guess of {number}. Please try again.")
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
