'''

Завдання 3
Напишіть програму, яка реалізує керування замовленнями
інтернет-магазину за допомогою текстового файлу orders.txt.
Програма повинна надавати користувачеві меню з можливими діями:
● Додати нове замовлення – користувач вводить номер
замовлення, назву товару, кількість і ціну, після чого дані
додаються у файл.
● Переглянути всі замовлення – програма завантажує і
відображає всі замовлення, збережені у файлі.
● Пошук замовлення за номером – користувач вводить номер
замовлення, програма виводить інформацію про нього.
● Оновити замовлення – користувач вводить номер замовлення,
програма дає змогу оновити кількість і ціну товару.
● Видалити замовлення – користувач вводить номер
замовлення, і програма видаляє його з файлу, якщо він існує.
● Вихід – завершує виконання програми.


'''

greeting = "1 - Все Заказы\n 2- Новый Заказ\n 3 - Удалить Заказ\n 4- Трек по номеру \n 5- Обновить Заказ \n 6 -Выход "


def gui():
    while True:
        print("\n" + "-" * 20)
        print(greeting)

        choice = input(": ")

        if choice == "1":
            show_orders()
        elif choice == "2":
            new_order()
        elif choice == "3":
            delete_order()
        elif choice == "4":
            search()
        elif choice == "5":
            update_order()
        elif choice == "6":
            break
        else:
            print("Опция не найденна")


def show_orders():
    try:
        with open("orders.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("Вы ничего не заказали")
                return

            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("Файл не существует")


def new_order():
    order_id = input("ID: ")
    name = input("Название: ")
    quantity = input("Кол.во: ")
    price = input("Цена: ")

    with open("orders.txt", "a", encoding="utf-8") as f:
        f.write(f"{order_id}|{name}|{quantity}|{price}\n")

    print("Заказ принят")


def search():
    order_id = input("ID: ")

    try:
        with open("orders.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(order_id + "|"):
                    print("Результат:", line.strip())
                    return
        print("Заказ не найден")
    except FileNotFoundError:
        print("Файл не найден")


def delete_order():
    order_id = input("Введіть ID: ")

    try:
        with open("orders.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("orders.txt", "w", encoding="utf-8") as f:
            found = False
            for line in lines:
                if not line.startswith(order_id + "|"):
                    f.write(line)
                else:
                    found = True

        if found:
            print("Удалено")
        else:
            print("Не найденно")

    except FileNotFoundError:
        print("Файла не существует")


def update_order():
    order_id = input("ID: ")

    try:
        with open("orders.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("orders.txt", "w", encoding="utf-8") as f:
            found = False
            for line in lines:
                if line.startswith(order_id + "|"):
                    parts = line.strip().split("|")

                    new_quantity = input("Кол.Во: ")
                    new_price = input("Цена: ")

                    f.write(f"{parts[0]}|{parts[1]}|{new_quantity}|{new_price}\n")
                    found = True
                else:
                    f.write(line)

        if found:
            print("Готово")
        else:
            print("Заказ не найден")

    except FileNotFoundError:
        print("Файл не существует")


if __name__ == "__main__":
    gui()