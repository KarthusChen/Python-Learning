import random
User1=int(input("User 1, enter a number between 1 and 10: "))
User2=int(input("User 2, enter a number between 1 and 10: "))
MagicNum= random.randint(1,10)

User1Diff=abs(User1-MagicNum)
User2Diff=abs(User2-MagicNum)

print("Magic Number:", MagicNum)

if User1Diff<User2Diff:
    print("User 1 guessed ",User1,", which is closer to ",MagicNum," than ",User2,sep="")
elif User1Diff==User2Diff:
    print("There is no winner")
else:
    print("User 2 guessed ",User2,", which is closer to ",MagicNum," than ",User1,sep="")



