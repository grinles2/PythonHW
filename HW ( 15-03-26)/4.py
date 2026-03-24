'''

Завдання 4
Напишіть програму, яка запитує в користувача число й обчислює
його квадратний корінь.
● У блоці try перетворіть введення в число і перевірте, що воно не
від'ємне.
● Якщо число від'ємне, згенеруйте виняток (raise Exception("Не
можна обчислити квадратний корінь від'ємного числа")).
● Перехопіть ValueError і згенероване виключення, виведіть
відповідне повідомлення.
● У блоці finally виведіть повідомлення про завершення
обчислень.


'''

import math


def calc():
    try:
        user_input = input("Введите число: ")

        number = float(user_input)

        if number < 0:
            raise Exception(f"Нельзя получить корень из числа {number}")

        result = math.sqrt(number)
        print(f"Результат:{result}")

    except ValueError:
        print("Вы ввели не число")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        print("КОд завершен.")

calc()
