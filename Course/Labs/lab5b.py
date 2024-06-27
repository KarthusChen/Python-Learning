Sum=0
while True:
    num=int(input("Enter a positive integer (<=0 to quit): "))
    if num%2==0:
        Sum+=num

    if num<=0:
        break

print("The sum of the positive even integers entered is ", Sum)