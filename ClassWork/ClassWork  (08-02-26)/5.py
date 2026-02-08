text = input("напишите текст: ")
old_word = input("слово для замены: ")
new_word = input("новое слово: ")

result = ""
i = 0

while i < len(text):

    if text[i:i + len(old_word)] == old_word:

        result += new_word
        i += len(old_word)


    else:
        exit()

print("Ответ:", result)
