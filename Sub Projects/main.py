#!/usr/bin/env python3
"""
Sub Projects Main Menu
A launcher for all mini Python programs
"""

import sys

# Import all Python mini programs
from ascii_animator import run as ascii_animator
from coin_flip import run as coin_flip
from color_changer import run as color_changer
from dice_roller import run as dice_roller
from fortune_cookie import run as fortune_cookie
from guess_the_number import run as guess_the_number
from mad_scientist_name import run as mad_scientist_name
from mini_chatbot import run as mini_chatbot
from mini_quiz import run as mini_quiz
from password_tester import run as password_tester
from random_jokes import run as random_jokes
from rock_paper_scissors import run as rock_paper_scissors
from simple_graph_plot import run as simple_graph_plot
from simple_timer import run as simple_timer
from text_adventure import run as text_adventure
from tictactoe import run as tictactoe
from tip_calculator import run as tip_calculator
from unit_converter import run as unit_converter
from weather_checker import run as weather_checker


# Define all programs with their names and callables
PROGRAMS = [
    ("ASCII Animator", ascii_animator),
    ("Coin Flip", coin_flip),
    ("Color Changer", color_changer),
    ("Dice Roller", dice_roller),
    ("Fortune Cookie", fortune_cookie),
    ("Guess the Number", guess_the_number),
    ("Mad Scientist Name Generator", mad_scientist_name),
    ("Mini Chatbot", mini_chatbot),
    ("Mini Quiz", mini_quiz),
    ("Password Strength Tester", password_tester),
    ("Random Jokes", random_jokes),
    ("Rock Paper Scissors", rock_paper_scissors),
    ("Simple Graph Plotter", simple_graph_plot),
    ("Simple Timer", simple_timer),
    ("Text Adventure", text_adventure),
    ("Tic Tac Toe", tictactoe),
    ("Tip Calculator", tip_calculator),
    ("Unit Converter", unit_converter),
    ("Weather Checker", weather_checker),
]


def display_menu():
    """Display the main menu with all available programs"""
    print("\n" + "="*50)
    print("🎮  MINI PROJECTS LAUNCHER  🎮")
    print("="*50)
    print("\nPlease select a mini program to play:\n")
    
    for i, (name, _) in enumerate(PROGRAMS, 1):
        print(f"  {i:2}. {name}")
    
    print(f"\n   0. Exit")
    print("="*50)


def main():
    """Main menu loop"""
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-19): ").strip()
            
            if choice == "0":
                print("\n👋 Thanks for playing! Goodbye!\n")
                sys.exit(0)
            
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(PROGRAMS):
                program_name, program_func = PROGRAMS[choice_num - 1]
                print(f"\n{'='*50}")
                print(f"🎯 Launching: {program_name}")
                print(f"{'='*50}\n")
                
                # Run the selected program
                program_func()
                
                # After program finishes, pause before returning to menu
                input("\n✅ Press Enter to return to the main menu...")
            else:
                print("\n❌ Invalid choice! Please enter a number between 0 and 19.")
                input("Press Enter to continue...")
        
        except ValueError:
            print("\n❌ Invalid input! Please enter a number.")
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted! Goodbye!\n")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()