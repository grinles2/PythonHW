def is_palindrome(number):
    num_str = str(number)

    if num_str == num_str[::-1]:
        return True
    else:
        return False


user_word = input("Впишите слово: ")

result = is_palindrome(user_word)

print(result)