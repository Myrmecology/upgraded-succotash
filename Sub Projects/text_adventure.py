#!/usr/bin/env python3
"""
Text Adventure
A simple choose-your-own-adventure game
"""

import time
import random


class TextAdventure:
    def __init__(self):
        self.player_name = ""
        self.inventory = []
        self.health = 100
        self.score = 0
    
    def print_slow(self, text, delay=0.03):
        """Print text with a typing effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def print_header(self, text):
        """Print a section header"""
        print("\n" + "="*50)
        print(text.center(50))
        print("="*50 + "\n")
    
    def show_status(self):
        """Display player status"""
        print(f"\n💚 Health: {self.health}/100 | 🎒 Items: {len(self.inventory)} | ⭐ Score: {self.score}")
    
    def intro(self):
        """Game introduction"""
        self.print_header("🗡️  THE MYSTERIOUS CASTLE 🏰")
        
        self.print_slow("Welcome, brave adventurer!")
        time.sleep(0.5)
        
        name = input("\nWhat is your name? ").strip()
        self.player_name = name if name else "Adventurer"
        
        print(f"\nWelcome, {self.player_name}!")
        time.sleep(1)
        
        self.print_slow("\nYou find yourself standing before a mysterious castle...")
        time.sleep(1)
        self.print_slow("Dark clouds swirl overhead, and you hear strange noises from within.")
        time.sleep(1)
        self.print_slow("Legend says a great treasure lies hidden inside...")
        time.sleep(1)
        self.print_slow("But many who entered never returned...\n")
        time.sleep(1)
        
        input("Press Enter to begin your adventure...")
    
    def castle_entrance(self):
        """First decision point"""
        self.print_header("CASTLE ENTRANCE")
        
        self.print_slow("You stand before the massive castle gates.")
        self.print_slow("To your left, you see a small side door.")
        self.print_slow("To your right, there's a window you could climb through.")
        self.print_slow("The main gate is locked with heavy chains.\n")
        
        print("What do you do?")
        print("  1. Try to break the chains on the main gate")
        print("  2. Go through the side door")
        print("  3. Climb through the window")
        print("  4. Look around for another entrance")
        
        choice = input("\nYour choice (1-4): ").strip()
        
        if choice == "1":
            return self.main_gate()
        elif choice == "2":
            return self.side_door()
        elif choice == "3":
            return self.window_path()
        elif choice == "4":
            return self.search_around()
        else:
            print("\n❌ Invalid choice! Try again.")
            return self.castle_entrance()
    
    def main_gate(self):
        """Main gate path"""
        self.print_header("MAIN GATE")
        
        self.print_slow("You pull at the heavy chains with all your might...")
        time.sleep(1)
        
        if random.random() > 0.7:
            self.print_slow("The chains snap! You're incredibly strong!")
            self.score += 20
            self.print_slow("\n⭐ +20 Score for breaking the chains!")
            return self.grand_hall()
        else:
            self.print_slow("The chains hold firm. You hurt your hands trying.")
            self.health -= 10
            print(f"\n💔 -10 Health")
            self.print_slow("\nYou'll need to find another way in...")
            time.sleep(1)
            return self.castle_entrance()
    
    def side_door(self):
        """Side door path"""
        self.print_header("SIDE DOOR")
        
        self.print_slow("You carefully open the creaky side door...")
        time.sleep(1)
        self.print_slow("It leads to a dark corridor lit by flickering torches.")
        
        self.inventory.append("torch")
        self.score += 10
        print("\n✨ You picked up a TORCH!")
        print("⭐ +10 Score")
        
        time.sleep(1)
        return self.dark_corridor()
    
    def window_path(self):
        """Window climbing path"""
        self.print_header("CLIMBING IN")
        
        self.print_slow("You climb through the window...")
        time.sleep(1)
        
        if random.random() > 0.5:
            self.print_slow("You successfully climb in and find yourself in a library!")
            self.score += 15
            print("\n⭐ +15 Score for stealth!")
            return self.library()
        else:
            self.print_slow("You slip and fall, scraping your knee!")
            self.health -= 15
            print(f"\n💔 -15 Health")
            self.print_slow("You manage to get inside, but you're hurt.")
            return self.library()
    
    def search_around(self):
        """Searching area"""
        self.print_header("SEARCHING")
        
        self.print_slow("You search around the castle perimeter...")
        time.sleep(1)
        self.print_slow("You find a rusty key hidden under a rock!")
        
        self.inventory.append("rusty key")
        self.score += 10
        print("\n✨ You picked up a RUSTY KEY!")
        print("⭐ +10 Score")
        
        time.sleep(1)
        
        self.print_slow("\nThe key might open the side door!")
        return self.side_door()
    
    def dark_corridor(self):
        """Dark corridor encounter"""
        self.print_header("DARK CORRIDOR")
        
        self.print_slow("The corridor is eerily quiet...")
        time.sleep(1)
        self.print_slow("Suddenly, you hear footsteps approaching!")
        time.sleep(1)
        
        print("\nWhat do you do?")
        print("  1. Hide behind a pillar")
        print("  2. Run forward")
        print("  3. Stand your ground")
        
        choice = input("\nYour choice (1-3): ").strip()
        
        if choice == "1":
            self.print_slow("\nYou hide behind a pillar...")
            time.sleep(1)
            self.print_slow("A skeleton guard passes by without noticing you!")
            self.score += 15
            print("\n⭐ +15 Score for stealth!")
            return self.treasure_room()
        elif choice == "2":
            self.print_slow("\nYou run forward blindly...")
            time.sleep(1)
            self.print_slow("You crash into a wall!")
            self.health -= 10
            print(f"\n💔 -10 Health")
            return self.treasure_room()
        else:
            self.print_slow("\nYou stand bravely...")
            time.sleep(1)
            self.print_slow("The skeleton guard challenges you to a riddle!")
            return self.riddle_challenge()
    
    def riddle_challenge(self):
        """Riddle challenge"""
        self.print_header("RIDDLE CHALLENGE")
        
        self.print_slow("The skeleton speaks:")
        time.sleep(1)
        print("\n'I speak without a mouth and hear without ears.")
        print("I have no body, but I come alive with wind.")
        print("What am I?'\n")
        
        print("  1. An echo")
        print("  2. A ghost")
        print("  3. A whisper")
        
        choice = input("\nYour answer (1-3): ").strip()
        
        if choice == "1":
            self.print_slow("\n'Correct!' the skeleton cries.")
            self.print_slow("'You may pass, wise one!'")
            self.score += 25
            print("\n⭐ +25 Score for solving the riddle!")
            self.inventory.append("silver coin")
            print("✨ The skeleton gives you a SILVER COIN!")
            return self.treasure_room()
        else:
            self.print_slow("\n'Wrong!' the skeleton attacks!")
            self.health -= 20
            print(f"\n💔 -20 Health")
            self.print_slow("You manage to escape...")
            return self.treasure_room()
    
    def grand_hall(self):
        """Grand hall"""
        self.print_header("GRAND HALL")
        
        self.print_slow("You enter a magnificent grand hall...")
        time.sleep(1)
        self.print_slow("Suits of armor line the walls.")
        time.sleep(1)
        
        return self.treasure_room()
    
    def library(self):
        """Library room"""
        self.print_header("LIBRARY")
        
        self.print_slow("Ancient books fill the shelves...")
        time.sleep(1)
        self.print_slow("You find a dusty spellbook!")
        
        self.inventory.append("spellbook")
        self.score += 20
        print("\n✨ You picked up a SPELLBOOK!")
        print("⭐ +20 Score")
        
        time.sleep(1)
        return self.treasure_room()
    
    def treasure_room(self):
        """Final treasure room"""
        self.print_header("TREASURE ROOM")
        
        self.print_slow("You enter a room filled with glittering gold!")
        time.sleep(1)
        self.print_slow("In the center sits a magnificent chest...")
        time.sleep(1)
        
        print("\nWhat do you do?")
        print("  1. Open the chest immediately")
        print("  2. Check for traps first")
        print("  3. Take some gold coins and leave")
        
        choice = input("\nYour choice (1-3): ").strip()
        
        if choice == "1":
            if random.random() > 0.6:
                return self.good_ending()
            else:
                return self.trap_ending()
        elif choice == "2":
            return self.careful_ending()
        else:
            return self.quick_ending()
    
    def good_ending(self):
        """Best ending"""
        self.print_header("VICTORY!")
        
        self.print_slow("The chest opens easily...")
        time.sleep(1)
        self.print_slow("Inside, you find the legendary Crown of Heroes!")
        self.score += 100
        time.sleep(1)
        
        self.show_status()
        print("\n🏆 CONGRATULATIONS! You completed the adventure!")
        print(f"⭐ Final Score: {self.score}")
        print(f"🎒 Items collected: {', '.join(self.inventory)}")
        
        return True
    
    def trap_ending(self):
        """Trap ending"""
        self.print_header("TRAPPED!")
        
        self.print_slow("The chest was trapped!")
        time.sleep(1)
        self.print_slow("Poison darts fly everywhere!")
        self.health -= 50
        time.sleep(1)
        
        if self.health > 0:
            self.print_slow("You survive, but barely...")
            self.print_slow("You grab what you can and escape!")
            self.score += 30
            
            self.show_status()
            print("\n✅ You survived! Not bad!")
            print(f"⭐ Final Score: {self.score}")
            return True
        else:
            self.print_slow("The poison overwhelms you...")
            print("\n💀 GAME OVER")
            print(f"⭐ Final Score: {self.score}")
            return False
    
    def careful_ending(self):
        """Careful ending"""
        self.print_header("WISE CHOICE!")
        
        self.print_slow("You carefully examine the chest...")
        time.sleep(1)
        self.print_slow("You find and disarm a trap!")
        self.score += 50
        time.sleep(1)
        self.print_slow("The chest opens safely, revealing incredible treasures!")
        self.score += 100
        
        self.show_status()
        print("\n🏆 PERFECT! Maximum score achieved!")
        print(f"⭐ Final Score: {self.score}")
        print(f"🎒 Items collected: {', '.join(self.inventory)}")
        
        return True
    
    def quick_ending(self):
        """Quick ending"""
        self.print_header("RETREAT")
        
        self.print_slow("You grab handfuls of gold coins...")
        time.sleep(1)
        self.print_slow("And make your escape!")
        self.score += 40
        
        self.show_status()
        print("\n✅ You escaped with some treasure!")
        print(f"⭐ Final Score: {self.score}")
        
        return True


def run():
    """Main function for text adventure"""
    
    while True:
        print("\n" + "="*50)
        print("📖  TEXT ADVENTURE  📖")
        print("="*50)
        print("\nOptions:")
        print("  1. Start New Adventure")
        print("  2. How to Play")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            game = TextAdventure()
            game.intro()
            game.castle_entrance()
            
            input("\n\nPress Enter to continue...")
        
        elif choice == "2":
            print("\n" + "="*50)
            print("HOW TO PLAY")
            print("="*50)
            print("""
🎮 Make choices by entering numbers
💚 Watch your health - don't let it reach 0!
🎒 Collect items to help you on your journey
⭐ Try to get the highest score possible
🏆 Different choices lead to different endings

Tips:
- Be brave but also careful!
- Sometimes patience is rewarded
- Explore thoroughly for bonus items

Good luck, adventurer!
            """)
            print("="*50)
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()