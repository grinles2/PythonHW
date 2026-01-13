num1 = float(input("Введите первое число---->"))
num2 = float(input("Введите второе число---->"))
num3 = float(input("Введите третье число---->"))



ans = input("Что вы хотите сделать с числами? "
            "1-Сумма 2-Разница ")

if ans == "1":
    result = (num1 + num2+num3 )
    print("Сумма:",result)


elif ans == "2":
    result = (num1 - num2 - num3)
    print("Разница:", result)

else:
    print("Команда не распознанна")

