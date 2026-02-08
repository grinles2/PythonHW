text = input("введите текст: ")

result = ""
i = len(text) - 1

while i >= 0:
    result += text[i]
    i -= 1

print("строка наоборот:", result)
