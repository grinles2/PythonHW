'''

Напишіть програму, яка запитує в користувача три рядки і записує їх
у файл data.txt, кожен рядок має бути записаний на новому рядку.


'''

lines = ""

def add(line1, line2, line3):
    try:
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(line1 + "\n")
            f.write(line2 + "\n")
            f.write(line3 + "\n")
    except FileNotFoundError:
        file = open("data.txt", "a")
        file.close()
        add(line1, line2, line3)


def user():
    print("Напишите рядок 1")
    line1 = input(": ")
    print("Напишите рядок 2")
    line2 = input(": ")
    print("Напишите рядок 3")
    line3 = input(": ")
    add(line1, line2, line3)

if __name__ == '__main__':
    user()
