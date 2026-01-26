num_1 = int(input("num1: "))
num_2 = int(input("num2: "))

current = num_1

while True:
    if current > num_2:
        break

    if current % 3 == 0 and current % 5 == 0:
        print("Fizz Buzz")
    elif current % 3 == 0:
        print("Fizz")
    elif current % 5 == 0:
        print("Buzz")
    else:
        print(current)

    current += 1
