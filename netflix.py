import turtle as n

# Set up the screen
n.speed(0)
n.hideturtle()
n.bgcolor('white')

# Draw the black rounded square background
n.penup()
n.goto(-200, 200)
n.pendown()
n.fillcolor('#221F1F')
n.begin_fill()
for _ in range(2):
    n.forward(400)
    n.circle(-10, 90)
    n.forward(400)
    n.circle(-10, 90)
n.end_fill()

# Draw the left vertical bar of the "N"
n.penup()
n.goto(-75, -125)
n.pendown()
n.color('#B81D24')
n.fillcolor('#E50914')
n.begin_fill()
n.left(20)
n.forward(300)
n.left(160)
n.forward(50)
n.left(20)
n.forward(300)
n.left(160)
n.forward(50)
n.end_fill()

# Draw the right vertical bar of the "N"
n.penup()
n.goto(75, 125)
n.pendown()
n.begin_fill()
n.right(200)
n.forward(300)
n.right(160)
n.forward(50)
n.right(20)
n.forward(300)
n.right(160)
n.forward(50)
n.end_fill()

# Draw the diagonal bar of the "N"
n.penup()
n.goto(-75, -125)
n.pendown()
n.color('#E50914')
n.begin_fill()
n.left(20)
n.forward(300)
n.left(70)
n.forward(175)
n.left(110)
n.forward(300)
n.left(70)
n.forward(175)
n.end_fill()

# Keep the window open
n.done()