'''

Завдання 6
Реалізуйте функцію connect_to_server(), яка з використанням модуля
random випадковим чином або повертає повідомлення про успішне
підключення, або генерує виняток ConnectionError (за допомогою
raise ConnectionError("Помилка підключення")).
● В основному блоці try викличте функцію connect_to_server().
● Перехопіть ConnectionError у блоці except і виведіть
повідомлення "Не вдалося підключитися до сервера".
● У блоці finally виведіть повідомлення "Спробу завершено"

'''

import random

def connect_to_server():
    if random.choice([True, False]):
        return "Вы подключены"
    else:
        raise ConnectionError("Ошибка Подключения")

try:
    result = connect_to_server()
    print(result)
except ConnectionError:
    print("Не удалось подключится к серверу")
finally:
    print("Попытка отменена")
