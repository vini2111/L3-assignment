import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Pattern")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.color("white")

# Draw the pattern
for i in range(36):
    for j in range(4):
        t.forward(110)
        t.right(100)
    t.right(20)

# Close the turtle window when clicked
turtle.exitonclick()
