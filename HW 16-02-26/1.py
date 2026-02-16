
'''

Користувач із клавіатури вводить список цілих чисел. Необхідно реалізувати циклічний
зсув списку вправо на N позицій. Результат вивести на екран.
Приклад:
● Вхідні дані:
○ Список чисел: 1, 2, 3, 4, 5.
○ Число позицій N: 2.
● Очікуваний результат:
○ Зсунутий список: [4, 5, 1, 2, 3].

'''
top_line = "-----------------Отладка---------------"
bottom_line = "-------------------------------------"
#num = "1 2 3 4 5"


num = str(input("Напишите числа через пробел: "))    # если 1 2 3 4 5
#space = 2
space = int(input("Напишите кол.во отступов вправо: ")) # если тут 2


numbers = num.split(' ')
print(top_line)
print(f'Список: {numbers}')  # ['1', '2', '3', '4', '5']
length = len(numbers)
print(f'Длина: {length}')

if num >= "0":
    print(f'Отступов: {space}')
    print(bottom_line)


    if length <= space:
        space = space % length
        print(f'Сдвиг: {space}')

        result = numbers[-space:] + numbers[:-space]
        print("\tРезультат")
        print(', '.join(result))




    else:
        result = numbers[-space:] + numbers[:-space]
        print("\tРезультат")
        print(', '.join(result))

else:
    exit()
