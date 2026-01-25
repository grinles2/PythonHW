num_1 = int(input('num1: '))
num_2 = int(input('num2: '))

while num_2 > num_1:
    num_2 -= 1
    if num_2 % 2 != 0:
        continue
    else:
        print(num_2)