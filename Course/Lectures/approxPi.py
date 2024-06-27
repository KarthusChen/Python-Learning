from random import random
from math import sqrt

drops = 10000000
hits = 0

for _ in range(drops):
    x = random()
    y = random()
    dist = sqrt(x**2 + y**2)
    
    if dist <= 1:
        hits += 1
        
print("\u03C0 \u2248 {}".format(4 * hits / drops))