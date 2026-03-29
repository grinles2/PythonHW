import turtle as t
import random

t.pensize(3)


def draw_square():
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.penup()


for i in range(36):
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r, g, b)
    draw_square()
    t.right(10)

t.done()