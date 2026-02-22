'''


Завдання 3
Є словник курсів:
 rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
Користувач вводить валюту та суму у гривнях, а програма виводить еквівалент у вибраній валюті.


'''

rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
print("Валюты: USD, EUR, PLN")
currency = input("Введите валюту-->")

if currency not in rates:
    print("Мы такой не принимаем")
else:
    amount_uah = float(input("Введите сумму в гривнах --> "))
    converted = amount_uah / rates[currency]
    print(f"{amount_uah} грн = {converted:.2f} {currency}")