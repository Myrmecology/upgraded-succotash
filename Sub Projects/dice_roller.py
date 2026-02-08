#!/usr/bin/env python3
"""
Dice Roller
Roll dice of various types and combinations
"""

import random
import time


def roll_dice(num_dice, num_sides):
    """Roll dice and return results"""
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls


def display_dice_art(value):
    """Display ASCII art for a six-sided die"""
    dice_art = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        ]
    }
    
    return dice_art.get(value, ["Invalid"])


def display_multiple_dice(rolls):
    """Display multiple dice side by side"""
    if all(1 <= roll <= 6 for roll in rolls):
        # Display dice art
        dice_arts = [display_dice_art(roll) for roll in rolls]
        
        # Print dice side by side
        for line_idx in range(5):
            line = "  ".join(dice[line_idx] for dice in dice_arts)
            print(line)
    else:
        # For non-standard dice, just show numbers
        for i, roll in enumerate(rolls, 1):
            print(f"  Die {i}: {roll}")


def roll_animation():
    """Animate dice rolling"""
    symbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    for _ in range(10):
        print(f"\r  Rolling... {random.choice(symbols)}", end='', flush=True)
        time.sleep(0.1)
    print("\r" + " " * 20, end='\r')


def run():
    """Main function for dice roller"""
    
    while True:
        print("\n" + "="*40)
        print("🎲  DICE ROLLER  🎲")
        print("="*40)
        print("\nOptions:")
        print("  1. Roll standard dice (d6)")
        print("  2. Roll custom dice")
        print("  3. Roll d20 (for tabletop RPGs)")
        print("  4. Roll multiple different dice")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            try:
                num_dice = int(input("\nHow many dice to roll? (1-10): ").strip())
                if 1 <= num_dice <= 10:
                    print("\n🎲 Rolling...")
                    roll_animation()
                    
                    rolls = roll_dice(num_dice, 6)
                    print("\n" + "─"*40)
                    display_multiple_dice(rolls)
                    print("─"*40)
                    print(f"Total: {sum(rolls)}")
                    print(f"Average: {sum(rolls)/len(rolls):.1f}")
                else:
                    print("❌ Please enter a number between 1 and 10.")
            except ValueError:
                print("❌ Invalid input!")
            
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            try:
                num_dice = int(input("\nHow many dice? (1-20): ").strip())
                num_sides = int(input("How many sides per die? (2-100): ").strip())
                
                if 1 <= num_dice <= 20 and 2 <= num_sides <= 100:
                    print(f"\n🎲 Rolling {num_dice}d{num_sides}...")
                    roll_animation()
                    
                    rolls = roll_dice(num_dice, num_sides)
                    print("\n" + "─"*40)
                    print(f"Results: {rolls}")
                    print("─"*40)
                    print(f"Total: {sum(rolls)}")
                    print(f"Average: {sum(rolls)/len(rolls):.1f}")
                    print(f"Minimum: {min(rolls)}")
                    print(f"Maximum: {max(rolls)}")
                else:
                    print("❌ Invalid range!")
            except ValueError:
                print("❌ Invalid input!")
            
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            print("\n🎲 Rolling d20...")
            roll_animation()
            
            roll = random.randint(1, 20)
            print("\n" + "─"*40)
            print(f"🎯 Result: {roll}")
            
            if roll == 20:
                print("🌟 CRITICAL HIT! Natural 20!")
            elif roll == 1:
                print("💀 CRITICAL FAIL! Natural 1!")
            elif roll >= 15:
                print("✨ Great roll!")
            
            print("─"*40)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print("\n🎲 Roll multiple different dice")
            print("Example: 2d6, 1d20, 3d4")
            dice_input = input("Enter dice notation (or press Enter for 1d6+1d20): ").strip()
            
            if not dice_input:
                dice_input = "1d6, 1d20"
            
            try:
                dice_groups = dice_input.split(',')
                all_rolls = []
                
                print("\n" + "─"*40)
                for group in dice_groups:
                    group = group.strip().lower()
                    if 'd' in group:
                        parts = group.split('d')
                        num = int(parts[0]) if parts[0] else 1
                        sides = int(parts[1])
                        
                        rolls = roll_dice(num, sides)
                        all_rolls.extend(rolls)
                        print(f"{num}d{sides}: {rolls} (sum: {sum(rolls)})")
                
                print("─"*40)
                print(f"Grand Total: {sum(all_rolls)}")
                
            except (ValueError, IndexError):
                print("❌ Invalid dice notation!")
            
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()