try:
    price = float(input("Введите цену-> "))
    discount = float(input("Введите % скидки-> : "))
    final_price = price - (price * discount / 100)

    print("Цена на кассе:", final_price)

except ValueError:
    print("Ошибка, введите только цифры")