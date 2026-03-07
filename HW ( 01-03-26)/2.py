'''

Напишіть функцію, яка приймає два числа як параметри і відображає
всі парні числа між ними.


'''


def difference(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)

num1 = int(input("введите число 1: "))
num2 = int(input("введите число 2: "))

difference(num1, num2)