
import random

num = [random.randint(1, 100) for _ in range(10)]


def find_min(id):
    if id > len(num) - 10:
        return id, float('inf')

    current_sum = sum(num[id: id + 10])

    next_id, next_min_sum = find_min(id + 1)

    if current_sum < next_min_sum:
        return id, current_sum
    else:
        return next_id, next_min_sum


best_index, min_sum = find_min(0)
print(f'Позиция: {best_index}')
print(f'Сумма: {min_sum}')