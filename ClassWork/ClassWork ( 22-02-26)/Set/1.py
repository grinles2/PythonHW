nums = []

user_nums = input("Введите список чисел (через , )-> ")
nums = [int(num.strip()) for num in user_nums.split(',')]
unique_nums = set(nums)
print("Результат:", unique_nums)