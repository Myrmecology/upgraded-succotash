#!/usr/bin/env python3
"""
Random Jokes Generator
Get random jokes from different categories
"""

import random
import time


# Joke collections by category
JOKES = {
    'Programming': [
        {
            'setup': 'Why do programmers prefer dark mode?',
            'punchline': 'Because light attracts bugs!'
        },
        {
            'setup': 'Why do Java developers wear glasses?',
            'punchline': "Because they don't C#!"
        },
        {
            'setup': 'How many programmers does it take to change a light bulb?',
            'punchline': "None. It's a hardware problem!"
        },
        {
            'setup': 'Why did the programmer quit his job?',
            'punchline': "Because he didn't get arrays!"
        },
        {
            'setup': 'What is a programmer\'s favorite hangout place?',
            'punchline': 'Foo Bar!'
        },
        {
            'setup': 'Why did the database administrator leave his wife?',
            'punchline': 'She had one-to-many relationships!'
        },
    ],
    'Dad Jokes': [
        {
            'setup': 'Why don\'t scientists trust atoms?',
            'punchline': 'Because they make up everything!'
        },
        {
            'setup': 'What do you call a fake noodle?',
            'punchline': 'An impasta!'
        },
        {
            'setup': 'Why did the scarecrow win an award?',
            'punchline': 'He was outstanding in his field!'
        },
        {
            'setup': 'What do you call cheese that isn\'t yours?',
            'punchline': 'Nacho cheese!'
        },
        {
            'setup': 'How does a penguin build its house?',
            'punchline': 'Igloos it together!'
        },
        {
            'setup': 'Why can\'t a bicycle stand on its own?',
            'punchline': "It's two tired!"
        },
    ],
    'Knock Knock': [
        {
            'setup': 'Knock knock.\nWho\'s there?\nBoo.\nBoo who?',
            'punchline': "Don't cry, it's just a joke!"
        },
        {
            'setup': 'Knock knock.\nWho\'s there?\nLettuce.\nLettuce who?',
            'punchline': 'Lettuce in, it\'s cold out here!'
        },
        {
            'setup': 'Knock knock.\nWho\'s there?\nInterrupting cow.\nInterrupting cow w—',
            'punchline': 'MOOOOO!'
        },
        {
            'setup': 'Knock knock.\nWho\'s there?\nDwayne.\nDwayne who?',
            'punchline': 'Dwayne the bathtub, I\'m dwowning!'
        },
        {
            'setup': 'Knock knock.\nWho\'s there?\nHoney bee.\nHoney bee who?',
            'punchline': 'Honey bee a dear and get me some water!'
        },
    ],
    'One-Liners': [
        {
            'setup': '',
            'punchline': "I told my wife she was drawing her eyebrows too high. She looked surprised."
        },
        {
            'setup': '',
            'punchline': "I'm reading a book about anti-gravity. It's impossible to put down!"
        },
        {
            'setup': '',
            'punchline': "I used to play piano by ear, but now I use my hands."
        },
        {
            'setup': '',
            'punchline': "Parallel lines have so much in common. It's a shame they'll never meet."
        },
        {
            'setup': '',
            'punchline': "I'm on a seafood diet. I see food and I eat it."
        },
        {
            'setup': '',
            'punchline': "Time flies like an arrow. Fruit flies like a banana."
        },
    ],
    'Animal': [
        {
            'setup': 'What do you call a bear with no teeth?',
            'punchline': 'A gummy bear!'
        },
        {
            'setup': 'Why don\'t elephants use computers?',
            'punchline': "They're afraid of the mouse!"
        },
        {
            'setup': 'What do you call a sleeping bull?',
            'punchline': 'A bulldozer!'
        },
        {
            'setup': 'Why do fish live in salt water?',
            'punchline': 'Because pepper makes them sneeze!'
        },
        {
            'setup': 'What do you call an alligator in a vest?',
            'punchline': 'An investigator!'
        },
        {
            'setup': 'Why don\'t oysters donate to charity?',
            'punchline': "Because they're shellfish!"
        },
    ],
}


def tell_joke(joke, animated=True):
    """Tell a joke with optional animation"""
    if joke['setup']:
        print(f"\n{joke['setup']}")
        
        if animated:
            time.sleep(1.5)
            print("\n.", end='', flush=True)
            time.sleep(0.3)
            print(".", end='', flush=True)
            time.sleep(0.3)
            print(".", end='', flush=True)
            time.sleep(0.5)
            print("\n")
    
    print(f"😄 {joke['punchline']}\n")


