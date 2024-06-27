from random import random

drops = 1000000
above = 0
wow = 0

for _ in range(drops):
    x = random()
    y = random()
    
    if y > x:
        above += 1

    if y == x:
        wow += 1
        
print("above =", above)
print("wow =", wow)
