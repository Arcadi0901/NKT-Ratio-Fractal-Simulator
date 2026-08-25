from turtle import *
import math

screen = Screen()
v = 1


def main():
    global v
    screen.tracer(0)
    hideturtle()
    pu()
    clear()
    goto((-window_width() / 2), (window_height() / 2))
    canvas = screen.getcanvas()
    canvas.bind("<MouseWheel>", handle_scroll)
    screen.title("NKT fractal")
    screen.listen()
    game_loop()


def handle_scroll(event):
    global v
    if event.delta > 0:
        if v > 1 * (1.1**31) or math.isclose(v, 1 * (1.1**31)):
            v = 1
        else:
            v *= 1.1
    elif event.delta < 0:
        if v < 1 or math.isclose(v, 1):
            v = 1 * (1.1**31)
        else:
            v /= 1.1


def game_loop():
    global v
    clear()
    pensize(2 * (v * 0.1 + 0.9))
    goto((-window_width() / 2), (window_height() / 2) - 200)
    setheading(0)
    fprinttwo(3 * v)
    goto((-window_width() / 2), (window_height() / 2 - 21 * 21 * 3 * v) - 200)
    setheading(90)
    fprinttwo(3 * v)

    pensize(1)
    goto((-window_width() / 2), (window_height() / 2) - 200)
    setheading(0)
    printtwo(3 * (v / 21))
    goto((-window_width() / 2), (window_height() / 2 - 21 * 3 * v) - 200)
    setheading(90)
    printtwo(3 * (v / 21))

    goto(0, window_height() / 2 - 125)
    write(
        "Dimension=log(N)/log(1/r)=log(82)/log(21)≈1.447\n*scroll wheel to zoom",
        align="center",
        font=("Courier", 15, "italic"),
    )
    screen.update()
    screen.ontimer(game_loop, 16)
    screen.setup(width=1280, height=750)


def printone(k):
    pd()
    forward(2 * k)
    right(45)
    forward((8**0.5) * k)
    left(135)
    forward(2 * k)
    right(90)
    forward(2 * k)
    right(90)
    forward(6 * k)
    right(90)
    forward(2 * k)
    right(45)
    forward((8**0.5) * k)
    left(135)
    forward(2 * k)
    right(90)
    forward(2 * k)
    right(90)
    forward(6 * k)
    right(90)

    pu()
    forward(7 * k)
    pd()

    forward(2 * k)
    right(90)
    forward(2 * k)
    left(135)
    forward((8**0.5) * k)
    right(45)
    forward(2 * k)
    right(135)
    forward(3 * k / (0.5**0.5))
    left(90)
    forward(3 * k / (0.5**0.5))
    right(135)
    forward(2 * k)
    right(45)
    forward((8**0.5) * k)
    left(135)
    forward(2 * k)
    right(90)
    forward(2 * k)
    right(90)
    forward(6 * k)
    right(90)

    pu()
    forward(7 * k)
    pd()

    forward(6 * k)
    right(90)
    forward(2 * k)
    right(90)
    forward(2 * k)
    left(90)
    forward(4 * k)
    right(90)
    forward(2 * k)
    right(90)
    forward(4 * k)
    left(90)
    forward(2 * k)
    right(90)
    forward(2 * k)
    right(90)
    pu()
    forward(7 * k)


def forwardprintone(n1, K1):
    for i in range(int(n1)):
        printone(K1)
    forward((n1 - int(n1)) * 21 * K1)


def fprinttwo(fk2):
    forward(21 * fk2)
    pd()
    forwardprintone(1, fk2)
    right(45)
    forwardprintone((8**0.5), fk2)
    left(135)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(6, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(45)
    forwardprintone((8**0.5), fk2)
    left(135)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(5, fk2)
    forward(21 * fk2)
    right(90)

    pu()
    forward(7 * 21 * fk2)
    pd()

    forwardprintone(2, fk2)
    right(90)
    forwardprintone(2, fk2)
    left(135)
    forwardprintone((8**0.5), fk2)
    right(45)
    forwardprintone(2, fk2)
    right(135)
    forwardprintone(3 / (0.5**0.5), fk2)
    left(90)
    forwardprintone(3 / (0.5**0.5), fk2)
    right(135)
    forwardprintone(2, fk2)
    right(45)
    forwardprintone((8**0.5), fk2)
    left(135)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(6, fk2)
    right(90)

    pu()
    forward(7 * 21 * fk2)
    pd()

    forwardprintone(6, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(2, fk2)
    left(90)
    forwardprintone(4, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(4, fk2)
    left(90)
    forwardprintone(2, fk2)
    right(90)
    forwardprintone(2, fk2)
    right(90)
    pu()
    forward(7 * 21 * fk2)


def printtwo(k2):
    pd()
    forwardprintone(2, k2)
    right(45)
    forwardprintone((8**0.5), k2)
    left(135)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(6, k2)
    right(90)
    forwardprintone(2, k2)
    right(45)
    forwardprintone((8**0.5), k2)
    left(135)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(6, k2)
    right(90)

    pu()
    forward(7 * 21 * k2)
    pd()

    forwardprintone(2, k2)
    right(90)
    forwardprintone(2, k2)
    left(135)
    forwardprintone((8**0.5), k2)
    right(45)
    forwardprintone(2, k2)
    right(135)
    forwardprintone(3 / (0.5**0.5), k2)
    left(90)
    forwardprintone(3 / (0.5**0.5), k2)
    right(135)
    forwardprintone(2, k2)
    right(45)
    forwardprintone((8**0.5), k2)
    left(135)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(6, k2)
    right(90)

    pu()
    forward(7 * 21 * k2)
    pd()

    forwardprintone(6, k2)
    right(90)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(2, k2)
    left(90)
    forwardprintone(4, k2)
    right(90)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(4, k2)
    left(90)
    forwardprintone(2, k2)
    right(90)
    forwardprintone(2, k2)
    right(90)
    pu()
    forward(7 * 21 * k2)


if __name__ == "__main__":
    main()
    screen.mainloop()
