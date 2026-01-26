num_1 = int(input("num1: "))
num_2 = int(input("num2: "))
current = num_1
print("все числа диапазона:")
while True:
    if current > num_2:
        break
    print(current)
    current += 1


current = num_2
print("в обратном порядке:")
while True:
    if current < num_1:
        break
    print(current)
    current -= 1


current = num_1
print("числа кратные 7:")
while True:
    if current > num_2:
        break
    if current % 7 == 0:
        print(current)
    current += 1


current = num_1
count = 0
while True:
    if current > num_2:
        break
    if current % 5 == 0:
        count += 1
    current += 1

print("кол.во чисел кратных 5:", count)
