import random

number_to_guess = random.randint(1, 10)
user_guess = int(input("Guess the number between 1 and 10: "))

if user_guess == number_to_guess:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {number_to_guess}.")
