#!/usr/bin/env python3
"""
Tic Tac Toe
Classic game with different difficulty levels
"""

import random
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self.games_played = 0
    
    def print_board(self):
        """Display the game board"""
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('  ' + ' | '.join(row))
            if row != self.board[6:9]:
                print('  ---------')
        print("\n")
    
    def print_board_nums(self):
        """Display board positions"""
        print("\n  Board Positions:")
        print("  1 | 2 | 3")
        print("  ---------")
        print("  4 | 5 | 6")
        print("  ---------")
        print("  7 | 8 | 9\n")
    
    def available_moves(self):
        """Return list of available moves"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        """Check if there are empty squares"""
        return ' ' in self.board
    
    def num_empty_squares(self):
        """Count empty squares"""
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        """Make a move on the board"""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        """Check if there's a winner"""
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False
    
    def reset_board(self):
        """Reset the board for a new game"""
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


class ComputerPlayer:
    def __init__(self, letter, difficulty='medium'):
        self.letter = letter
        self.difficulty = difficulty
    
    def get_move(self, game):
        """Get computer's move based on difficulty"""
        if self.difficulty == 'easy':
            return self.easy_move(game)
        elif self.difficulty == 'medium':
            return self.medium_move(game)
        else:
            return self.hard_move(game)
    
    def easy_move(self, game):
        """Easy: Random moves"""
        return random.choice(game.available_moves())
    
    def medium_move(self, game):
        """Medium: Block obvious wins, otherwise random"""
        # Try to win if possible
        for move in game.available_moves():
            test_board = game.board.copy()
            test_board[move] = self.letter
            if self.check_winner(test_board, move, self.letter):
                return move
        
        # Block opponent's winning move
        opponent = 'O' if self.letter == 'X' else 'X'
        for move in game.available_moves():
            test_board = game.board.copy()
            test_board[move] = opponent
            if self.check_winner(test_board, move, opponent):
                return move
        
        # Otherwise random
        return random.choice(game.available_moves())
    
    def hard_move(self, game):
        """Hard: Minimax algorithm"""
        if len(game.available_moves()) == 9:
            return random.choice([0, 2, 4, 6, 8])  # Start with corner or center
        
        best_score = -float('inf')
        best_move = None
        
        for move in game.available_moves():
            game.board[move] = self.letter
            score = self.minimax(game, False)
            game.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def minimax(self, game, is_maximizing):
        """Minimax algorithm for optimal play"""
        opponent = 'O' if self.letter == 'X' else 'X'
        
        # Check terminal states
        if game.current_winner == self.letter:
            return 1
        elif game.current_winner == opponent:
            return -1
        elif not game.empty_squares():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for move in game.available_moves():
                game.board[move] = self.letter
                if game.winner(move, self.letter):
                    game.current_winner = self.letter
                score = self.minimax(game, False)
                game.board[move] = ' '
                game.current_winner = None
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in game.available_moves():
                game.board[move] = opponent
                if game.winner(move, opponent):
                    game.current_winner = opponent
                score = self.minimax(game, True)
                game.board[move] = ' '
                game.current_winner = None
                best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, board, square, letter):
        """Check if move creates a winner"""
        # Check row
        row_ind = square // 3
        row = board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False


def play_game(game, difficulty='medium'):
    """Play a single game"""
    game.reset_board()
    game.print_board_nums()
    
    # Player is X, Computer is O
    player_letter = 'X'
    computer = ComputerPlayer('O', difficulty)
    
    current_letter = 'X'  # X goes first
    
    while game.empty_squares():
        if current_letter == player_letter:
            # Player's turn
            game.print_board()
            print("Your turn (X)")
            
            while True:
                try:
                    square = int(input("Enter position (1-9): ").strip()) - 1
                    if square in game.available_moves():
                        break
                    else:
                        print("❌ That space is taken!")
                except ValueError:
                    print("❌ Invalid input! Enter a number 1-9.")
        else:
            # Computer's turn
            print("\n🤖 Computer is thinking", end='', flush=True)
            for _ in range(3):
                time.sleep(0.3)
                print(".", end='', flush=True)
            print("\n")
            
            square = computer.get_move(game)
            print(f"Computer chose position {square + 1}")
            time.sleep(0.5)
        
        game.make_move(square, current_letter)
        
        if game.current_winner:
            game.print_board()
            if current_letter == player_letter:
                print("🎉 YOU WIN! 🎉")
                game.player_wins += 1
            else:
                print("💻 COMPUTER WINS! 💻")
                game.computer_wins += 1
            game.games_played += 1
            return
        
        # Switch turns
        current_letter = 'O' if current_letter == 'X' else 'X'
    
    # No winner - it's a tie
    game.print_board()
    print("🤝 IT'S A TIE! 🤝")
    game.ties += 1
    game.games_played += 1


def two_player_game(game):
    """Two player mode"""
    game.reset_board()
    game.print_board_nums()
    
    current_letter = 'X'
    
    while game.empty_squares():
        game.print_board()
        print(f"\nPlayer {current_letter}'s turn")
        
        while True:
            try:
                square = int(input("Enter position (1-9): ").strip()) - 1
                if square in game.available_moves():
                    break
                else:
                    print("❌ That space is taken!")
            except ValueError:
                print("❌ Invalid input! Enter a number 1-9.")
        
        game.make_move(square, current_letter)
        
        if game.current_winner:
            game.print_board()
            print(f"🎉 PLAYER {current_letter} WINS! 🎉")
            return
        
        current_letter = 'O' if current_letter == 'X' else 'X'
    
    game.print_board()
    print("🤝 IT'S A TIE! 🤝")


def run():
    """Main function for tic tac toe"""
    
    game = TicTacToe()
    
    while True:
        print("\n" + "="*50)
        print("❌⭕  TIC TAC TOE  ❌⭕")
        print("="*50)
        
        if game.games_played > 0:
            print(f"\n📊 Statistics:")
            print(f"   Games Played: {game.games_played}")
            print(f"   Your Wins: {game.player_wins}")
            print(f"   Computer Wins: {game.computer_wins}")
            print(f"   Ties: {game.ties}")
            
            if game.games_played > 0:
                win_rate = (game.player_wins / game.games_played * 100)
                print(f"   Your Win Rate: {win_rate:.1f}%")
            
            print("─"*50)
        
        print("\nGame Modes:")
        print("  1. Play vs Computer (Easy)")
        print("  2. Play vs Computer (Medium)")
        print("  3. Play vs Computer (Hard)")
        print("  4. Two Player Mode")
        print("  5. Reset Statistics")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            play_game(game, difficulty='easy')
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            play_game(game, difficulty='medium')
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            print("\n⚠️  Hard mode: Computer plays perfectly!")
            input("Press Enter to start...")
            play_game(game, difficulty='hard')
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print("\n👥 Two Player Mode")
            print("Player 1 is X, Player 2 is O\n")
            two_player_game(game)
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            confirm = input("\n⚠️  Reset all statistics? (yes/no): ").strip().lower()
            if confirm == 'yes':
                game.player_wins = 0
                game.computer_wins = 0
                game.ties = 0
                game.games_played = 0
                print("✅ Statistics reset!")
            else:
                print("❌ Reset cancelled.")
            time.sleep(1)
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()