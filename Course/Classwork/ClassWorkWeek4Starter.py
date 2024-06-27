# include a correct import statement
# ???

# we will use x to verify the theoretical probabilities
x = int(input("Enter a number from 2 to 12: "))

n = 1000000 # the number of times the loop will run
i = 0 # a counter to see how many time the loop has run
match = 0 # used to count the times when the sum is x

while i < n:
    # generate the roll of two dice
    # ???

    # sum up the dice just rolled
    # ???

    # use a selection structure to check if the sum of the dice
    # matches x - if it does increment match
    # ???

    # increment i
    # ???


# printing the probability of rolling 2 die and getting a sum of x
print(match / n)
