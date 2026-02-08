text = input("введите текст: ")

words = text.split()

longest_word = ""

for word in words:

    if len(word) > len(longest_word):

        longest_word = word
    else

print("Самое большое слово:", longest_word)
