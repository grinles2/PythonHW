'''

Створіть програму, яка із введеного тексту створює "зворотний
текст" (перевертає текст на рівні слів, а не символів). Наприклад, "я
люблю Python" перетворюється на "Python люблю я".

'''

raw_text = input("Введите текст -> ")

words = raw_text.split()

reversed = words[::-1]
reversed_text = " ".join(reversed)

print("Ответ:")
print(reversed_text)
