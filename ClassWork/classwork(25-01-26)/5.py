num_1 = int(input('num1: '))
num_2 = int(input('num2: '))

while num_1 < num_2:
    num_1 += 1
    if num_1 % 2 == 0:
        continue
    else:
        print(num_1)
else:
    print('Придумайте сами')

while num_1 > num_2:
    num_1 -= 1
    if num_1 % 2 == 0:
        continue
    else:
        print(num_1)
else:
    print('Ква')