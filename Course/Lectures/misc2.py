# global

def access_global():
    print(x)

def access_local():
    x = "local"
    print(x)

def modify_global():
    global x
    x = "changed in modify global"
    print(x)

x = "global"

access_global()

input("\nPress Enter to continue...")

access_local()

input("\nPress Enter to continue...")

print(x)

input("\nPress Enter to continue...")

modify_global()

input("\nPress Enter to continue...")

print(x)

input("\nPress Enter to continue...")

# yield

def factorial():
    total = 1
    i = 1
    while True:
        yield total
        total *= i
        i += 1

for val in factorial():
    if val > 1000000000:
        break
    print(val)
