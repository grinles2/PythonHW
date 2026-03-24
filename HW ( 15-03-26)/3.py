'''

Завдання 3
Попросіть користувача ввести дані про продажі через пробіл
(наприклад, "100 250 300").
● У блоці try перетворіть введений рядок на список чисел і
обчисліть загальну суму продажів.
● Перехопіть ValueError для некоректного введення.
● У блоці finally виведіть повідомлення про завершення обробки.

'''


try:
    sales_avg = 0
    userSales = input("Введите список продаж через пробел-> ")
    print(userSales.split(" "))
    sales_avg = userSales / len(userSales)
    print(sales_avg)
except ValueError:
    print("Вы ввели не число.")
except Exception as a:
    print(f"Ошибка->{a}")
finally:
    print(f"Результат-> {sales_avg}")