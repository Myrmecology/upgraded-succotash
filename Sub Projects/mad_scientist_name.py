#!/usr/bin/env python3
"""
Mad Scientist Name Generator
Generate hilarious mad scientist names and evil schemes
"""

import random
import time


# Name components
TITLES = [
    "Dr.", "Professor", "Doctor", "Lord", "Baron", "Count",
    "Doktor", "Herr Doktor", "Mad", "The Insane", "The Deranged"
]

FIRST_NAMES = [
    "Victor", "Heinrich", "Ignatius", "Mortimer", "Cornelius",
    "Erasmus", "Hieronymus", "Nikola", "Emmett", "Herbert",
    "Lazarus", "Percival", "Quentin", "Reginald", "Thaddeus",
    "Ulysses", "Wendell", "Xavier", "Zachary", "Igor",
    "Vlad", "Boris", "Klaus", "Franz", "Otto"
]

LAST_NAMES = [
    "Frankenstein", "Von Doom", "Strangelove", "Moriarty", "Calamari",
    "Catastrophe", "Chaos", "Destruction", "Evil", "Fiendish",
    "Gruesome", "Horrible", "Insidious", "Malevolent", "Nefarious",
    "Ominous", "Perilous", "Sinister", "Terrible", "Vicious",
    "Wicked", "Diabolical", "Maniacal", "Demented", "Twisted",
    "Von Brainstorm", "McEvil", "O'Terror", "De La Muerte"
]

SUFFIXES = [
    "III", "Jr.", "Sr.", "the Terrible", "the Mad", "the Insane",
    "the Diabolical", "the Maniacal", "the Evil", "PhD", "Esq.",
    "the Deranged", "the Twisted", "the Wicked"
]

# Laboratory equipment
LAB_EQUIPMENT = [
    "Tesla Coil", "Death Ray", "Doomsday Device", "Time Machine",
    "Mind Control Helmet", "Robot Army", "Weather Machine", "Shrink Ray",
    "Giant Laser", "Mutation Chamber", "Clone Vat", "Teleporter",
    "Freeze Ray", "Molecular Disintegrator", "Dimensional Portal",
    "Brain Swapper", "Monster Creator", "Evil Computer", "Giant Magnet"
]

# Evil schemes
EVIL_SCHEMES = [
    "take over the world",
    "destroy the moon",
    "create an army of mutants",
    "steal all the world's chocolate",
    "turn everyone into chickens",
    "reverse the Earth's rotation",
    "block out the sun",
    "create a volcano in the city",
    "freeze the entire ocean",
    "make everyone dance uncontrollably",
    "switch everyone's minds",
    "shrink all the world leaders",
    "turn gravity upside down",
    "create a black hole in my basement",
    "make cats rule the world",
    "erase all memories of pizza",
    "turn the sky purple permanently",
    "make it rain backwards"
]

# Minions
MINIONS = [
    "an army of robots", "genetically modified sharks", "zombie accountants",
    "flying monkeys", "evil penguins", "mutant squirrels", "laser-equipped cats",
    "sentient computers", "brain-washed minions", "clone warriors",
    "mechanical spiders", "intelligent fungi", "cyber-enhanced hamsters",
    "telepathic goldfish", "ninja turtles (the evil kind)"
]

# Laboratory locations
LOCATIONS = [
    "a secret volcano lair", "an abandoned castle", "a hidden underwater base",
    "a space station", "a hollowed-out mountain", "beneath the city sewers",
    "an invisible floating fortress", "inside an active volcano", "on the dark side of the moon",
    "a secret island", "an abandoned subway station", "a remote arctic facility"
]


def generate_scientist_name():
    """Generate a random mad scientist name"""
    title = random.choice(TITLES)
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    
    # Sometimes add a suffix
    if random.random() > 0.5:
        suffix = random.choice(SUFFIXES)
        return f"{title} {first} {last}, {suffix}"
    else:
        return f"{title} {first} {last}"


def generate_evil_plan():
    """Generate a complete evil plan"""
    scientist = generate_scientist_name()
    equipment = random.choice(LAB_EQUIPMENT)
    scheme = random.choice(EVIL_SCHEMES)
    minion = random.choice(MINIONS)
    location = random.choice(LOCATIONS)
    
    plan = {
        'name': scientist,
        'equipment': equipment,
        'scheme': scheme,
        'minions': minion,
        'location': location
    }
    
    return plan


