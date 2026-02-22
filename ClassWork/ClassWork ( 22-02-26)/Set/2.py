import random

set1 = set(random.randint(1, 20) for i in range(10))
set2 = set(random.randint(1, 20) for i in range(10))

print("Первая множинна:", set1)
print("вторая множинна:", set2)
print("*" * 50)
print("Общие Элементы:", set1 & set2)
print("Разница:", set1 - set2)
print("Объединенные:", set1 | set2)