
translations = {
    "hi": "привіт",
    "cat": "кіт",
    "dog": "собака",
    "how are you": "як справи",
    "bye": "до побачення"
}

word = input("Введите слово на англ языке --> ")

word = word.lower()

if word in translations:
    print(f"Переклад: {translations[word]}")
else:
    print("Не найден перевод")