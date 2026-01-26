num_1 = int(input("Начало диапазона: "))
num_2 = int(input("Конец диапазона: "))

if num_1 > num_2:
    num_1, num_2 = num_2, num_1

current = num_1
product = 1
found = False

while True:
    if current > num_2:
        break

    if current % 4 == 0 and current % 6 != 0:
        product *= current
        found = True

    current += 1

if found:
    print("Сумма умноженных чисел:", product)
else:
    print("Нету чисел в диапазоне на 4/6")
