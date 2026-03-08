

num1 = int(input("Впишите число: "))
num2 = int(input("Впишите число:"))


def recursion(base, expo):
    if expo == 0:
        return 1
    elif expo > 0:
        return base * recursion(base, expo - 1)
    else:
        return 1 / recursion(base, -expo)


print(recursion(num1, num2))
