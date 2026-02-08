#!/usr/bin/env python3
"""
Coin Flip Simulator
Flip a coin and track your results
"""

import random
import time


def flip_coin():
    """Simulate a coin flip"""
    return random.choice(["Heads", "Tails"])


def animate_flip():
    """Animate the coin flip"""
    animations = ["⚪", "⚫", "⚪", "⚫", "⚪"]
    for frame in animations:
        print(f"\r  Flipping... {frame}", end='', flush=True)
        time.sleep(0.15)
    print("\r" + " " * 20, end='\r')  # Clear the line


def run():
    """Main function for coin flip"""
    heads_count = 0
    tails_count = 0
    total_flips = 0
    
    print("\n" + "="*40)
    print("🪙  COIN FLIP SIMULATOR  🪙")
    print("="*40)
    
    while True:
        print("\n" + "-"*40)
        if total_flips > 0:
            print(f"📊 Statistics:")
            print(f"   Total Flips: {total_flips}")
            print(f"   Heads: {heads_count} ({heads_count/total_flips*100:.1f}%)")
            print(f"   Tails: {tails_count} ({tails_count/total_flips*100:.1f}%)")
            print("-"*40)
        
        print("\nOptions:")
        print("  1. Flip the coin")
        print("  2. Flip multiple times")
        print("  3. Reset statistics")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            print("\n🪙 Flipping the coin...")
            animate_flip()
            result = flip_coin()
            
            if result == "Heads":
                print("🟡 Result: HEADS!")
                heads_count += 1
            else:
                print("⚫ Result: TAILS!")
                tails_count += 1
            
            total_flips += 1
            time.sleep(0.5)
        
        elif choice == "2":
            try:
                num_flips = int(input("\nHow many times to flip? (1-1000): ").strip())
                if 1 <= num_flips <= 1000:
                    print(f"\n🪙 Flipping {num_flips} times...")
                    time.sleep(0.5)
                    
                    temp_heads = 0
                    temp_tails = 0
                    
                    for _ in range(num_flips):
                        result = flip_coin()
                        if result == "Heads":
                            temp_heads += 1
                        else:
                            temp_tails += 1
                    
                    heads_count += temp_heads
                    tails_count += temp_tails
                    total_flips += num_flips
                    
                    print(f"\n✅ Results:")
                    print(f"   Heads: {temp_heads}")
                    print(f"   Tails: {temp_tails}")
                else:
                    print("❌ Please enter a number between 1 and 1000.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
            
            time.sleep(1)
        
        elif choice == "3":
            confirm = input("\n⚠️  Reset all statistics? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                heads_count = 0
                tails_count = 0
                total_flips = 0
                print("✅ Statistics reset!")
            else:
                print("❌ Reset cancelled.")
            time.sleep(1)
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()