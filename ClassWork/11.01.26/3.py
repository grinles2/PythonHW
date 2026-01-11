first = int(input("Введіть перше число: "))
second = int(input("Введіть друге число: "))

if first > second:
    print("Найбільше число:", first)
elif second > first:
    print("Найбільше число:", second)
else:
    print("Числа рівні:", first)