numbers = input("введите числа колекции через ПРОБЕЛ: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

index = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        index.append(i)
    else:
        exit()
print("Ответ:",index)
