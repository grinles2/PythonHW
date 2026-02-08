'''

Користувач вводить текст і набір символів. Видаліть з тексту всі
слова, що містять хоча б один з цих символів, і виведіть результат.

'''



raw_text = input("Введите текст -> ")
symbols = input("Введите символы, которые удалить из текста (через ,) -> ")

#
symbols_list = [s.strip().lower() for s in symbols.split(",")]
print(f'ОТЛАДКА: список = {symbols_list}')


words = raw_text.split()
print(f'ОТЛАДКА: вордс = {words}')


result_words = []

for word in words:
    word_lower = word.lower()

    if not any(sym in word_lower for sym in symbols_list):
        result_words.append(word)

result_text = " ".join(result_words)

print("Результат:")
print(result_text)

