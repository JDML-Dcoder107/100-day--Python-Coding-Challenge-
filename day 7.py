#Day 7 generating random number
import random
print(" Welcome to the Random Number Guessing Game ".center(60, "="))
num_guess = random.randint(1, 101)
attempts = 5
print("I have selected a random number between 1 and 100.")
while attempts > 0:
    guess = int(input("Your guess: "))
    if guess < num_guess and guess < 100:
        attempts -= 1
        print(f"Too low!, you have {attempts} attempts left.\n")
    elif 100 >= guess and guess > num_guess:
        attempts -= 1
        print(f"Too high!, you have {attempts} attempts left.\n")
    elif guess == num_guess:
        print("Congratulations! You've guessed the correct number!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    if attempts == 0:
        print(f"The number is {num_guess}. Better luck next time!")
