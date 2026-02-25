
'''
Завдання 2
Користувач вводить кількість своїх друзів та ігри, що є у
кожного з них та у нього самого. Вивести ігри, в які можуть
зіграти всі гравці разом
'''

friend_num = int(input("Введите кол-во друзей -> "))

if friend_num <= 0:
    exit("Вы не можете играть в одиночку")

friends_games = input("Введите игры (через , ) которые есть у ваших друзей -> ")
user_games = input("Введите игры (через , ) которые есть у вас -> ")

friends_games = [game.strip().lower()
for game in friends_games.split(',')]
user_games = [game.strip().lower()
for game in user_games.split(',')]

common_games = set(friends_games) & set(user_games)

if common_games:
    print("У вас общих игр:")
    for game in common_games:
        print("-", game)
else:
    print("У вас нету общих игр")

