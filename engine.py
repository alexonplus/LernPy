import json
import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.prompt import IntPrompt
from rich.text import Text

from models import Puzzle, Difficulty, Language, PuzzleType
from i18n import UI_STRINGS

console = Console()
PROFILE_FILE = "profile.json"

NEXT_DIFFICULTY = {
    Difficulty.EASY: Difficulty.MEDIUM,
    Difficulty.MEDIUM: Difficulty.HARD,
    Difficulty.HARD: None
}

DIFFICULTY_NAMES = {
    Difficulty.EASY: "level_easy",
    Difficulty.MEDIUM: "level_medium",
    Difficulty.HARD: "level_hard"
}

class GameEngine:
    def __init__(self, puzzles_db):
        self.puzzles_db = puzzles_db
        self.lang = Language.RU
        self.level = Difficulty.EASY
        self.puzzles = []
        self.score = 0
        self.total = 0
        self.lives = 3
        self.combo = 0
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

    def _get_level_name(self, diff: Difficulty) -> str:
        key = DIFFICULTY_NAMES.get(diff, "level_easy")
        return self._t(key)

    def setup(self):
        console.clear()
        
        # 1. Choose Language
        console.print("[bold cyan]Choose language / Выберите язык:[/bold cyan]")
        console.print("  [bold]1.[/bold] Русский")
        console.print("  [bold]2.[/bold] English")
        lang_choice = IntPrompt.ask("1/2", choices=["1", "2"], default=1)
        self.lang = Language.RU if lang_choice == 1 else Language.EN
        
        console.clear()
        
        # 2. Choose Starting Difficulty
        console.print(f"[bold cyan]{self._t('choose_level')}[/bold cyan]")
        console.print(f"  [bold]1.[/bold] {self._t('level_easy')} [dim](Рекомендуется для начала)[/dim]")
        console.print(f"  [bold]2.[/bold] {self._t('level_medium')}")
        console.print(f"  [bold]3.[/bold] {self._t('level_hard')}")
        
        level_choice = IntPrompt.ask("1/2/3", choices=["1", "2", "3"], default=1)
        if level_choice == 1:
            self.level = Difficulty.EASY
        elif level_choice == 2:
            self.level = Difficulty.MEDIUM
        else:
            self.level = Difficulty.HARD

    def _load_level_puzzles(self):
        all_puzzles = self.puzzles_db[self.lang]
        self.puzzles = [p for p in all_puzzles if p.difficulty == self.level]
        random.shuffle(self.puzzles)
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
        self.show_welcome()
        
        self.lives = 3
        self.combo = 0
        total_answered_in_session = 0
        campaign_won = False

        while True:
            self._load_level_puzzles()
            
            if self.total == 0:
                console.print(f"\n[bold yellow]{self._t('level_not_found')}[/bold yellow]")
                break

            current_level_name = self._get_level_name(self.level)
            
            # Play all puzzles in the current level
            for idx, puzzle in enumerate(self.puzzles, 1):
                console.clear()
                
                puzzle_type_str = self._t("type_bug") if puzzle.type == PuzzleType.BUG else self._t("type_output")
                status_str = f"[{current_level_name}] | {self._t('lives', lives=self.lives)} | {self._t('combo', combo=self.combo)}"
                console.rule(f"[bold cyan]{self._t('puzzle')} {idx}/{self.total} | {puzzle_type_str}[/bold cyan] | {status_str}")
                
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
                total_answered_in_session += 1
                
                # Check answer
                if answer == puzzle.correct_answer:
                    self.combo += 1
                    base_xp = {Difficulty.EASY: 10, Difficulty.MEDIUM: 20, Difficulty.HARD: 30}[puzzle.difficulty]
                    
                    multiplier = 1.0 + (self.combo - 1) * 0.5 if self.combo > 0 else 1.0
                    total_xp = int(base_xp * multiplier)
                    bonus_xp = total_xp - base_xp
                    
                    self.score += 1
                    self.profile['xp'] += total_xp
                    self.profile['solved'] += 1
                    
                    console.print(f"\n[bold green]{self._t('correct')}[/bold green] [bold magenta]{self._t('xp_gained', xp=total_xp)}[/bold magenta]")
                    if bonus_xp > 0:
                        console.print(f"[bold yellow]{self._t('combo_bonus', bonus=bonus_xp)}[/bold yellow]")
                else:
                    self.combo = 0
                    self.lives -= 1
                    correct_idx = puzzle.correct_answer - 1
                    console.print(f"\n[bold red]{self._t('incorrect')}[/bold red] [bold]{puzzle.options[correct_idx]}[/bold]")
                    
                console.print(Panel(f"[bold magenta]{self._t('explanation')}[/bold magenta]\n{puzzle.explanation}", border_style="magenta"))
                
                # Check if out of lives
                if self.lives <= 0:
                    console.print(f"\n[bold red]{self._t('out_of_lives')}[/bold red]")
                    console.input(f"\n[dim]{self._t('press_enter_next')}[/dim]")
                    break
                    
                if idx < self.total:
                    console.input(f"\n[dim]{self._t('press_enter_next')}[/dim]")
                    
            # If player died, end session
            if self.lives <= 0:
                break
                
            # Level Cleared!
            console.clear()
            cleared_panel = Panel(
                f"[bold green]{self._t('level_cleared', level=current_level_name)}[/bold green]\n\n"
                f"{self._t('bonus_life')}",
                border_style="green",
                expand=False
            )
            console.print(cleared_panel)
            
            # Heal 1 life (max 3)
            if self.lives < 3:
                self.lives += 1
                
            # Check if there is a next level
            next_lvl = NEXT_DIFFICULTY.get(self.level)
            if next_lvl is not None:
                next_lvl_name = self._get_level_name(next_lvl)
                console.print(f"\n[bold cyan]{self._t('proceed_next_level', next_level=next_lvl_name)}[/bold cyan]")
                console.print(f"  [bold]1.[/bold] {self._t('yes_proceed')}")
                console.print(f"  [bold]2.[/bold] {self._t('no_exit')}")
                
                choice = IntPrompt.ask("1/2", choices=["1", "2"], default=1)
                if choice == 1:
                    self.level = next_lvl
                    continue
                else:
                    break
            else:
                # Beaten the hardest level
                campaign_won = True
                console.print(f"\n[bold gold1]{self._t('campaign_completed')}[/bold gold1]")
                console.input(f"\n[dim]{self._t('press_enter_next')}[/dim]")
                break
                
        self.show_results(total_answered_in_session, campaign_won)
        self.save_profile()
        
    def show_results(self, total_answered, campaign_won):
        console.clear()
        console.rule(f"[bold green]{self._t('game_over')}[/bold green]")
        
        score_text = Text(self._t("score", score=self.score, total=total_answered), style="bold yellow", justify="center")
        
        if self.lives <= 0:
            feedback = Text(f"\n💀 Ваши жизни исчерпаны. Попробуйте еще раз!", justify="center", style="bold red")
        elif campaign_won:
            feedback = Text(f"\n🏆 Невероятно! Вы прошли ВСЕ уровни сложности!", justify="center", style="bold gold1")
        elif self.score == total_answered and total_answered > 0:
            feedback = Text(f"\n{self._t('feedback_perfect')}", justify="center")
        elif self.score >= total_answered / 2:
            feedback = Text(f"\n{self._t('feedback_good')}", justify="center")
        else:
            feedback = Text(f"\n{self._t('feedback_bad')}", justify="center")
            
        panel = Panel(Text.assemble(score_text, feedback), border_style="yellow", expand=False)
        console.print(panel)
        
        stats = Text(self._t("profile_stats", xp=self.profile['xp'], solved=self.profile['solved']), style="bold magenta", justify="center")
        console.print(Panel(stats, border_style="magenta", expand=False))
        
        console.print(f"\n[dim]{self._t('thanks')}[/dim]")
