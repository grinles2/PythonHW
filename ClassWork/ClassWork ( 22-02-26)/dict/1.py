'''

Завдання 1
Створити застосунок “Контактна книжка”. Меню реалізувати через консоль. Функції меню:
додати контакт
видалити контакт
змінити контакт
відобразити всі контакти


'''


contacts = {}

while True:
    print("\n1 - Добавить Контакт")
    print("2 - Удалить Контакт")
    print("3 - Изменить Контакт")
    print("4 - Список Контактов")


    user_choice = int(input("Категория ---> "))

    if user_choice == 1:
        name = input("Введите имя: ")
        phone = input("Введите номер: ")

        if name in contacts:
            print("контакт уже есть")
        else:
            contacts[name] = phone
            print("контакт добавлен")


    elif user_choice == 2:
        name = input("Введите имя: ")

        if name in contacts:
            del contacts[name]
            print("Готово")
        else:
            print("Такого нету")

    elif user_choice == 3:
        name = input("Введите имя: ")

        if name in contacts:
            new_phone = input("Введите новый номер: ")
            contacts[name] = new_phone
            print("Контакт изменен")
        else:
            print("Контакта нету")

    elif user_choice == 4:
        if contacts:
            print("\nСписок контактов:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("Контактов нет.")



    else:
        print("Команда не распознана!")
        print("*" * 50)