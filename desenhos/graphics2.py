import turtle

t = turtle.Turtle()

# screen
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.speed(0)

for n in range(73):
    for i in range(4):
        t.forward(80)
        t.left(90)
    t.left(5)
t.hideturtle()


turtle.done()
