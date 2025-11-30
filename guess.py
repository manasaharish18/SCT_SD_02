import random
number= random.randint(1,100)
print("Welcome to the Number guessing Game!")
print("I have generated a number between 1 and 100.")
print("Try to guess it!")
while True:
    guess=int(input("Enter your guess:"))
    if guess<number:
        print("Too low! Try again.")
    elif guess>number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number:",number)
        break