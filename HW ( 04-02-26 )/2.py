print("меню фигур")
print("1 - а")
print("2 - б")
print("3 - в")
print("4 - г")
print("5 - д")
print("6 - е")
print("7 - ж")
print("8 - з")
print("9 - и")
print("10 - к")

symbol = "*"
space = " "
choice = int(input("Выберите фигуру: "))


if choice == 1:
    print("Фигура А")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(space * i + symbol * (size - i))

elif choice == 2:
    print("Фигура Б")
    size = int(input("Напишите ширину: "))
    for i in range(1, size + 1):
        print(symbol * i)

elif choice == 3:
    print("Фигура В")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(space * i + symbol * (size - i))


elif choice == 4:
    print("Фигура Г")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(space * (size - i - 1) + symbol * (i + 1))


elif choice == 5:
    print("Фигура Д")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(symbol * (i + 1) + space * (size - i - 1))
    for i in range(size):
        print(space * i + symbol * (size - i))


elif choice == 6:
    print("Фигура Е")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(symbol * size)

elif choice == 7:
    print("Фигура Ж")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(symbol * (size - i) + space * i)


elif choice == 8:
    print("Фигура З")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(space * (size - i - 1) + symbol * (i + 1))
    for i in range(size):
        print(space * i + symbol * (size - i))


elif choice == 9:
    print("Фигура И")
    size = int(input("Напишите ширину: "))
    while size > 0:
        print(symbol * size)
        size -= 1


elif choice == 10:
    print("Фигура К")
    size = int(input("Напишите ширину: "))
    for i in range(size):
        print(symbol * size)

else:
    print("Неверный выбор")
