text = input("напишите текст: ")
symbol = input("символ для поиска: ")

count = 0
i = 0

while i < len(text):
    if text[i] == symbol:
        count += 1
    i += 1

print("Символ", symbol, "встречается", count, "раз(а)")
