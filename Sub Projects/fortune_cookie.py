#!/usr/bin/env python3
"""
Fortune Cookie
Get random fortunes, lucky numbers, and wise sayings
"""

import random
import time


# Collection of fortunes
FORTUNES = [
    "A beautiful, smart, and loving person will be coming into your life.",
    "A dubious friend may be an enemy in camouflage.",
    "A feather in the hand is better than a bird in the air.",
    "A fresh start will put you on your way.",
    "A golden egg of opportunity falls into your lap this month.",
    "A good time to finish up old tasks.",
    "A hunch is creativity trying to tell you something.",
    "A lifetime of happiness lies ahead of you.",
    "A light heart carries you through all the hard times.",
    "A new perspective will come with the new year.",
    "A pleasant surprise is waiting for you.",
    "A short pencil is usually better than a long memory any day.",
    "A smooth long journey! Great expectations.",
    "A soft voice may be awfully persuasive.",
    "Adventure can be real happiness.",
    "All your hard work will soon pay off.",
    "Be careful or you could fall for some tricks today.",
    "Because you demand more from yourself, others respect you deeply.",
    "Believe in yourself and others will too.",
    "Better ask twice than lose yourself once.",
    "Courage is not simply one of the virtues, but the form of every virtue.",
    "Curiosity kills boredom. Nothing can kill curiosity.",
    "Dedicate yourself with a calm mind to the task at hand.",
    "Determination is what you need now.",
    "Do not be intimidated by the eloquence of others.",
    "Don't just think, act!",
    "Embrace this love relationship you have!",
    "Every flower blooms in its own sweet time.",
    "Executive ability is prominent in your make-up.",
    "Good news will come to you by mail.",
    "Hard work pays off in the future, laziness pays off now.",
    "Have a beautiful day.",
    "In the end, all things will be known.",
    "It is better to be an optimist and proven a fool than to be a pessimist and be proven right.",
    "It takes courage to admit fault.",
    "Keep your face to the sunshine and you will never see shadows.",
    "Let the world be filled with tranquility and goodwill.",
    "Listen to everyone. Ideas come from everywhere.",
    "Many receive advice, few profit by it.",
    "Nature, time and patience are the three great physicians.",
    "Now is the time to try something new.",
    "Opportunity knocks softly, listen carefully.",
    "People find you attractive. Your personality sparkles.",
    "Plan for many pleasures ahead.",
    "Success is a journey, not a destination.",
    "The best prediction of future is the past.",
    "The harder you work, the luckier you get.",
    "The only way to discover the limits of the possible is to go beyond them.",
    "The star of riches is shining upon you.",
    "There is no greater pleasure than seeing your loved ones prosper.",
    "Time is precious, but truth is more precious than time.",
    "Today is the conserve yourself, as things just won't budge.",
    "Welcome change.",
    "You are a lover of words; one day you will write a book.",
    "You are never selfish with your advice or your help.",
    "You are talented in many ways.",
    "You will be successful in your work.",
    "Your ability to juggle many tasks will take you far.",
    "Your life will be happy and peaceful.",
    "Your talents will be recognized and suitably rewarded.",
]


# Wise sayings
WISE_SAYINGS = [
    "A journey of a thousand miles begins with a single step.",
    "The wise man adapts himself to circumstances, as water shapes itself to the vessel.",
    "To know what is right and not do it is the worst cowardice.",
    "When the winds of change blow, some build walls, others build windmills.",
    "The gem cannot be polished without friction, nor man perfected without trials.",
    "Give a man a fish and you feed him for a day. Teach him how to fish and you feed him for a lifetime.",
    "He who knows others is wise. He who knows himself is enlightened.",
    "A single conversation with a wise man is better than ten years of study.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Fall seven times, stand up eight.",
]


def generate_lucky_numbers():
    """Generate 6 lucky numbers"""
    return sorted(random.sample(range(1, 50), 6))


def crack_fortune():
    """Simulate cracking open a fortune cookie with animation"""
    print("\n🥠 Cracking open your fortune cookie...")
    time.sleep(0.5)
    
    animation = ["_", "\\", "|", "/"]
    for _ in range(8):
        for frame in animation:
            print(f"\r  {frame}", end='', flush=True)
            time.sleep(0.1)
    
    print("\r💥 *CRACK!*")
    time.sleep(0.5)


def display_fortune():
    """Display a random fortune"""
    crack_fortune()
    
    fortune = random.choice(FORTUNES)
    lucky_nums = generate_lucky_numbers()
    
    print("\n" + "="*50)
    print("📜 YOUR FORTUNE:")
    print("="*50)
    print(f"\n   {fortune}\n")
    print("─"*50)
    print(f"🍀 Lucky Numbers: {', '.join(map(str, lucky_nums))}")
    print("="*50)


def display_wise_saying():
    """Display a random wise saying"""
    print("\n🧙 Opening ancient scroll...")
    time.sleep(1)
    
    saying = random.choice(WISE_SAYINGS)
    
    print("\n" + "="*50)
    print("💡 ANCIENT WISDOM:")
    print("="*50)
    print(f"\n   {saying}\n")
    print("="*50)


def fortune_with_numbers():
    """Get fortune with specific lucky number count"""
    try:
        count = int(input("\nHow many lucky numbers? (1-10): ").strip())
        if 1 <= count <= 10:
            crack_fortune()
            
            fortune = random.choice(FORTUNES)
            lucky_nums = sorted(random.sample(range(1, 100), count))
            
            print("\n" + "="*50)
            print("📜 YOUR FORTUNE:")
            print("="*50)
            print(f"\n   {fortune}\n")
            print("─"*50)
            print(f"🍀 Lucky Numbers: {', '.join(map(str, lucky_nums))}")
            print("="*50)
        else:
            print("❌ Please enter a number between 1 and 10.")
    except ValueError:
        print("❌ Invalid input!")


def run():
    """Main function for fortune cookie"""
    
    while True:
        print("\n" + "="*40)
        print("🥠  FORTUNE COOKIE  🥠")
        print("="*40)
        print("\nOptions:")
        print("  1. Crack a Fortune Cookie")
        print("  2. Get Ancient Wisdom")
        print("  3. Custom Lucky Numbers")
        print("  4. Get 5 Fortunes")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            display_fortune()
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            display_wise_saying()
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            fortune_with_numbers()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print("\n🥠 Cracking 5 fortune cookies...\n")
            for i in range(5):
                print(f"\n--- Fortune #{i+1} ---")
                fortune = random.choice(FORTUNES)
                print(f"📜 {fortune}")
                time.sleep(0.5)
            
            lucky_nums = generate_lucky_numbers()
            print(f"\n🍀 Bonus Lucky Numbers: {', '.join(map(str, lucky_nums))}")
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()