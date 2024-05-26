import random

top = int(input("How high would you like the range to go up?"))
x = int(random.randrange(1,top))
guess = int(input(f"Guess the the number from 1 to {top}: "))

tries = 1
while x != guess:
    if int(x) > int(guess):
        print("Higher")
    else:
        print("Lower")
    guess = input("Incorrect! Try again: ")

    if int(x) == int(guess):
        print(f"Correct! It took you {tries} tries!")
        break
    tries += 1

else:
    print(f"Correct! It only took you {tries} try!")
