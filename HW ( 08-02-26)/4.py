'''

Завдання 4
Користувач вводить рядок і два символи. Видаліть із рядка всі
символи між першим входженням першого символу і першим
входженням другого символу, включаючи самі символи. Виведіть
результат.


'''

line = input("введите текст -> ")
symbols = input("введите два символа (CЛИТНО) -> ")

if len(symbols) < 2:
    print("вы ввели не два символа")
    exit()

first_symbol = symbols[0]
second_symbol = symbols[1]

if first_symbol not in line or second_symbol not in line:
    print("символы не найдена")
    exit()


start = line.find(first_symbol)
end = line.find(second_symbol)

result = line[:start] + line[end + 1:]

print("Ответ:")
print(result)