def display_evil_plan(plan):
    """Display the evil plan dramatically"""
    print("\n" + "="*50)
    print("🧪 EVIL SCIENTIST PROFILE 🧪")
    print("="*50)
    print(f"\n👨‍🔬 Name: {plan['name']}")
    print(f"\n📍 Secret Laboratory: Located in {plan['location']}")
    print(f"\n⚡ Primary Weapon: {plan['equipment']}")
    print(f"\n😈 Evil Scheme: To {plan['scheme']}!")
    print(f"\n🤖 Minions: Commanding {plan['minions']}")
    print("\n" + "="*50)


def create_origin_story(name):
    """Generate a random origin story"""
    accidents = [
        "struck by lightning during a freak storm",
        "exposed to mysterious radiation",
        "bitten by a radioactive calculator",
        "trapped in a time loop",
        "rejected from science fair",
        "laughed at by the scientific community",
        "denied tenure at the university",
        "their pet goldfish was mocked",
        "failed chemistry class in high school",
        "their invention was stolen"
    ]
    
    motivations = [
        "they vowed revenge on humanity",
        "they swore to prove everyone wrong",
        "they decided to reshape the world",
        "they embraced their dark destiny",
        "they chose the path of evil science",
        "they dedicated their life to chaos",
        "they became obsessed with power"
    ]
    
    accident = random.choice(accidents)
    motivation = random.choice(motivations)
    
    print("\n" + "="*50)
    print("📖 ORIGIN STORY")
    print("="*50)
    print(f"\n{name} wasn't always evil...")
    time.sleep(1)
    print(f"\nBut everything changed when they were {accident}.")
    time.sleep(1)
    print(f"\nFrom that day forward, {motivation}!")
    print("\n" + "="*50)


def run():
    """Main function for mad scientist name generator"""
    
    while True:
        print("\n" + "="*40)
        print("🧪  MAD SCIENTIST NAME GENERATOR  🧪")
        print("="*40)
        print("\nOptions:")
        print("  1. Generate Scientist Name")
        print("  2. Generate Complete Evil Plan")
        print("  3. Generate Origin Story")
        print("  4. Generate 5 Scientists")
        print("  5. Create Your Own Scientist")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            print("\n⚡ Generating mad scientist...")
            time.sleep(0.5)
            name = generate_scientist_name()
            print("\n" + "="*50)
            print(f"👨‍🔬 {name}")
            print("="*50)
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            print("\n⚡ Concocting evil plan...")
            time.sleep(1)
            plan = generate_evil_plan()
            display_evil_plan(plan)
            
            add_story = input("\nGenerate origin story? (yes/no): ").strip().lower()
            if add_story in ['yes', 'y']:
                create_origin_story(plan['name'])
            
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            print("\n⚡ Generating scientist...")
            time.sleep(0.5)
            name = generate_scientist_name()
            create_origin_story(name)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print("\n⚡ Creating 5 mad scientists...\n")
            time.sleep(0.5)
            print("="*50)
            for i in range(5):
                name = generate_scientist_name()
                print(f"{i+1}. {name}")
                time.sleep(0.3)
            print("="*50)
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            print("\n🧪 Create Your Own Mad Scientist!")
            print("="*50)
            
            custom_first = input("Enter first name (or press Enter for random): ").strip()
            custom_last = input("Enter last name (or press Enter for random): ").strip()
            
            first = custom_first if custom_first else random.choice(FIRST_NAMES)
            last = custom_last if custom_last else random.choice(LAST_NAMES)
            title = random.choice(TITLES)
            
            custom_name = f"{title} {first} {last}"
            
            scheme = random.choice(EVIL_SCHEMES)
            equipment = random.choice(LAB_EQUIPMENT)
            
            print("\n" + "="*50)
            print(f"👨‍🔬 Name: {custom_name}")
            print(f"⚡ Weapon: {equipment}")
            print(f"😈 Scheme: To {scheme}!")
            print("="*50)
            
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()