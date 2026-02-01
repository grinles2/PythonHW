num = int(input("введите число: "))
action = 0
while action < 10:
    action = action + 1
    result = num * action
    print(f'{num} * {action} = {result}')