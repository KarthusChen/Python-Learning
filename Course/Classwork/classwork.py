bill = float(input("Enter bill: "))
people = int(input("Enter number of people in party: "))

if people >= 8:
    bill = bill * 1.18

print("The bill is ${:,.2f}.".format(bill))
