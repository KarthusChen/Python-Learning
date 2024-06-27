# include a correct import statement
import random

# we will use x to verify the theoretical probabilities.
x = int(input("Enter a number from 2 to 12: "))

n = 1000000 # the number of times the loop will run
i = 0 # a counter to see how many time the loop has run
match = 0 # used to count the times when the sum is x

while i < n:
    # generate the roll of two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # sum up the dice just rolled
    summ = die1 + die2

    # use a selection structure to check if the sum of the dice
    # matches x - if it does increment match
    if summ == x:
        match += 1

    # increment i
    i += 1


# print the probability of rolling 2 die and getting a sum of x
print(match / n)
