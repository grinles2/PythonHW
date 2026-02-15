numbers = input("введите числа колекции через ПРОБЕЛ: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

new = []
for num in numbers:
    if new.count(num) == 0:
        new.append(num)
    else:
        exit()
print("Ответ:", new)