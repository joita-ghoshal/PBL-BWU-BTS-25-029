# Number guessing game
# Random Numbers, conditions 


import random

random_int = random.randint(1, 100)

max_attempts = int(input("Enter the number of attempts: "))
attempts_left = max_attempts

print("\n*** Number Guessing Game ***")

while attempts_left > 0:
    x = int(input("Enter your guess (1-100): "))

    if x == random_int:
        print("\n Found the number!!")
        print("Total attempts taken:", max_attempts - attempts_left + 1)
        break

    elif x > random_int:
        attempts_left -= 1
        print("Too high")

    else:
        attempts_left -= 1
        print("Too low")

    if attempts_left > 0:
        print("Attempts left:", attempts_left)
    else:
        print("\nGame Over!")
        print("You have used all your attempts.")
        print("The correct number was:", random_int)