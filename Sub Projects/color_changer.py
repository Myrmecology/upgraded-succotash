#!/usr/bin/env python3
"""
Color Changer
Display text in different colors using ANSI escape codes
"""

import time


class Colors:
    """ANSI color codes"""
    RESET = '\033[0m'
    
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def display_color_demo():
    """Display all available colors"""
    print("\n🎨 Color Palette:\n")
    
    print("Regular Colors:")
    colors = [
        ("Red", Colors.RED),
        ("Green", Colors.GREEN),
        ("Yellow", Colors.YELLOW),
        ("Blue", Colors.BLUE),
        ("Magenta", Colors.MAGENTA),
        ("Cyan", Colors.CYAN),
        ("White", Colors.WHITE),
    ]
    
    for name, color in colors:
        print(f"  {color}■■■ {name}{Colors.RESET}")
    
    print("\nBright Colors:")
    bright_colors = [
        ("Bright Red", Colors.BRIGHT_RED),
        ("Bright Green", Colors.BRIGHT_GREEN),
        ("Bright Yellow", Colors.BRIGHT_YELLOW),
        ("Bright Blue", Colors.BRIGHT_BLUE),
        ("Bright Magenta", Colors.BRIGHT_MAGENTA),
        ("Bright Cyan", Colors.BRIGHT_CYAN),
        ("Bright White", Colors.BRIGHT_WHITE),
    ]
    
    for name, color in bright_colors:
        print(f"  {color}■■■ {name}{Colors.RESET}")
    
    print("\nText Styles:")
    print(f"  {Colors.BOLD}Bold Text{Colors.RESET}")
    print(f"  {Colors.UNDERLINE}Underlined Text{Colors.RESET}")
    print(f"  {Colors.RED}{Colors.BOLD}Bold Red Text{Colors.RESET}")


def rainbow_text(text):
    """Display text in rainbow colors"""
    rainbow = [
        Colors.RED,
        Colors.YELLOW,
        Colors.GREEN,
        Colors.CYAN,
        Colors.BLUE,
        Colors.MAGENTA,
    ]
    
    result = ""
    for i, char in enumerate(text):
        color = rainbow[i % len(rainbow)]
        result += f"{color}{char}"
    result += Colors.RESET
    
    return result


def animate_rainbow():
    """Animate text cycling through rainbow colors"""
    text = "  ★ RAINBOW ANIMATION ★  "
    rainbow = [
        Colors.RED,
        Colors.YELLOW,
        Colors.GREEN,
        Colors.CYAN,
        Colors.BLUE,
        Colors.MAGENTA,
    ]
    
    print("\n🌈 Rainbow Animation (will play 3 times):\n")
    
    try:
        for _ in range(3):
            for color in rainbow:
                print(f"\r{color}{text}{Colors.RESET}", end='', flush=True)
                time.sleep(0.3)
    except KeyboardInterrupt:
        print(f"\n{Colors.RESET}")


def custom_text_color():
    """Let user input text and choose a color"""
    print("\n" + "="*40)
    user_text = input("Enter text to colorize: ").strip()
    
    if not user_text:
        print("❌ No text entered!")
        return
    
    print("\nChoose a color:")
    color_options = [
        ("Red", Colors.RED),
        ("Green", Colors.GREEN),
        ("Yellow", Colors.YELLOW),
        ("Blue", Colors.BLUE),
        ("Magenta", Colors.MAGENTA),
        ("Cyan", Colors.CYAN),
        ("Bright Red", Colors.BRIGHT_RED),
        ("Bright Green", Colors.BRIGHT_GREEN),
        ("Bright Cyan", Colors.BRIGHT_CYAN),
    ]
    
    for i, (name, _) in enumerate(color_options, 1):
        print(f"  {i}. {name}")
    
    try:
        choice = int(input("\nYour choice (1-9): ").strip())
        if 1 <= choice <= len(color_options):
            name, color = color_options[choice - 1]
            print(f"\n{color}{Colors.BOLD}{user_text}{Colors.RESET}\n")
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Please enter a valid number!")


def run():
    """Main function for color changer"""
    
    while True:
        print("\n" + "="*40)
        print("🎨  COLOR CHANGER  🎨")
        print("="*40)
        print("\nOptions:")
        print("  1. Display Color Palette")
        print("  2. Rainbow Text Demo")
        print("  3. Rainbow Animation")
        print("  4. Colorize Custom Text")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            display_color_demo()
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            text = input("\nEnter text for rainbow effect: ").strip()
            if text:
                print(f"\n{rainbow_text(text)}\n")
            else:
                print("❌ No text entered!")
            time.sleep(1)
        
        elif choice == "3":
            animate_rainbow()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            custom_text_color()
            time.sleep(1)
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()