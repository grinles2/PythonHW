num = input("Введите трехзначное число ----> ")

if len(num) == 3 and num[0] == num[1] == num[2]:
    print("Всі цифри однакові")
else:
    print("Цифри різні")
