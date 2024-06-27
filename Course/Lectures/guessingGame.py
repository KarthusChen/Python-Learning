import random

n = 100

num = random.randint(1, n)

guess = int(input("Enter a guess between 1 and {}: ".format(n)))

while guess != num:
    if guess < num:
        print("Higher")
    else:
        print("Lower")

    guess = int(input("Enter a guess: "))

print("You guessed it! The number was", num, end=".\n")