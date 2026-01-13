num1 = float(input("Введите первое число ----> "))
num2 = float(input("Введите второе число ----> "))

operation = input(
    "Выберите операцию:\n"
    "1 - Сложение \n"
    "2 - Вычитание \n"
    "3 - Умножение \n"
    "4 - Деление \n"
    "5 - Остаток от деления \n"
    "6 - Возведение в степень \n"
    "---->: "
)

if operation == "1":
    result = num1 + num2
    print("Результат:", result)

elif operation == "2":
    result = num1 - num2
    print("Результат:", result)

elif operation == "3":
    result = num1 * num2
    print("Результат:", result)

elif operation == "4":
    if num2 == 0:
        print("Дядя какой на 0 делить тютю шо ли")
    else:
        result = num1 / num2
        print("Результат:", result)

elif operation == "5":
    if num2 == 0:
        print("Дядя какой на 0 делить тютю шо ли")
    else:
        result = num1 % num2
        print("Результат:", result)

elif operation == "6":
    result = num1 ** num2
    print("Результат:", result)

else:
    print("Команда не распознана")
