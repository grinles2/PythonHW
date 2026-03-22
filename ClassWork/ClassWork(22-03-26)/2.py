'''

Напишіть програму, яка читає вміст файлу data.txt,
 замінює кожну літеру на наступну в алфавіті (наприклад, a b, z a),
  а потім записує результат у encrypted.txt.

'''


def read():
    file_path = "data.txt"
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            encrypt(file_content)
    except FileNotFoundError:
        print("Файл не существует")
        file = open(file_path, "a")
        file.close()

def encrypt(file_content):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for list in file_content:
        if list.lower() in alphabet:
            c = alphabet.index(list.lower())
            a = (c + 1) % len(alphabet)
            b = alphabet[a]

            if list.isupper():
                b = b.upper()

            result += b
        else:
            result += list

    write(result)



def write(result):
    print(result)

    with open("encrypted.txt", "w") as i:
        i.writelines(result)

if __name__ == '__main__':
    read()