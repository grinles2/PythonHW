import time
num1 = float( input("Введите ваше число: ") )
num2 = float( input("Введите процент содержания жира в молоке: ") )
print("Обработка...")
time.sleep(1)


ans = (num1 / num2)

ans = int(ans)

print(ans)