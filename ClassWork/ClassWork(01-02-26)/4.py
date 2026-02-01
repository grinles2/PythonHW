import random
attempts = 0
random_number = random.randint(1, 500)
print(random_number)


while True:

    user_num = int(input("угадайте число 1-500: "))

    if user_num == random_number:
        print(f'Попыток использованно:{attempts}')
        exit()

    elif user_num == 0:
        exit()

    else:
        attempts += 1

