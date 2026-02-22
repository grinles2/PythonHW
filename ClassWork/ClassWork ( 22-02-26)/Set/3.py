
word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

word1 = word1.lower()
word2 = word2.lower()

word1 = word1.strip()
word2 = word2.strip()

if sorted(word1) == sorted(word2):
    print("True")
else:
    print("False")