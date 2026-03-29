'''

Завдання 1
Напишіть програму, яка малює три базові фігури поруч одна з одною, не з'єднуючи їх лініями (використовуйте penup() та pendown()):
Квадрат (червоного кольору).
Рівносторонній трикутник (зеленого кольору).
П'ятикутник (синього кольору).


'''


import turtle as t

t.pensize(3)

t.color("red")
t.penup()
t.goto(-200, 0)
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


t.color("green")
t.forward(150)
t.pendown()
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.penup()


t.color("blue")
t.forward(150)
t.pendown()
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.forward(100)
t.right(72)
t.penup()

t.done()