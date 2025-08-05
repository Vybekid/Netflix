import turtle
import math # Import math for sqrt function

# --- Setup ---
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")  # Set screen to black for better contrast
t.speed(0)
t.hideturtle()

# --- 1. Draw the Black Rounded Background ---
t.penup()
t.goto(-175, -175)
t.pendown()
t.color("#141414")  # Netflix's dark grey, not pure black
t.begin_fill()
t.forward(350)
t.circle(25, 90)  # Creates smooth, rounded corners
t.forward(350)
t.circle(25, 90)
t.forward(350)
t.circle(25, 90)
t.forward(350)
t.circle(25, 90)
t.end_fill()

# --- 2. Draw the "N" Logo with Correct Overlaps ---

# Define properties for the N shapes
ANGLE = 22
HEIGHT = 275
WIDTH = 55
COLOR_BRIGHT = "#E50914"  # Main bright Netflix red
COLOR_DARK = "#B81D24"    # Darker red for the shadow/3D effect

# Draw the left bar FIRST (bright red)
t.penup()
t.goto(-120, -125)
t.pendown()
t.color(COLOR_BRIGHT)
t.begin_fill()
t.setheading(90)  # Make it a vertical bar
t.forward(HEIGHT)
t.setheading(0)
t.forward(WIDTH)
t.setheading(270)
t.forward(HEIGHT)
t.setheading(180)
t.forward(WIDTH)
t.end_fill()

# --- Corrected middle "shadow" bar SECOND (dark red) ---
t.penup()
# Calculate the top-right corner of the left bar
start_x_left_bar = -120
start_y_left_bar = -125
top_right_x_left_bar = start_x_left_bar + WIDTH
top_right_y_left_bar = start_y_left_bar + HEIGHT

# Calculate the bottom-left corner of the right bar
start_x_right_bar = 65
start_y_right_bar = -125
bottom_left_x_right_bar = start_x_right_bar
bottom_left_y_right_bar = start_y_right_bar

# Move to the starting point for the diagonal bar (top-right of the left bar)
t.goto(top_right_x_left_bar, top_right_y_left_bar)
t.pendown()
t.color(COLOR_DARK)
t.begin_fill()

# Calculate the precise length of the diagonal segment
# This is the distance from (top_right_x_left_bar, top_right_y_left_bar)
# to (bottom_left_x_right_bar, bottom_left_y_right_bar)
diagonal_length = math.sqrt(
    (bottom_left_x_right_bar - top_right_x_left_bar)**2 +
    (bottom_left_y_right_bar - top_right_y_left_bar)**2
)

# Draw the first long side (down-right diagonal)
t.setheading(270 - ANGLE) # Tilt it diagonally
t.forward(diagonal_length)

# Draw the short side (width, perpendicular to the long side)
t.setheading(270 - ANGLE + 90) # Turn 90 degrees clockwise from current heading
t.forward(WIDTH)

# Draw the second long side (up-left diagonal, parallel to the first)
t.setheading(90 - ANGLE) # Go back up diagonally
t.forward(diagonal_length)

# Draw the last short side (width, back to the start)
t.setheading(90 - ANGLE + 90) # Turn 90 degrees clockwise from current heading
t.forward(WIDTH)
t.end_fill()
t.penup() # Lift pen after drawing

# --- Draw the right bar THIRD (bright red) ---
t.goto(65, -125)  # Position it to the right of the diagonal bar
t.pendown()
t.color(COLOR_BRIGHT)
t.begin_fill()
t.setheading(90)  # Make it a vertical bar
t.forward(HEIGHT)
t.setheading(0)
t.forward(WIDTH)
t.setheading(270)
t.forward(HEIGHT)
t.setheading(180)
t.forward(WIDTH)
t.end_fill()

# --- Finish ---
turtle.done()