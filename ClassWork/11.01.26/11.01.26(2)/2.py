import math

diameter = float(input("Диаметр Круга: "))
choice = input("(1 - Площадь, 2 - Периметр): ")

radius = diameter / 2

if choice == "1":
    area = math.pi * radius ** 2
    print("Ответ:", area)
elif choice == "2":
    perimeter = 2 * math.pi * radius
    print("Ответ:", perimeter)
else:
    print("Брат в каталоге такого нэту")
