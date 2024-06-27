S = list(input("Enter a string:"))
FD={}
for element in S:
    FD[element]=S.count(element)
    frequency=0
    if S.count(element)> frequency:
        frequency=S.count(element)
        theKey=element
print(theKey," ",FD[theKey])