import math


class Circle:    # пr^2
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius


class Rectangle: # l*w
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * (self.a + self.b)


class Triangle: # 1/2 * L * H
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimetr(self):
        return self.a + self.b + self.c


while True:
    print("\n1. Круг")
    print("2. Прямоугольник")
    print("3. Треугольник")
    print("0. Выход")

    choice = input("Выберите фигуру: ")

    if choice == "1":
        r = float(input("Введите радиус: "))
        c = Circle(r)
        print("Площадь:", c.area())
        print("Периметр:", c.perimetr())

    elif choice == "2":
        a = float(input("Введите сторону 1: "))
        b = float(input("Введите сторону 2: "))
        r = Rectangle(a, b)
        print("Площадь:", r.area())
        print("Периметр:", r.perimetr())

    elif choice == "3":
        a = float(input("Введите сторону 1: "))
        b = float(input("Введите сторону 2: "))
        c = float(input("Введите сторону 3: "))
        t = Triangle(a, b, c)
        print("Площадь:", t.area())
        print("Периметр:", t.perimetr())

    elif choice == "0":
        exit()
    else:
        print("Броу опция не найденна бро")