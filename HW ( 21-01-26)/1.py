'''

Написати програму, яка за вибором користувача зводить введене
ним число у степінь від нульового до сьомого включно.

'''

user_num = int(input("Введите своё число-->"))

num_power1 = user_num ** 0
num_power2 = user_num ** 1
num_power3 = user_num ** 2
num_power4 = user_num ** 3
num_power5 = user_num ** 4
num_power6 = user_num ** 5
num_power7 = user_num ** 6
num_power8 = user_num ** 7

print(f"Ваше число в ^0 -> {num_power1}")
print(f"Ваше число в ^1 -> {num_power2}")
print(f"Ваше число в ^2 -> {num_power3}")
print(f"Ваше число в ^3  ->{num_power4}")
print(f"Ваше число в ^4 -> {num_power5}")
print(f"Ваше число в ^5 -> {num_power6}")
print(f"Ваше число в ^6 -> {num_power7}")
print(f"Ваше число в ^7 -> {num_power8}")