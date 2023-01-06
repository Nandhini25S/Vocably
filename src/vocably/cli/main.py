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
            rich.print("""vocably provides you environment for Natural Language Completely focus on
            text and speech. It is a free and open source framework for Natural Language
            development, understanding, and generation. It is written in Python and allows
            for easy integration with other Python libraries. It is licensed under the MIT
            License. Author: Sanjaypranav, Nandhini Sivakumar and Sarika Mohan (2022) Date: 2022-10-11
            Press ctrl+c to exit or ctrl+d or exit() or quit()""")
        elif user_input in ("exit()", "quit()"):
            sys.exit()
        else:
            rich.print("Invalid command")


if __name__ == "__main__":
    sys.exit(main())
