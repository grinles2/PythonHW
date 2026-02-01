action = 0
num = 1


while action < 9:
    action = action + 1
    result = num * action
    print(f'{num} * {action} = {result}')

    if action == 9:
        num += 1
        action = 0
        print("---------")


    elif num > 9:

        exit()

    else:
        exit()
