file_path = "data.txt"
backup_path = "backup.txt"
lines = []
def read():
    global lines
    try:
        with open(file_path, "r") as a:
            lines = a.readlines()
    except FileNotFoundError:
        print("Файл не существует")
        file = open(file_path, "a")
        file.close()


def write():
    global lines
    with open(backup_path, "w") as i:
        i.writelines(lines)

if __name__ == "__main__":
    read()
    write()
