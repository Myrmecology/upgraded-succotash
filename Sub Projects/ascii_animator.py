#!/usr/bin/env python3
"""
ASCII Animator
Display fun ASCII art animations
"""

import time
import os
import sys


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def animate_spinner():
    """Spinning animation"""
    frames = ['|', '/', '-', '\\']
    print("\n⭐ Spinner Animation (Press Ctrl+C to stop)\n")
    try:
        for _ in range(20):
            for frame in frames:
                print(f"\r  {frame} Loading... {frame}", end='', flush=True)
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\r  ✓ Complete!     ")


def animate_bouncing_ball():
    """Bouncing ball animation"""
    print("\n⚽ Bouncing Ball (Press Ctrl+C to stop)\n")
    try:
        for _ in range(3):
            # Ball going down
            for i in range(10):
                print("\r" + " " * i + "o", end='', flush=True)
                time.sleep(0.05)
            # Ball going up
            for i in range(10, 0, -1):
                print("\r" + " " * i + "o", end='', flush=True)
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n")


def animate_wave():
    """Wave animation"""
    print("\n🌊 Wave Animation (Press Ctrl+C to stop)\n")
    try:
        wave = "~-~-~-~-~-~-~-~-~-~-"
        for _ in range(15):
            for i in range(len(wave)):
                print(f"\r{wave[i:] + wave[:i]}", end='', flush=True)
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n")


def animate_typing_text():
    """Typing text animation"""
    text = "Hello! This is a typing animation effect..."
    print("\n⌨️  Typing Animation\n")
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")
    time.sleep(1)


def animate_progress_bar():
    """Progress bar animation"""
    print("\n📊 Progress Bar\n")
    for i in range(101):
        bar_length = 30
        filled = int(bar_length * i / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"\r  [{bar}] {i}%", end='', flush=True)
        time.sleep(0.03)
    print("\n")


def run():
    """Main function for ASCII animator"""
    animations = [
        ("Spinner", animate_spinner),
        ("Bouncing Ball", animate_bouncing_ball),
        ("Wave", animate_wave),
        ("Typing Text", animate_typing_text),
        ("Progress Bar", animate_progress_bar),
    ]
    
    while True:
        print("\n" + "="*40)
        print("✨ ASCII ANIMATOR ✨")
        print("="*40)
        print("\nSelect an animation:\n")
        
        for i, (name, _) in enumerate(animations, 1):
            print(f"  {i}. {name}")
        
        print(f"  0. Return to Main Menu")
        print("="*40)
        
        try:
            choice = input("\nYour choice: ").strip()
            
            if choice == "0":
                break
            
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(animations):
                name, anim_func = animations[choice_num - 1]
                print(f"\n▶️  Playing: {name}")
                anim_func()
                input("\nPress Enter to continue...")
            else:
                print("❌ Invalid choice!")
                time.sleep(1)
        
        except ValueError:
            print("❌ Please enter a valid number!")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n")
            break


if __name__ == "__main__":
    run()