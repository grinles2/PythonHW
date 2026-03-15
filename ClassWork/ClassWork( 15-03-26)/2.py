user_num = float(input('Сумма в долларах-> '))
exch = float(input('Курс-> '))
try:
    result = user_num * exch
    print(f'{user_num} * {exch} = {result}')

    if exch == 0:
        print('Курс не может быть 0')

except ValueError:
    print('Неправильное число')

finally: 
    print(f'--------ЧЕК--------\n Доллары: {user_num} \n Обмен: {result} \n Коммисия: 0 \n Кассир: ERROR 503')