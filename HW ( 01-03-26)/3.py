def draw_square(size, symbol, filled):
    for i in range(size):
        for j in range(size):
            if filled:
                print(symbol, end=" ")
            else:
                if i == 0 or i == size-1 or j == 0 or j == size-1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")
        print()


size = int(input("Введите длину: "))
symbol = input("впишите символ: ")
filled = input("напишите True/False для заполненного квадрата или нет: ")

if filled == "True":
    filled = True
else:
    filled = False


draw_square(size, symbol, filled)