def get_nums():
    x = int(input("Num 1: "))
    y = int(input("Num 2: "))
    return x, y

def average(a, b):
    return (a + b) / 2

m, n = get_nums()
print(average(m, n))

print(average(*get_nums()))
