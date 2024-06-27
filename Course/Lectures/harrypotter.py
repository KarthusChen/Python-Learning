import turtle
import random

t = turtle.Turtle()
t.screen.title("It's Harry Potter!")

t.screen.bgcolor("black")
t.pensize(10)
t.speed(0)
t.hideturtle()

#stars
for i in range(100):
    t.color("white")
    x = random.randrange(-400, 400)
    y = random.randrange(-350, 350)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(2)

#shirt
t.speed(3)
t.shape("circle")
i = 1
for j in range(400, 800, 40):
    t.penup()
    t.goto(0,-j)
    t.shapesize(40,7,5)
    t.pendown()
    if (i%2 == 0):
        t.color("gold", "goldenrod")
    else:
        t.color("darkred", "firebrick")
    t.stamp()
    i += 1

t.penup()
t.goto(50,-400)
t.pendown()
t.color("gray", "dim gray")
t.shape("circle")
t.shapesize(40,2,5)
t.stamp()

t.penup()
t.goto(-50,-400)
t.pendown()
t.stamp()

#face
t.penup()
t.goto(0,-100)
t.pendown()
t.color("bisque", "peach puff")
t.begin_fill()
t.circle(100)
t.end_fill()

#eyes/glasses
t.penup()
t.goto(-50,-25)
t.pendown()
t.pensize(5)
t.color("black", "white")
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(50,-25)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(-50,-15)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.goto(50,-15)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.goto(-100,0)
t.pendown()
t.fd(25)

t.penup()
t.goto(-25,0)
t.pendown()
t.fd(50)

t.penup()
t.goto(75,0)
t.pendown()
t.fd(25)

#scar
t.penup()
t.goto(-20,100)
t.pendown()
t.color("maroon", "brown")
t.pensize(5)
t.fd(15)
t.right(120)
t.begin_fill()
t.fd(60)
t.left(160)
t.fd(50)
t.left(140)
t.fd(35)
t.right(120)
t.fd(20)
t.end_fill()

#smile
t.penup()
t.goto(-25, -50)
t.color("black")
t.right(140)
t.pendown()
t.circle(25, 180)

