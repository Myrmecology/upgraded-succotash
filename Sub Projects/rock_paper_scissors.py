#!/usr/bin/env python3
"""
Rock Paper Scissors
Classic game with various modes and statistics
"""

import random
import time


class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0
        
        # ASCII art for choices
        self.art = {
            'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
            """,
            'paper': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
            """,
            'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            """
        }
    
    def get_winner(self, player, computer):
        """Determine the winner"""
        if player == computer:
            return 'tie'
        
        winning_combos = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combos[player] == computer:
            return 'player'
        else:
            return 'computer'
    
    def display_choices(self, player, computer):
        """Display the choices with ASCII art"""
        print("\nYour choice:")
        print(self.art[player])
        
        print("\nComputer's choice:")
        print(self.art[computer])
    
    def play_round(self):
        """Play a single round"""
        print("\n" + "─"*50)
        print(f"Round {self.rounds_played + 1}")
        print("─"*50)
        print("\nChoose your weapon:")
        print("  1. 🪨 Rock")
        print("  2. 📄 Paper")
        print("  3. ✂️  Scissors")
        
        while True:
            choice = input("\nYour choice (1-3): ").strip()
            
            if choice in ['1', '2', '3']:
                player_choice = self.choices[int(choice) - 1]
                break
            else:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
        
        # Computer makes a choice
        computer_choice = random.choice(self.choices)
        
        # Animate thinking
        print("\n🤔 Computer is choosing", end='', flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end='', flush=True)
        print("\n")
        
        # Display choices
        self.display_choices(player_choice, computer_choice)
        
        # Determine winner
        result = self.get_winner(player_choice, computer_choice)
        
        self.rounds_played += 1
        
        if result == 'player':
            self.player_score += 1
            print("\n🎉 YOU WIN THIS ROUND! 🎉")
        elif result == 'computer':
            self.computer_score += 1
            print("\n💻 COMPUTER WINS THIS ROUND! 💻")
        else:
            self.ties += 1
            print("\n🤝 IT'S A TIE! 🤝")
        
        print("\n" + "─"*50)
        print(f"Score - You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        print("─"*50)
    
    def best_of_game(self, rounds):
        """Play best of N rounds"""
        target = (rounds // 2) + 1
        
        print(f"\n🎮 Best of {rounds} rounds!")
        print(f"First to {target} wins!\n")
        
        temp_player = 0
        temp_computer = 0
        temp_rounds = 0
        
        while temp_player < target and temp_computer < target:
            self.play_round()
            temp_rounds += 1
            
            # Update temporary scores based on last round result
            if self.rounds_played > 0:
                temp_player = self.player_score - (self.player_score - temp_player - (1 if self.player_score > temp_player else 0))
                temp_computer = self.computer_score - (self.computer_score - temp_computer - (1 if self.computer_score > temp_computer else 0))
            
            if temp_player < target and temp_computer < target:
                continue_game = input("\nContinue to next round? (y/n): ").strip().lower()
                if continue_game != 'y':
                    return
        
        # Game over
        print("\n" + "="*50)
        print("🏆 GAME OVER! 🏆")
        print("="*50)
        
        if self.player_score > self.computer_score:
            print("🎊 YOU ARE THE CHAMPION! 🎊")
        elif self.computer_score > self.player_score:
            print("💻 COMPUTER IS THE CHAMPION! 💻")
        else:
            print("🤝 IT'S A TIE GAME! 🤝")
        
        print(f"\nFinal Score: You {self.player_score} - {self.computer_score} Computer")
        print("="*50)
    
    def reset_scores(self):
        """Reset all scores"""
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0


def run():
    """Main function for rock paper scissors"""
    
    game = RockPaperScissors()
    
    while True:
        print("\n" + "="*50)
        print("🪨📄✂️  ROCK PAPER SCISSORS  🪨📄✂️")
        print("="*50)
        
        if game.rounds_played > 0:
            print(f"\n📊 Session Stats:")
            print(f"   Rounds Played: {game.rounds_played}")
            print(f"   Your Wins: {game.player_score}")
            print(f"   Computer Wins: {game.computer_score}")
            print(f"   Ties: {game.ties}")
            
            if game.rounds_played > 0:
                win_rate = (game.player_score / game.rounds_played * 100)
                print(f"   Your Win Rate: {win_rate:.1f}%")
            
            print("─"*50)
        
        print("\nGame Modes:")
        print("  1. Single Round")
        print("  2. Best of 3")
        print("  3. Best of 5")
        print("  4. Best of 7")
        print("  5. Play until you want to stop")
        print("  6. Reset statistics")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            game.play_round()
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            game.best_of_game(3)
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            game.best_of_game(5)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            game.best_of_game(7)
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            print("\n🎮 Continuous Play Mode")
            print("Type 'quit' when you want to stop\n")
            
            while True:
                game.play_round()
                
                continue_playing = input("\nPlay another round? (y/n): ").strip().lower()
                if continue_playing != 'y':
                    break
            
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            confirm = input("\n⚠️  Reset all statistics? (yes/no): ").strip().lower()
            if confirm == 'yes':
                game.reset_scores()
                print("✅ Statistics reset!")
            else:
                print("❌ Reset cancelled.")
            
            time.sleep(1)
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()