import turtle

# Create a turtle object
n = turtle.Turtle()
n.speed(0)  # Set the drawing speed to the fastest

# --- 1. Draw the Black Rounded Background ---

# Set up the pen
n.penup()
n.goto(-150, -200) # Starting position for the background
n.pendown()

# Set the fill color for the background
n.fillcolor("#221F1F") # A very dark grey, almost black
n.begin_fill()

# Draw the rounded rectangle shape
for _ in range(2):
    n.forward(300)
    n.circle(20, 90) # Creates a rounded corner
    n.forward(400)
    n.circle(20, 90)

n.end_fill() # Complete the fill for the background

# --- 2. Draw the Red "N" Logo ---

# Hide the turtle icon for a cleaner look
n.hideturtle()

# Part A: Draw the left vertical bar of the "N"
n.penup()
n.goto(-80, -125)
n.pendown()
n.setheading(110) # Set the initial angle
n.color("#B81D24") # Darker red for the "shadow"
n.fillcolor("#E50914") # Main Netflix red
n.begin_fill()
n.forward(250)
n.setheading(0)
n.forward(50)
n.setheading(290)
n.forward(250)
n.setheading(180)
n.forward(50)
n.end_fill()

# Part B: Draw the right vertical bar of the "N"
n.penup()
n.goto(20, 125)
n.pendown()
n.setheading(290)
n.begin_fill()
n.forward(250)
n.setheading(180)
n.forward(50)
n.setheading(110)
n.forward(250)
n.setheading(0)
n.forward(50)
n.end_fill()

# Part C: Draw the diagonal bar of the "N"
n.penup()
n.goto(-80, -125)
n.pendown()
n.setheading(290)
n.begin_fill()
n.forward(250)
n.setheading(20)
n.forward(55)
n.setheading(110)
n.forward(250)
n.setheading(200)
n.forward(55)
n.end_fill()


# Keep the window open until it's manually closed
turtle.done()