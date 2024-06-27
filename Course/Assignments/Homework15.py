import turtle
import random

# Function to draw a random shape with random colors
def draw_shape(t, shape):
    t.color(random.choice(['red', 'green', 'blue']))
    if shape == 'circle':
        radius = random.randint(10, 100)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    elif shape == 'square':
        side = random.randint(20, 100)
        t.begin_fill()
        for _ in range(4):
            t.forward(side)
            t.right(90)
        t.end_fill()
    elif shape == 'triangle':
        side = random.randint(20, 100)
        t.begin_fill()
        for _ in range(3):
            t.forward(side)
            t.right(120)
        t.end_fill()

# Main application code
def main():
    screen = turtle.Screen()
    screen.bgcolor('white')
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    
    for _ in range(10):  # Draw 10 shapes at random positions
        shape = random.choice(['circle', 'square', 'triangle'])
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_shape(t, shape)
    
    turtle.done()

# Running the main function to create a unique artwork
main()
