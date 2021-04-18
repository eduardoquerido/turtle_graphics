import turtle


def star():
    ts = turtle.Screen()
    ts.setup(600, 600)
    ts.bgcolor("black")

    spiral = turtle.Turtle()

    spiral.speed(10)

    col = ["yellow", "pink", "white", "violet"]

    c = 0

    for i in range(50):
        spiral.forward(i * 10)
        spiral.right(144)
        spiral.color(col[c])
        if c == 3:
            c = 0
        else:
            c += 1

    turtle.done()


if __name__ == "__main__":
    star()
