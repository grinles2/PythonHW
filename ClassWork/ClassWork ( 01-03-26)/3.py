'''

Завдання 3
Напишіть функцію, яка відображає горизонтальну або вертикальну лінію з деякого символу. Функція приймає як параметр: довжину лінії, напрямок, символ.


'''

def draw_line(length, direction, symbol):
    if len(symbol) != 1:
        return "Symbol must be exactly one character!"

    if direction.lower() == 'h':
        return symbol * length
    elif direction.lower() == 'v':
        return '\n'.join(symbol for _ in range(length))
    else:
        return 'Error, direction must be "h" or "v"'


print(draw_line(10, 'h', '*'))
print(draw_line(5, 'v', '|'))