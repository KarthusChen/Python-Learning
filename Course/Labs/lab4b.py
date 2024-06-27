import random
choice1=input("Enter choice 1:")
choice2=input("Enter choice 2:")

decision=random.randint(1,2)
if decision==1:
    print("Random Selection Engine chooses: ",choice1)
else:
    print("Random Selection Engine chooses: ",choice2)