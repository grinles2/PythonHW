amount_usd = float(input("Доллары: "))

currency = input("Обменять что вам ? (EUR, GBP, UAH): ").upper()

rate = float(input(f"Введите курс {currency}: "))

if currency == "EUR":
    result = amount_usd * rate
    print(f"{amount_usd} USD = {result} EUR")


elif currency == "GBP":
    result = amount_usd * rate
    print(f"{amount_usd} USD = {result} GBP")


elif currency == "UAH":
    result = amount_usd * rate
    print(f"{amount_usd} USD = {result} UAH")


else:
    print("Ты шо брат мы не центральный банк. Такого нэту")
