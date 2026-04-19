from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
import random
from datetime import datetime

console = Console()

history = []
round_num = 1

while True:
    console.clear()

    console.print(
        Panel(
            "[bold yellow]Главное меню[/bold yellow]\n\n"
                  "[1] Начать игру\n"
                  "[2] История игр\n"
                  "[3] Выход",
            border_style="blue",
            title="Меню",
            title_align="center"
        )
    )

    choice = Prompt.ask("Выбери вариант", choices=["1", "2", "3"])

    if choice == "1":
        console.print("\n[bold magenta]Игра Камень / Ножницы / Бумага[/bold magenta]\n")
        console.print("1 - Камень\n2 - Бумага\n3 - Ножницы")

        player = Prompt.ask("Твой выбор", choices=["1", "2", "3"])

        moves = {
            "1": "Камень",
            "2": "Бумага",
            "3": "Ножницы"
        }

        player_move = moves[player]
        computer_move = random.choice(list(moves.values()))

        console.print(f"\n[blue]Компьютер выбрал: {computer_move}[/blue]")

        if player_move == computer_move:
            result = "Ничья"
            console.print("[yellow]Ничья[/yellow]")
        elif (
            (player == "1" and computer_move == "Ножницы") or
            (player == "2" and computer_move == "Камень") or
            (player == "3" and computer_move == "Бумага")
        ):
            result = "Перемога"
            console.print("[green]Ты победил![/green]")
        else:
            result = "Поразка"
            console.print("[red]Ты проиграл![/red]")

        history.append({
            "round": round_num,
            "player": player_move,
            "computer": computer_move,
            "result": result
        })

        round_num += 1

        input("\nНажми Enter чтобы вернуться в меню...")

    elif choice == "2":
        table = Table(title="История игр")

        table.add_column("Раунд", style="cyan")
        table.add_column("Игрок", style="white")
        table.add_column("Компьютер", style="white")
        table.add_column("Результат", style="bold")

        wins = 0
        losses = 0
        draws = 0

        for game in history:
            res = game["result"]

            if res == "Перемога":
                color_res = "[green]Перемога[/green]"
                wins += 1
            elif res == "Поразка":
                color_res = "[red]Поразка[/red]"
                losses += 1
            else:
                color_res = "[yellow]Ничья[/yellow]"
                draws += 1

            table.add_row(
                str(game["round"]),
                game["player"],
                game["computer"],
                color_res
            )

        console.print(table)

        console.print("\n[bold]Статистика:[/bold]")
        console.print(f"Победы: {wins}")
        console.print(f"Поражения: {losses}")
        console.print(f"Ничьи: {draws}")

        input("\nEnter чтобы вернуться в меню...")

    elif choice == "3":
        console.print("[red]Выход из игры...[/red]")
        break