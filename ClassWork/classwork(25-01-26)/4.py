num_1 = int(input('num1: '))
num_2 = int(input('num2: '))
action = input("Порядок(1, 2): ")

match action:
    case "1":
        while num_1 <= num_2:
            num_1 += 1
            print(num_1)
        else:
            print('Ля вас радуйся')
    case "2":
        while num_2 >= num_1:
            num_2 -= 1
            print(num_2)
        else:
            print('ля вася гуляй или радуйся')
