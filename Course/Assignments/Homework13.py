class Money:
    def __init__(self, amount):
        self.amount = float(amount)

    def __str__(self):
        return "${:,.2f}".format(self.amount)

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        raise ValueError("Addition is only supported between Money instances")

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        raise ValueError("Subtraction is only supported between Money instances")

# Testing the Money class
money1 = Money(12345.78)
money2 = Money(8765.43)

print(money1)  # Output: $12,345.78
print(money2)  # Output: $8,765.43

money3 = money1 + money2
print(money3)  # Output: $21,111.21

money4 = money1 - money2
print(money4)  # Output: $3,580.35