def run():
    """Main function for random jokes"""
    
    jokes_told = 0
    favorites = []
    
    while True:
        print("\n" + "="*50)
        print("😂  RANDOM JOKES GENERATOR  😂")
        print("="*50)
        
        if jokes_told > 0:
            print(f"\n📊 Jokes told this session: {jokes_told}")
            if favorites:
                print(f"⭐ Favorites saved: {len(favorites)}")
            print("─"*50)
        
        print("\nJoke Categories:")
        categories = list(JOKES.keys())
        
        for i, category in enumerate(categories, 1):
            print(f"  {i}. {category} ({len(JOKES[category])} jokes)")
        
        print(f"  {len(categories) + 1}. Random joke (any category)")
        print(f"  {len(categories) + 2}. Tell multiple jokes")
        print(f"  {len(categories) + 3}. View favorites")
        print(f"  0. Return to Main Menu")
        
        try:
            choice = input("\nYour choice: ").strip()
            
            if choice == "0":
                break
            
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(categories):
                # Specific category
                category = categories[choice_num - 1]
                joke = random.choice(JOKES[category])
                
                print("\n" + "─"*50)
                print(f"📁 Category: {category}")
                print("─"*50)
                
                tell_joke(joke)
                jokes_told += 1
                
                # Ask if they want to save as favorite
                save = input("⭐ Save as favorite? (y/n): ").strip().lower()
                if save == 'y':
                    favorites.append(joke)
                    print("✅ Saved to favorites!")
                
                input("\nPress Enter for another joke...")
            
            elif choice_num == len(categories) + 1:
                # Random joke from any category
                all_jokes = []
                for jokes_list in JOKES.values():
                    all_jokes.extend(jokes_list)
                
                joke = random.choice(all_jokes)
                
                print("\n" + "─"*50)
                print("🎲 Random Joke")
                print("─"*50)
                
                tell_joke(joke)
                jokes_told += 1
                
                # Ask if they want to save as favorite
                save = input("⭐ Save as favorite? (y/n): ").strip().lower()
                if save == 'y':
                    favorites.append(joke)
                    print("✅ Saved to favorites!")
                
                input("\nPress Enter for another joke...")
            
            elif choice_num == len(categories) + 2:
                # Tell multiple jokes
                num = input("\nHow many jokes? (1-10): ").strip()
                try:
                    num_jokes = int(num)
                    if 1 <= num_jokes <= 10:
                        all_jokes = []
                        for jokes_list in JOKES.values():
                            all_jokes.extend(jokes_list)
                        
                        selected_jokes = random.sample(all_jokes, min(num_jokes, len(all_jokes)))
                        
                        print(f"\n🎭 Here are {len(selected_jokes)} jokes!\n")
                        print("="*50)
                        
                        for i, joke in enumerate(selected_jokes, 1):
                            print(f"\n--- Joke #{i} ---")
                            tell_joke(joke, animated=False)
                            time.sleep(1)
                        
                        jokes_told += len(selected_jokes)
                        print("="*50)
                    else:
                        print("❌ Please enter a number between 1 and 10!")
                except ValueError:
                    print("❌ Invalid number!")
                
                input("\nPress Enter to continue...")
            
            elif choice_num == len(categories) + 3:
                # View favorites
                if favorites:
                    print("\n" + "="*50)
                    print(f"⭐ YOUR FAVORITE JOKES ({len(favorites)})")
                    print("="*50)
                    
                    for i, joke in enumerate(favorites, 1):
                        print(f"\n--- Favorite #{i} ---")
                        tell_joke(joke, animated=False)
                        time.sleep(0.5)
                    
                    print("="*50)
                    
                    # Option to clear favorites
                    clear = input("\nClear all favorites? (y/n): ").strip().lower()
                    if clear == 'y':
                        favorites.clear()
                        print("✅ Favorites cleared!")
                else:
                    print("\n❌ No favorite jokes saved yet!")
                    print("💡 Tip: Save jokes as favorites when you hear them!")
                
                input("\nPress Enter to continue...")
            
            else:
                print("❌ Invalid choice!")
                time.sleep(1)
        
        except ValueError:
            print("❌ Invalid input!")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for laughing with us!")
            break


if __name__ == "__main__":
    run()