start = int(input("Начало диапазон: "))
end = int(input("Конец диапазона: "))
step = int(input("Шаг: "))

order = input("Введите порядок (1 — прямой, 2 — обратный): ")

if order == "1":
    current = start
    while True:
        if current > end:
            break
        print(current)
        current += step


elif order == "2":
    current = end
    while True:
        if current < start:
            break
        print(current)
        current -= step

else:
    print("брат 1 или 2, тебя на математике цифрам не учили?")
