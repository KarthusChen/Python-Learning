List1=[]
for i in range(3):
    List1.append(int(input("Enter a number:")))

total=0

for element in List1:
    total+=element

average= total/len(List1)

print("The total of the number is ", total, ", and the average is ", average,".")
