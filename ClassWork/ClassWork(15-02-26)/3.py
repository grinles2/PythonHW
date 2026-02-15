numbers = input("введите числа колекции (положительные числа) через ПРОБЕЛ: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

positive_sum = 0
for num in numbers:
    if num > 0:
        positive_sum += num
    else:
        exit("ну сказанно же ПОЛОЖИТЕЛЬНЫЕ")
print("сумма:", positive_sum)