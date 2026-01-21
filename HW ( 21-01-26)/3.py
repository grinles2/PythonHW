import time

print("Здравствуйте")
print("Приветствую вас в нашем ресторане")
time.sleep(1)

client = input("Вы уже были у нас? y/n: ")

if client == "y":
    loyal = True
else:
    loyal = False

# TODO Сделать переменные под каждое блюдо
balance = 0
discount_percent = 0
snacks = False
main_course = False
deserts = False
salad = False
soup = False
chicken = False
fish = False
ice_cream = False
fruits = False
free_drink = False
dessert_discount = 0


while True:
    print("\nВыберите категорию:")
    print("1 — Закуски")
    print("2 — Основное блюдо")
    print("3 — Десерт")
    print("0 — Принести еду")

    menu = int(input("Ваш выбор: "))

    if menu == 0:
        break

    if menu == 1 and not snacks:
        snacks = True
        print("\n1) Салат — 5$")
        print("2) Суп — 7$")
        order1 = int(input("Ваш выбор: "))

        if order1 == 1:
            salad = True
            balance += 5
        elif order1 == 2:
            soup = True
            balance += 7

    elif menu == 1 and snacks:
        print("Сорянчик, закуски кончились")

    elif menu == 2 and not main_course:
        main_course = True
        print("\n1) Курица — 10$")
        print("2) Рыба — 12$")
        order2 = int(input("Ваш выбор: "))

        if order2 == 1:
            chicken = True
            balance += 10
        elif order2 == 2:
            fish = True
            balance += 12

    elif menu == 2 and main_course:
        print("У вас в меню уже выбранно главное блюдо, плз выбери другое")

    elif menu == 3 and not deserts:
        deserts = True
        print("\n1) Мороженое — 3$")
        print("2) Фрукты — 4$")
        order3 = int(input("Ваш выбор: "))

        if order3 == 1:
            ice_cream = True
            balance += 3
        elif order3 == 2:
            fruits = True
            balance += 4

    elif menu == 3 and deserts:
        print("Братик, не слипнеться?")

    else:
        print("Э вася ты читать научись")




if snacks and main_course and deserts:
    discount_percent += 10


if balance > 20:
    discount_percent += 15


if loyal:
    discount_percent += 5


if soup and fish:
    dessert_discount = 2


if chicken and ice_cream:
    free_drink = True



# TODO сделать конец оформления
print("\nЧЕК:")
print("Сумма до скидки:", balance, "$")


if dessert_discount > 0:
    balance -= dessert_discount
    print("Поздравляю с скидкой на 2$ к десерту")



if discount_percent > 0:
    discount_amount = balance * discount_percent / 100
    balance -= discount_amount
    print("% скидки:", discount_amount)


if free_drink:
    print("ваш бесплатный чай за счёт заведения")



print("вы должны:", round(balance, 2), "$")
