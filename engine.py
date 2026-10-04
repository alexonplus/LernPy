from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.prompt import IntPrompt
from rich.text import Text
import time

console = Console()

class GameEngine:
    def __init__(self, puzzles):
        self.puzzles = puzzles
        self.score = 0
        self.total = len(puzzles)
        
    def show_welcome(self):
        console.clear()
        title = Text("Добро пожаловать в LernPy! 🐍", style="bold green", justify="center")
        subtitle = Text("Учим Python на хитрых примерах и загадках.\n", justify="center")
        panel = Panel(Text.assemble(title, "\n", subtitle), border_style="green", expand=False)
        console.print(panel)
        console.input("\n[dim]Нажмите Enter, чтобы начать...[/dim]")

    def run(self):
        self.show_welcome()
        
        for idx, puzzle in enumerate(self.puzzles, 1):
            console.clear()
            console.rule(f"[bold cyan]Загадка {idx}/{self.total} - {puzzle['title']}[/bold cyan]")
            
            # Show code
            syntax = Syntax(puzzle['code'], "python", theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title="Код", border_style="blue"))
            
            console.print(f"\n[bold yellow]{puzzle['question']}[/bold yellow]")
            
            # Show options
            for i, option in enumerate(puzzle['options'], 1):
                console.print(f"  [bold cyan]{i}.[/bold cyan] {option}")
                
            console.print()
            
            # Get input
            answer = IntPrompt.ask("Ваш ответ (введите номер)", choices=[str(i) for i in range(1, len(puzzle['options']) + 1)])
            
            # Check answer
            if answer == puzzle['correct_answer']:
                console.print("\n[bold green]✅ Правильно![/bold green]")
                self.score += 1
            else:
                correct_idx = puzzle['correct_answer'] - 1
                console.print(f"\n[bold red]❌ Неверно.[/bold red] Правильный ответ: [bold]{puzzle['options'][correct_idx]}[/bold]")
                
            console.print(Panel(f"[bold magenta]Объяснение:[/bold magenta]\n{puzzle['explanation']}", border_style="magenta"))
            
            if idx < self.total:
                console.input("\n[dim]Нажмите Enter для следующей загадки...[/dim]")
                
        self.show_results()
        
    def show_results(self):
        console.clear()
        console.rule("[bold green]Игра окончена![/bold green]")
        
        score_text = Text(f"Ваш результат: {self.score} из {self.total}", style="bold yellow", justify="center")
        
        if self.score == self.total:
            feedback = Text("\n🎉 Отлично! Вы настоящий Python-ниндзя!", justify="center")
        elif self.score >= self.total / 2:
            feedback = Text("\n👍 Неплохо, но есть куда расти. Продолжайте практиковаться!", justify="center")
        else:
            feedback = Text("\n📚 Нужно больше практики. В Python много неочевидных вещей!", justify="center")
            
        panel = Panel(Text.assemble(score_text, feedback), border_style="yellow", expand=False)
        console.print(panel)
        console.print("\n[dim]Спасибо за игру в LernPy![/dim]")
