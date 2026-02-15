numbers = input("введите числа колекции через ПРОБЕЛ : ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

total = 0
for num in numbers:
    total += num
print("Сумма:", total)

average = total / len(numbers) if len(numbers) > 0 else 0
print("AVG:", average)