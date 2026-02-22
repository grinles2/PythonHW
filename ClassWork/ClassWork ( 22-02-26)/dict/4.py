
translations = {
    "hi": "привіт",
    "cat": "кіт",
    "dog": "собака",
}

word = input("Введите слово на англ языке --> ")

word = word.lower()

if word in translations:
    print(f"Переклад: {translations[word]}")
else:
    print("Не найден перевод")