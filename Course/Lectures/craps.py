import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

roll = die1 + die2

print("You rolled", roll, end=".\n")

if roll == 2 or roll == 3 or roll == 12:
    print("You crapped out!")
    done = True
elif roll == 7 or roll == 11:
    print("You win with a natural!")
    done = True
else:
    point = roll
    print("The point is", point)
    done = False

while not(done):
    die1 = random.randrange(6) + 1
    die2 = random.randrange(6) + 1
    
    roll = die1 + die2
    input("Press enter to roll again.")
    print("You rolled", roll, end=".\n")

    if roll == 7:
        print("You lose!")
        done = True
    elif roll == point:
        print("You rolled the point.")
        print("You win.")
        done = True