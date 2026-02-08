change_word = ["Samsung", "The", "Best"]

initial_text = "Samsung is The Best phone manufacturer"
print(f'{initial_text}')

raw_text = input("Введите текст: ")

words = raw_text.split(" ")
print(f'Отладка 1: {words}')

result = []

for word in words:
    if word.lower() in [w.lower() for w in change_word]:
        result.append(word.upper())
    else:
        result.append(word)

final_text = " ".join(result)
print("Результат:")
print(final_text)
