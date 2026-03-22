'''

Напишіть програму, яка реалізує керування музичною колекцією за допомогою текстового файлу music_collection.txt. Програма повинна надавати користувачеві меню з можливими діями:
Додати новий альбом — користувач вводить назву альбому, виконавця і рік випуску, програма додає їх у файл.
Переглянути всю колекцію — програма завантажує і відображає всі альбоми, збережені у файлі.
Пошук альбомів за виконавцем — користувач вводить ім'я виконавця, програма виводить усі альбоми цього виконавця.
Видалити альбом — користувач вводить назву альбому, і програма видаляє його з файлу, якщо він існує.
Вихід — завершує виконання програми.


'''

def cli():

    global file_path
    file_path = "music_collection.txt"
    while True:
        print("\n1 - Добавить альбом")
        print("2 - Просмотреть коллекцию")
        print("3 - Поиск по исполнителю")
        print("4 - Удалить альбом")
        print("5 - Выход")

        option = input("Выберите: ")

        if option == "1":
            add()
        elif option == "2":
            view()
        elif option == "3":
            search()
        elif option == "4":
            delete()
        elif option == "5":
            logout()
        else:
            print("Неверный ввод")


def add():
    album = input("Название альбома: ")
    artist = input("Исполнитель: ")
    year = input("Год: ")

    with open(file_path, "a") as file:
        file.write(f"{album} | {artist} | {year}\n")

    print("Альбом добавлен")


def view():
    try:
        with open(file_path, "r") as file:
            data = file.readlines()

            if not data:
                print("Вы нчего не добавили")
                return

            print("\nКоллекция:")
            for line in data:
                print(line.strip())

    except FileNotFoundError:
        print("Файл не найден")


def search():
    artist_name = input("Введите автора: ")

    try:
        with open(file_path, "r") as file:
            found = False

            for line in file:
                if artist_name.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print("Не найденно")

    except FileNotFoundError:
        print("Файл не существует")


def delete():
    album_name = input("Введите название: ")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            found = False

            for line in lines:
                if album_name.lower() not in line.lower():
                    file.write(line)
                else:
                    found = True

        if found:
            print("Альбом удалён")
        else:
            print("Альбом не найден")

    except FileNotFoundError:
        print("Файл не найден")


def logout():
    print("Программа завершена")
    exit()


if __name__ == '__main__':
    cli()