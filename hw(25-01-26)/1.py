num_1 = int(input("num1: "))
num_2 = int(input("num2: "))

current = num_1

while True:
    if current > num_2:
        exit("Брат то не старт диапазона")

    elif current % 7 == 0:
        print(current)

    current += 1
