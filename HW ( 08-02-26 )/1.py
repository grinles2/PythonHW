def result(a, b):
    if b == 0:
        return a
    return result(b, a % b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Ответ", result(a, b))