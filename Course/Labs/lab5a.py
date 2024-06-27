num=int(input("Enter a positive integer: "))
Sum=0
i=0
while True:
    Sum+=i
    if i==num:
        break
    i+=1
    print(i, end=" ")
    
print("")
print("The sum is ",Sum)