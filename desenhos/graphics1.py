import turtle

t = turtle.Turtle()

# screen
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()

a = 0
for b in range(210):
	t.forward(a)
	t.right(b)
	a+=3
	t.hideturtle()

turtle.done()