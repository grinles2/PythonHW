'''

Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть
на екран отриманий результат.

'''

raw_text = "Samsung is the best phone manufacturer"
processed_text = raw_text.split(" ")
print(f'Отладка: {processed_text}')
length = len(processed_text)
print(f'Результат: {length}')