user_choice = int(input("1 - Квадрат / 2 - Прямоугольник: "))
symbol = "*"

if user_choice == 1:
    side = int(input("Введите длину стороны квадрата: "))
    for i in range(side):
        print(symbol * (side * 2))


elif user_choice == 2:
    width = int(input("Введите ширину: "))
    height = int(input("Введите высоту: "))
    for i in range(height):
        print(symbol * width)

else:
    print("Неверный выбор")
