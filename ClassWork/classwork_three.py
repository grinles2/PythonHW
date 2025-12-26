import time
num1 = float( input("Введите ваше число: ") )
num2 = float( input("Введите процент содержания жира в молоке: ") )
print("Обработка...")
time.sleep(1)


ans = (num2 * num1)

ans = (ans / 100)


print(ans)