import time
import console_ui

def load():
    loading = ""
    for i in range(3):
        loading += "."
        print(f"\rЗагрузка{loading}", end="")
        time.sleep(1)
    print()


options = ["Начать игру", "Сохраниться", "Выйти"]

console_ui.draw_header("Example")
console_ui.draw_menu(options)

choice = int(input(": "))

if choice < 1 or choice > len(options):
    console_ui.draw_warning("Неверный выбор")

elif choice == 1:
    load()
elif choice == 2:
    load()
elif choice == 3:
    print("Выход...")