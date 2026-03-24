'''

Завдання 1
Напишіть програму, яка запитує в користувача два числа і виводить
результат ділення першого числа на друге.
● У блоці try отримайте числа, перетворіть їх у тип float і
виконайте ділення.
● Перехопіть ValueError, якщо введене значення не є числом, і
ZeroDivisionError, якщо відбувається ділення на нуль.
● У блоці finally виведіть повідомлення про завершення операції.

'''

try:
    result = 0.00
    user_num1 = input("Введите первое число-> ")
    user_num2 = input("Введите второе число-> ")
    user_num2 = float(user_num2)
    user_num1 = float(user_num1)

    result = user_num1 / user_num2
except ZeroDivisionError:
    print("Ответ: деление на 0, невозможно")
except ValueError:
    print("Вы ввели не число")
except Exception as ex:
    print(ex)
finally:
    print(f"Результат: {result} ")