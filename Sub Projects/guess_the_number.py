#!/usr/bin/env python3
"""
Guess the Number
Classic number guessing game with different difficulty levels
"""

import random
import time


def play_game(min_num, max_num, max_attempts=None):
    """Play a single round of guess the number"""
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    guesses = []
    
    print(f"\n🎯 I'm thinking of a number between {min_num} and {max_num}...")
    if max_attempts:
        print(f"You have {max_attempts} attempts to guess it!")
    else:
        print("You have unlimited attempts!")
    
    print("\n" + "─"*40)
    
    while True:
        attempts += 1
        
        if max_attempts:
            remaining = max_attempts - attempts + 1
            if remaining <= 0:
                print(f"\n💀 Game Over! You ran out of attempts.")
                print(f"The number was: {secret_number}")
                return False
            print(f"\nAttempts remaining: {remaining}")
        
        try:
            guess = input(f"\nAttempt #{attempts} - Your guess: ").strip()
            
            if guess.lower() == 'quit':
                print(f"\n👋 Giving up? The number was {secret_number}!")
                return False
            
            guess = int(guess)
            
            if guess < min_num or guess > max_num:
                print(f"❌ Please guess between {min_num} and {max_num}!")
                attempts -= 1  # Don't count invalid guesses
                continue
            
            guesses.append(guess)
            
            if guess == secret_number:
                print("\n" + "="*40)
                print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
                print("="*40)
                print(f"You guessed the number in {attempts} attempts!")
                print(f"Your guesses: {guesses}")
                
                # Calculate score
                if max_attempts:
                    score = int((max_attempts - attempts + 1) / max_attempts * 100)
                    print(f"Score: {score}%")
                
                return True
            
            elif guess < secret_number:
                diff = secret_number - guess
                if diff <= 5:
                    print("🔥 Very close! Go HIGHER!")
                elif diff <= 10:
                    print("📈 Too low, but getting warmer!")
                else:
                    print("❄️  Too low! Go much HIGHER!")
            
            else:  # guess > secret_number
                diff = guess - secret_number
                if diff <= 5:
                    print("🔥 Very close! Go LOWER!")
                elif diff <= 10:
                    print("📉 Too high, but getting warmer!")
                else:
                    print("❄️  Too high! Go much LOWER!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input
        except KeyboardInterrupt:
            print(f"\n\n👋 Game interrupted! The number was {secret_number}!")
            return False


def run():
    """Main function for guess the number"""
    wins = 0
    losses = 0
    games_played = 0
    
    while True:
        print("\n" + "="*40)
        print("🎯  GUESS THE NUMBER  🎯")
        print("="*40)
        
        if games_played > 0:
            print(f"\n📊 Stats: {wins} Wins, {losses} Losses")
            win_rate = (wins / games_played * 100) if games_played > 0 else 0
            print(f"Win Rate: {win_rate:.1f}%")
            print("─"*40)
        
        print("\nDifficulty Levels:")
        print("  1. Easy (1-50, unlimited attempts)")
        print("  2. Medium (1-100, 10 attempts)")
        print("  3. Hard (1-200, 8 attempts)")
        print("  4. Expert (1-500, 12 attempts)")
        print("  5. Custom Range")
        print("  6. View Statistics")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            result = play_game(1, 50)
            games_played += 1
            if result:
                wins += 1
            else:
                losses += 1
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            result = play_game(1, 100, 10)
            games_played += 1
            if result:
                wins += 1
            else:
                losses += 1
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            result = play_game(1, 200, 8)
            games_played += 1
            if result:
                wins += 1
            else:
                losses += 1
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            result = play_game(1, 500, 12)
            games_played += 1
            if result:
                wins += 1
            else:
                losses += 1
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            try:
                print("\n📝 Custom Game Settings:")
                min_num = int(input("Minimum number: ").strip())
                max_num = int(input("Maximum number: ").strip())
                
                if min_num >= max_num:
                    print("❌ Minimum must be less than maximum!")
                    time.sleep(1)
                    continue
                
                use_limit = input("Limit attempts? (yes/no): ").strip().lower()
                
                if use_limit in ['yes', 'y']:
                    max_attempts = int(input("Maximum attempts: ").strip())
                    result = play_game(min_num, max_num, max_attempts)
                else:
                    result = play_game(min_num, max_num)
                
                games_played += 1
                if result:
                    wins += 1
                else:
                    losses += 1
                
            except ValueError:
                print("❌ Invalid input!")
                time.sleep(1)
                continue
            
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            print("\n" + "="*40)
            print("📊 STATISTICS")
            print("="*40)
            print(f"Games Played: {games_played}")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            if games_played > 0:
                win_rate = wins / games_played * 100
                print(f"Win Rate: {win_rate:.1f}%")
            print("="*40)
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()