from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from game import start_game, show_history

console = Console()

def main_menu():
    while True:
        console.print(
            Panel(
                "[1] Начать игру\n[2] История игр\n[3] Выход",
                border_style="cyan"
            )
        )
        choice = Prompt.ask("")
        if choice == "1":
            start_game()
        elif choice == "2":
            show_history()
        elif choice == "3":
            console.print("Выход из игры")
            break
        else:
            console.print("Выбор не найден")
if __name__ == "__main__":
    main_menu()