"""CLI - Main file"""
import sys
import rich
from vocably import __authors__


def main():
    """CLI vocably"""
    rich.print("[bold purple]Welcome to vocably![/bold purple]")
    rich.print(f"Authors : [bold blue]{__authors__}[/bold blue]")
    rich.print("Type [bold blue]help[/bold blue] to get help")
    while True:
        user_input = input(">>> ")
        if user_input == "help":
            rich.print("help")
        elif user_input == "exit()":
            sys.exit()
        else:
            rich.print("Invalid command")


if __name__ == "__main__":
    sys.exit(main())
