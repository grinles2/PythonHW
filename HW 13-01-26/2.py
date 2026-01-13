num1 = float(input("Введите первое число ----> "))
num2 = float(input("Введите второе число ----> "))
num3 = float(input("Введите третье число ----> "))

ans = input(
    "Что вы хотите сделать с числами?\n"
    "1 - Максимум из трех\n"
    "2 - Минимум из трех\n"
    "3 - Среднее арифметическое\n"
    "---->: "
)

if ans == "1":
    result = max(num1, num2, num3)
    print("Максимум из трёх:", result)

elif ans == "2":
    result = min(num1, num2, num3)
    print("Минимум из трёх:", result)

elif ans == "3":
    result = (num1 + num2 + num3) / 3
    print("Среднее арифметическое:", result)

else:
    print("Команда не распознана")
