'''

Завдання 5
Напишіть функцію, яка перевіряє чи є число простим.
Число передається як параметр.
Якщо число просте потрібно повернути з методу true, інакше false.

'''

def common(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


num = int(input("введите числоr: "))

print(common(num))