while True:
    num1 = int(input("напишите num1: "))
    num2 = int(input("напишите num2: "))

    if num1 == num2:
        print("числа равны:", num1)
        break

    if num1 < num2:
        current = num1
        while current <= num2:
            print(current)
            current += 1
    else:
        current = num1
        while current >= num2:
            print(current)
            current -= 1

    break
