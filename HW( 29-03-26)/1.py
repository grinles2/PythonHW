
'''

Опис: У багатьох іграх чи сервісах ім'я користувача, яке він
хоче взяти, вже зайняте. Напишіть програму, яка просить
користувача ввести базове ім'я (наприклад, vlad), а потім
генерує 3 варіанти унікальних нікнеймів на його основі.
Вимоги:
● Імпортувати модулі random та string.
● Варіант 1 (Цифровий): Додає до імені випадкове число
від 100 до 9999 (використати random.randint). Приклад:
vlad7391
● Варіант 2 (Літерний): Додає до імені розділювач
(випадково вибраний з string.punctuation, але
обмежтеся лише _, ., -), а потім 3 випадкові літери
англійського алфавіту (використати
string.ascii_lowercase та random.choices). Приклад:
vlad_xqp
● Варіант 3 (Елітний): Робить першу літеру імені великою
(метод рядків), додає випадковий префікс (наприклад,
Pro, Super, Ultra — вибрати через random.choice зі
створеного списку) та перемішує ім'я з 2 випадковими
цифрами.
● Вивести всі 3 варіанти у консоль красиво.

'''


import random
import string
import time


def gui():
    print("Введите свой никнейм")
    user_nick = input(": ")
    print("Ожидайте идёт загрузка..")
    time.sleep(2)
    print("Ожидайте идёт загрузка...")
    time.sleep(2)
    print("Данный никнейм уже занят")
    time.sleep(1)
    nickname(user_nick)


def nickname(user_nick):



    options = []

    def option1():
        number = random.randint(100, 9999)
        username = user_nick + str(number)
        options.append(username)


    option1()

    def option2():

        list_punctuation = "_.-"
        punctuation = random.choice(list_punctuation)

        letters = string.ascii_letters
        letters = ''.join(random.choices(letters, k=3))

        username = user_nick + punctuation + letters
        options.append(username)

    option2()

    def option3():
        prefix = ["Super", "Pro", "Max", "Mini", "Galaxy", "Ultra", "Expert", "YT"]
        prefix = random.choice(prefix)

        username = user_nick.lower()
        username = user_nick.capitalize()
        username = username + prefix
        options.append(username)

    option3()

    def print_options():
        #print(len(options))
        line = "=" * 50
        print(f"Вот доступные вам варианты: \n{line} \n{options[0]} \n{options[1]} \n{options[2]} ")
        print("Какой хотите использывать?")

        nick = input(": ")
        exit()


    print_options()






if __name__ == '__main__':
    gui()