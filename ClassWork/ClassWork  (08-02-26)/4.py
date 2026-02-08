text = input("напишите текст: ")
word = input("напишите слово для поиска: ")

count = 0
i = 0

while i <= len(text) - len(word):
    if text[i:i + len(word)] == word:
        count += 1
        i += len(word)


    else:
        i += 1

print("cлово", word, "встречается", count, "раз")
