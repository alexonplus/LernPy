import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.prompt import IntPrompt
from rich.text import Text

from models import Puzzle, Difficulty, Language, PuzzleType
from i18n import UI_STRINGS

console = Console()
PROFILE_FILE = "profile.json"

class GameEngine:
    def __init__(self, puzzles_db):
        self.puzzles_db = puzzles_db
        self.lang = Language.RU
        self.level = Difficulty.EASY
        self.puzzles = []
        self.score = 0
        self.total = 0
        self.profile = self.load_profile()
        
    def load_profile(self):
        if os.path.exists(PROFILE_FILE):
            try:
                with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
        return {"xp": 0, "solved": 0}

    def save_profile(self):
        with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.profile, f, indent=4)

    def _t(self, key, **kwargs):
        text = UI_STRINGS[self.lang.value].get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text

    def setup(self):
        console.clear()
        
        # 1. Choose Language
        console.print("[bold cyan]Choose language / Выберите язык:[/bold cyan]")
        console.print("  [bold]1.[/bold] Русский")
        console.print("  [bold]2.[/bold] English")
        lang_choice = IntPrompt.ask("1/2", choices=["1", "2"], default=1)
        self.lang = Language.RU if lang_choice == 1 else Language.EN
        
        console.clear()
        
        # 2. Choose Difficulty
        console.print(f"[bold cyan]{self._t('choose_level')}[/bold cyan]")
        console.print(f"  [bold]1.[/bold] {self._t('level_easy')}")
        console.print(f"  [bold]2.[/bold] {self._t('level_medium')}")
        console.print(f"  [bold]3.[/bold] {self._t('level_hard')}")
        
        level_choice = IntPrompt.ask("1/2/3", choices=["1", "2", "3"], default=1)
        if level_choice == 1:
            self.level = Difficulty.EASY
        elif level_choice == 2:
            self.level = Difficulty.MEDIUM
        else:
            self.level = Difficulty.HARD

        # Filter puzzles
        all_puzzles = self.puzzles_db[self.lang]
        self.puzzles = [p for p in all_puzzles if p.difficulty == self.level]
        self.total = len(self.puzzles)
        
    def show_welcome(self):
        console.clear()
        title = Text(self._t("welcome_title"), style="bold green", justify="center")
        subtitle = Text(self._t("welcome_subtitle"), justify="center")
        
        stats = Text(self._t("profile_stats", xp=self.profile['xp'], solved=self.profile['solved']), style="bold magenta", justify="center")
        
        panel = Panel(Text.assemble(title, "\n", subtitle, "\n", stats), border_style="green", expand=False)
        console.print(panel)
        console.input(f"\n[dim]{self._t('press_enter')}[/dim]")

    def run(self):
        self.setup()
        
        if self.total == 0:
            console.print(f"\n[bold yellow]{self._t('level_not_found')}[/bold yellow]")
            return

        self.show_welcome()
        
        for idx, puzzle in enumerate(self.puzzles, 1):
            console.clear()
            
            puzzle_type_str = self._t("type_bug") if puzzle.type == PuzzleType.BUG else self._t("type_output")
            console.rule(f"[bold cyan]{self._t('puzzle')} {idx}/{self.total} | {puzzle_type_str} | {puzzle.title}[/bold cyan]")
            
            # Show code
            syntax = Syntax(puzzle.code, "python", theme="monokai", line_numbers=(puzzle.type != PuzzleType.BUG))
            console.print(Panel(syntax, title=self._t("code"), border_style="blue" if puzzle.type == PuzzleType.OUTPUT else "red"))
            
            console.print(f"\n[bold yellow]{puzzle.question}[/bold yellow]")
            
            # Show options
            for i, option in enumerate(puzzle.options, 1):
                console.print(f"  [bold cyan]{i}.[/bold cyan] {option}")
                
            console.print()
            
            # Get input
            answer = IntPrompt.ask(self._t("your_answer"), choices=[str(i) for i in range(1, len(puzzle.options) + 1)])
            
            # Check answer
            if answer == puzzle.correct_answer:
                xp_reward = {Difficulty.EASY: 10, Difficulty.MEDIUM: 20, Difficulty.HARD: 30}[puzzle.difficulty]
                self.score += 1
                self.profile['xp'] += xp_reward
                self.profile['solved'] += 1
                
                console.print(f"\n[bold green]{self._t('correct')}[/bold green] [bold magenta]{self._t('xp_gained', xp=xp_reward)}[/bold magenta]")
            else:
                correct_idx = puzzle.correct_answer - 1
                console.print(f"\n[bold red]{self._t('incorrect')}[/bold red] [bold]{puzzle.options[correct_idx]}[/bold]")
                
            console.print(Panel(f"[bold magenta]{self._t('explanation')}[/bold magenta]\n{puzzle.explanation}", border_style="magenta"))
            
            if idx < self.total:
                console.input(f"\n[dim]{self._t('press_enter_next')}[/dim]")
                
        self.show_results()
        self.save_profile()
        
    def show_results(self):
        console.clear()
        console.rule(f"[bold green]{self._t('game_over')}[/bold green]")
        
        score_text = Text(self._t("score", score=self.score, total=self.total), style="bold yellow", justify="center")
        
        if self.score == self.total:
            feedback = Text(f"\n{self._t('feedback_perfect')}", justify="center")
        elif self.score >= self.total / 2:
            feedback = Text(f"\n{self._t('feedback_good')}", justify="center")
        else:
            feedback = Text(f"\n{self._t('feedback_bad')}", justify="center")
            
        panel = Panel(Text.assemble(score_text, feedback), border_style="yellow", expand=False)
        console.print(panel)
        
        stats = Text(self._t("profile_stats", xp=self.profile['xp'], solved=self.profile['solved']), style="bold magenta", justify="center")
        console.print(Panel(stats, border_style="magenta", expand=False))
        
        console.print(f"\n[dim]{self._t('thanks')}[/dim]")
