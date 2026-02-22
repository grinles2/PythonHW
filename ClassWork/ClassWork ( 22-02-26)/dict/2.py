'''

Завдання 2
Користувач вводить текст у консоль. Програма повинна порахувати скільки разів кожне слово зустрічається у тексті (ігноруючи регістр) та вивести на екран результат.

'''
user_text = input("Введите текст --> ")
user_text = user_text.lower()
words = user_text.split()

word_count = {}

for word in words:
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print("Кол.во слов:")
for word, count in word_count.items():
    print(f"{word} : {count}")