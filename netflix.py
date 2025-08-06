import turtle
import colorsys

window = turtle.setup(height=700, width=700)
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(10)
t.speed(5)

num = 36
hs = 0
turtle.goto(-60, 0)

for i in range(20):

    color = colorsys.hsv_to_rgb(hs, 1, 1)
    hs += 1 / num
    t.pencolor(color)

    t.circle(105, 103)
    t.backward(98)
    t.right(60)
    t.circle(70, 68)
    t.left(87)
    t.backward(108)
    t.forward(150)