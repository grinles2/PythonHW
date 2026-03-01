'''

Напишіть функцію, яка приймає два числа як параметр і відображає всі непарні числа між ними.


'''

def difference(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)
        else:
            exit()

num1 = int(input("Введите число--> "))
num2 = int(input("Введите число--> "))

difference(num1, num2)