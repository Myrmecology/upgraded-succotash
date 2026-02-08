#!/usr/bin/env python3
"""
Mini Chatbot
A simple rule-based chatbot with personality
"""

import random
import time
import re


class MiniChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.user_name = None
        self.conversation_count = 0
        
        # Response patterns
        self.patterns = {
            r'\b(hi|hello|hey|greetings)\b': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to see you!",
                "Greetings! How are you doing?"
            ],
            r'\b(how are you|how\'s it going|what\'s up)\b': [
                "I'm doing great, thanks for asking!",
                "I'm wonderful! How about you?",
                "Fantastic! Just here chatting with you!",
                "I'm excellent! Ready to chat!"
            ],
            r'\b(your name|who are you|what are you)\b': [
                f"I'm {self.name}, your friendly chatbot!",
                f"My name is {self.name}. Nice to meet you!",
                f"I'm {self.name}, a simple but enthusiastic chatbot!",
            ],
            r'\b(my name is|i\'m|i am) (\w+)': [
                "Nice to meet you, {name}!",
                "Hello {name}! Great to chat with you!",
                "Welcome {name}! How can I help you?",
            ],
            r'\b(bye|goodbye|see you|exit|quit)\b': [
                "Goodbye! It was nice chatting with you!",
                "See you later! Come back soon!",
                "Bye! Have a wonderful day!",
                "Take care! Chat with you again soon!"
            ],
            r'\b(thank you|thanks|thx)\b': [
                "You're very welcome!",
                "Happy to help!",
                "Anytime! That's what I'm here for!",
                "My pleasure!"
            ],
            r'\b(joke|funny|laugh)\b': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "What do you call a bear with no teeth? A gummy bear!",
                "Why don't eggs tell jokes? They'd crack each other up!",
            ],
            r'\b(weather|temperature|forecast)\b': [
                "I'm not connected to weather services, but I hope it's nice where you are!",
                "I don't have weather data, but maybe check a weather app?",
                "Sorry, I can't check the weather, but I hope it's pleasant!",
            ],
            r'\b(age|old|years)\b': [
                "I'm timeless! Or maybe just very young in internet years.",
                "Age is just a number, especially for chatbots!",
                "I was born when you started this program!",
            ],
            r'\b(love|like) you\b': [
                "Aww, I like you too!",
                "That's so sweet! I enjoy chatting with you!",
                "You're making me blush! Well, if I could blush...",
            ],
            r'\b(help|what can you do|capabilities)\b': [
                "I can chat about various topics, tell jokes, and try to be helpful!",
                "I'm here to have a friendly conversation with you!",
                "I can respond to greetings, questions, and general chat. Try asking me something!",
            ],
            r'\b(smart|intelligent|clever)\b': [
                "I try my best! Though I'm just a simple chatbot.",
                "Thanks! I'm learning from every conversation.",
                "You're too kind! I'm just following patterns.",
            ],
            r'\b(sad|unhappy|depressed|down)\b': [
                "I'm sorry you're feeling down. Want to talk about it?",
                "That's tough. Is there anything I can do to help cheer you up?",
                "I'm here to listen if you want to share what's bothering you.",
            ],
            r'\b(happy|excited|great|wonderful)\b': [
                "That's wonderful! I'm happy for you!",
                "Awesome! Your positive energy is contagious!",
                "That's great to hear! Keep that positive vibe going!",
            ],
        }
        
        # Default responses
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. Can you elaborate on that?",
            "Hmm, I'm not sure I understand completely.",
            "That's a good point!",
            "Interesting perspective!",
            "I hear you. What else is on your mind?",
            "Could you rephrase that?",
            "I'm still learning. Can you say that differently?",
        ]
    
    def find_name(self, text):
        """Extract name from user input"""
        match = re.search(r'\b(my name is|i\'m|i am) (\w+)', text, re.IGNORECASE)
        if match:
            return match.group(2)
        return None
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        user_input_lower = user_input.lower()
        
        # Check if user is sharing their name
        name = self.find_name(user_input_lower)
        if name:
            self.user_name = name.capitalize()
        
        # Check patterns
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input_lower):
                response = random.choice(responses)
                # Replace {name} placeholder
                if '{name}' in response and self.user_name:
                    response = response.replace('{name}', self.user_name)
                elif '{name}' in response and name:
                    response = response.replace('{name}', name.capitalize())
                return response
        
        # No pattern matched, use default response
        return random.choice(self.default_responses)
    
    def is_goodbye(self, text):
        """Check if user is saying goodbye"""
        return bool(re.search(r'\b(bye|goodbye|exit|quit|see you)\b', text.lower()))


def run():
    """Main function for mini chatbot"""
    bot = MiniChatbot()
    
    print("\n" + "="*50)
    print("🤖  MINI CHATBOT  🤖")
    print("="*50)
    print(f"\nHello! I'm {bot.name}, your friendly chatbot!")
    print("Type 'bye', 'goodbye', or 'quit' to exit.\n")
    print("─"*50)
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                print(f"{bot.name}: Please say something!")
                continue
            
            bot.conversation_count += 1
            
            # Check for goodbye
            if bot.is_goodbye(user_input):
                response = bot.get_response(user_input)
                print(f"{bot.name}: {response}")
                
                # Ask if they want to return to main menu
                print("\n" + "─"*50)
                choice = input("\nReturn to main menu? (yes/no): ").strip().lower()
                if choice in ['yes', 'y', '']:
                    break
                else:
                    print(f"\n{bot.name}: Great! Let's keep chatting then!")
                    continue
            
            # Get and display response
            response = bot.get_response(user_input)
            
            # Simulate thinking
            time.sleep(0.3)
            print(f"{bot.name}: {response}")
            
            # Occasional personality moments
            if bot.conversation_count % 10 == 0:
                time.sleep(0.5)
                print(f"{bot.name}: Wow, we've been chatting for a while! I'm enjoying this!")
        
        except KeyboardInterrupt:
            print(f"\n\n{bot.name}: Goodbye! Thanks for chatting!")
            break
        except EOFError:
            print(f"\n{bot.name}: Goodbye!")
            break
    
    print("\n" + "="*50)
    print(f"💬 Chat Statistics:")
    print(f"   Messages exchanged: {bot.conversation_count}")
    if bot.user_name:
        print(f"   User: {bot.user_name}")
    print("="*50)


if __name__ == "__main__":
    run()