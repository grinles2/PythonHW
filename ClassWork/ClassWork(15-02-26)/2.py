numbers = input("введите числа колекции через ПРОБЕЛ: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

num = int(input("введите число: "))

count_num = numbers.count(num)
print(f"число {num} находиться в  {count_num} раз")
