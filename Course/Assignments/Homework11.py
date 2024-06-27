def names():
    name_count = {}
    
    while True:
        name = input("Enter next name: ")
        if name == 'q':
            break
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    
    for name, count in sorted(name_count.items()):
        print(f"{count} student(s) named {name}")

names()

