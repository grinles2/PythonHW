'''

Користувач вводить з клавіатури рядок. Перевірте чи є введений
рядок паліндромом. Паліндром — слово або текст, що читається
однаково зліва направо і справа наліво. Наприклад:
● Козак з казок;
● Радар;
● А мене нема.

'''


raw_text = input("Введите текст -> ")

user_text = raw_text.lower()
print(f"ОТЛАДКА 1 (ловер кейс): {user_text}")

processed_text = ""

for char in user_text:
    if char.isalpha():
        processed_text += char

reversed_text = processed_text[::-1]

print(f"ОТЛАДКА 2 (убрать пробелы): {processed_text}")
print(f"ОТЛАДКА 3 (обратный текст): {reversed_text}")
print("-----------------------------")

if processed_text == reversed_text:
    print(f'Текст: "{raw_text}" — палиндром')
else:
    print(f'Текст: "{raw_text}" — НЕ палиндром')





