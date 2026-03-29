import turtle as t

t.pensize(3)


t.color("brown")
t.penup()
t.goto(-50, -50)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.penup()


t.color("red")
t.fillcolor("orange")
t.goto(-50, 50)
t.pendown()
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()
t.penup()

t.done()