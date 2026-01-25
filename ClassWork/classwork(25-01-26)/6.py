while True:
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))

    if num1 > num2:
        print("Норм порядок")
        num1, num2 = num2, num1

    print("Четные числа:")

    now = num1
    while now <= num2:
        match now % 2:
            case 0:
                print(now)
            case _:
                pass
        now += 1

    print("Нечетные:")

    now = num2
    while now >= num1:
        if now % 2 != 0:
            print(now)
        else:
            pass
        now -= 1

    break
