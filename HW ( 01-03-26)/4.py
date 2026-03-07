def count_digits(number):
    if number == 0:
        return 1

    count = 0
    number = abs(number)

    while number > 0:
        number //= 10
        count += 1

    return count


result = count_digits(3456)
print(result)