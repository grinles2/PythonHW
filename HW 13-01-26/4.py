m = float(input("Введите кол.во метров ----> "))

ans = input(
    "Во что конвертировать метры?\n"
    "1 - В одну из единиц (мили, дюймы, ярды)\n"
    "2 - Во все сразу (мили, дюймы, ярды)\n"
    "3 - В километры и сантиметры\n"
    "---->: "
)

if ans == "1":
    unit = input(
        "Выберите единицу:\n"
        "1 - Мили\n"
        "2 - Дюймы\n"
        "3 - Ярды\n"
        "---->: "
    )

    if unit == "1":
        result = m * 0.000621371
        print(m, "метров =", result, "миль")

    elif unit == "2":
        result = m * 39.3701
        print(m, "метров =", result, "дюймов")

    elif unit == "3":
        result = m * 1.09361
        print(m, "метров =", result, "ярдов")

    else:
        print("Неверный выбор")

elif ans == "2":
    mile = m * 0.000621371
    inch = m * 39.3701
    yard = m * 1.09361

    print("Мили:", mile)
    print("Дюймы:", inch)
    print("Ярды:", yard)

elif ans == "3":
    km = m * 0.001
    cm = m * 100

    print("Км:", km)
    print("См:", cm)

else:
    print("Команда не распознана")
