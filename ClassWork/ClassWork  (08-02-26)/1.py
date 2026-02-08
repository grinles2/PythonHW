text = input("Введіть рядок: ")

l = 0
d = 0

for i in text:
    if i.isalpha():
        l += 1
    elif i.isdigit():
        d += 1

print("Кількість букв:", l)
print("Кількість цифр:", d)