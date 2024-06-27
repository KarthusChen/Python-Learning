import turtle
import math

from random import uniform

size = 200 # allow resizing

t = turtle.Turtle()
t.hideturtle() # remove turtle pointer
t.speed(0) # draw at fastest speed
t.pensize(2)

# draw square boundary
t.penup()
t.goto(-size, size)
t.pendown()
t.forward(size * 2)
t.right(90)
t.forward(size * 2)
t.right(90)
t.forward(size * 2)
t.right(90)
t.forward(size * 2)
t.right(90)

# draw circle boundary
t.penup()
t.goto(0, -size)
t.pendown()
t.circle(size)

# generate and draw points
# keep track of points in circle
count = 0
for i in range(1000000):
    x = uniform(-size, size)
    y = uniform(-size, size)
    t.penup()
    t.goto(x, y)
    t.pendown()
    if math.sqrt(x ** 2 + y ** 2) <= size:
        count += 1
        color = "blue"
    else:
        color = "red"
    t.dot(4, color)
    approximation = count / (i + 1) * 4
    # print("\u03c0 \u2248", approximation)
    if math.isclose(approximation, math.pi, rel_tol = 0.0001):
        print(approximation, "is close to", math.pi, "at", i + 1)
        break


