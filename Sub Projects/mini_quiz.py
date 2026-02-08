#!/usr/bin/env python3
"""
Mini Quiz
Multiple choice quiz game with different categories
"""

import random
import time


# Quiz questions by category
QUIZ_DATA = {
    'General Knowledge': [
        {
            'question': 'What is the capital of France?',
            'options': ['London', 'Berlin', 'Paris', 'Madrid'],
            'answer': 2
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
            'answer': 1
        },
        {
            'question': 'Who painted the Mona Lisa?',
            'options': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Michelangelo'],
            'answer': 2
        },
        {
            'question': 'What is the largest ocean on Earth?',
            'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
            'answer': 3
        },
        {
            'question': 'In which year did World War II end?',
            'options': ['1943', '1944', '1945', '1946'],
            'answer': 2
        },
    ],
    'Science': [
        {
            'question': 'What is the chemical symbol for gold?',
            'options': ['Go', 'Gd', 'Au', 'Ag'],
            'answer': 2
        },
        {
            'question': 'How many bones are in the adult human body?',
            'options': ['186', '206', '226', '246'],
            'answer': 1
        },
        {
            'question': 'What is the speed of light in vacuum?',
            'options': ['299,792 km/s', '199,792 km/s', '399,792 km/s', '99,792 km/s'],
            'answer': 0
        },
        {
            'question': 'What is the powerhouse of the cell?',
            'options': ['Nucleus', 'Ribosome', 'Mitochondria', 'Chloroplast'],
            'answer': 2
        },
        {
            'question': 'What is the hardest natural substance on Earth?',
            'options': ['Gold', 'Iron', 'Diamond', 'Platinum'],
            'answer': 2
        },
    ],
    'Geography': [
        {
            'question': 'What is the longest river in the world?',
            'options': ['Amazon', 'Nile', 'Yangtze', 'Mississippi'],
            'answer': 1
        },
        {
            'question': 'How many continents are there?',
            'options': ['5', '6', '7', '8'],
            'answer': 2
        },
        {
            'question': 'Which country has the most population?',
            'options': ['India', 'United States', 'China', 'Indonesia'],
            'answer': 2
        },
        {
            'question': 'What is the smallest country in the world?',
            'options': ['Monaco', 'Vatican City', 'San Marino', 'Liechtenstein'],
            'answer': 1
        },
        {
            'question': 'Mount Everest is located in which mountain range?',
            'options': ['Alps', 'Andes', 'Rockies', 'Himalayas'],
            'answer': 3
        },
    ],
    'Pop Culture': [
        {
            'question': 'Who is known as the "King of Pop"?',
            'options': ['Elvis Presley', 'Michael Jackson', 'Prince', 'David Bowie'],
            'answer': 1
        },
        {
            'question': 'Which movie won the first Academy Award for Best Picture?',
            'options': ['Wings', 'The Jazz Singer', 'Sunrise', 'Metropolis'],
            'answer': 0
        },
        {
            'question': 'How many Harry Potter books are there?',
            'options': ['5', '6', '7', '8'],
            'answer': 2
        },
        {
            'question': 'What year was the first iPhone released?',
            'options': ['2005', '2006', '2007', '2008'],
            'answer': 2
        },
        {
            'question': 'Which band wrote "Bohemian Rhapsody"?',
            'options': ['The Beatles', 'Led Zeppelin', 'Queen', 'Pink Floyd'],
            'answer': 2
        },
    ],
}


def play_quiz(category, questions):
    """Play a quiz with the given questions"""
    score = 0
    total = len(questions)
    
    # Shuffle questions
    quiz_questions = random.sample(questions, len(questions))
    
    print(f"\n{'='*50}")
    print(f"📚 {category} Quiz")
    print(f"{'='*50}")
    print(f"Answer {total} questions. Good luck!\n")
    time.sleep(1)
    
    for i, q in enumerate(quiz_questions, 1):
        print(f"\n{'─'*50}")
        print(f"Question {i}/{total}:")
        print(f"\n{q['question']}\n")
        
        for idx, option in enumerate(q['options']):
            print(f"  {idx + 1}. {option}")
        
        while True:
            try:
                answer = input("\nYour answer (1-4): ").strip()
                answer_idx = int(answer) - 1
                
                if 0 <= answer_idx < 4:
                    break
                else:
                    print("❌ Please enter a number between 1 and 4!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Check answer
        if answer_idx == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            correct_answer = q['options'][q['answer']]
            print(f"❌ Wrong! The correct answer was: {correct_answer}")
        
        time.sleep(1)
    
    # Display results
    print(f"\n{'='*50}")
    print("🎯 QUIZ COMPLETE!")
    print(f"{'='*50}")
    print(f"Your Score: {score}/{total}")
    
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Give feedback based on score
    if percentage == 100:
        print("\n🌟 Perfect score! You're a genius!")
    elif percentage >= 80:
        print("\n🎉 Excellent work! Great job!")
    elif percentage >= 60:
        print("\n👍 Good job! Not bad at all!")
    elif percentage >= 40:
        print("\n😊 Nice try! Keep learning!")
    else:
        print("\n📖 Keep studying! You'll do better next time!")
    
    print(f"{'='*50}")


def run():
    """Main function for mini quiz"""
    
    total_quizzes = 0
    total_score = 0
    total_questions = 0
    
    while True:
        print("\n" + "="*50)
        print("📝  MINI QUIZ GAME  📝")
        print("="*50)
        
        if total_quizzes > 0:
            avg_score = (total_score / total_questions * 100) if total_questions > 0 else 0
            print(f"\n📊 Overall Stats:")
            print(f"   Quizzes Taken: {total_quizzes}")
            print(f"   Total Questions: {total_questions}")
            print(f"   Correct Answers: {total_score}")
            print(f"   Average Score: {avg_score:.1f}%")
            print("─"*50)
        
        print("\nSelect a quiz category:")
        categories = list(QUIZ_DATA.keys())
        
        for i, category in enumerate(categories, 1):
            print(f"  {i}. {category} ({len(QUIZ_DATA[category])} questions)")
        
        print(f"  {len(categories) + 1}. Random Mix (all categories)")
        print(f"  0. Return to Main Menu")
        
        try:
            choice = input("\nYour choice: ").strip()
            
            if choice == "0":
                break
            
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(categories):
                category = categories[choice_num - 1]
                questions = QUIZ_DATA[category]
                
                # Ask how many questions
                print(f"\nHow many questions? (1-{len(questions)})")
                num_q = input("Enter number (or press Enter for all): ").strip()
                
                if num_q:
                    num_questions = int(num_q)
                    if 1 <= num_questions <= len(questions):
                        selected_questions = random.sample(questions, num_questions)
                    else:
                        print(f"❌ Invalid number! Using all {len(questions)} questions.")
                        selected_questions = questions
                else:
                    selected_questions = questions
                
                # Count correct answers before quiz
                pre_score = total_score
                pre_questions = total_questions
                
                play_quiz(category, selected_questions)
                
                # Update stats (for simplicity, we'll ask user)
                try:
                    user_score = int(input("\nEnter your score to save it: ").strip())
                    total_score += user_score
                    total_questions += len(selected_questions)
                    total_quizzes += 1
                except:
                    pass
                
                input("\nPress Enter to continue...")
            
            elif choice_num == len(categories) + 1:
                # Random mix
                all_questions = []
                for cat_questions in QUIZ_DATA.values():
                    all_questions.extend(cat_questions)
                
                print(f"\nHow many questions? (1-{len(all_questions)})")
                num_q = input("Enter number (default: 10): ").strip()
                
                if num_q:
                    num_questions = int(num_q)
                else:
                    num_questions = 10
                
                num_questions = min(num_questions, len(all_questions))
                selected_questions = random.sample(all_questions, num_questions)
                
                play_quiz("Random Mix", selected_questions)
                
                # Update stats
                try:
                    user_score = int(input("\nEnter your score to save it: ").strip())
                    total_score += user_score
                    total_questions += len(selected_questions)
                    total_quizzes += 1
                except:
                    pass
                
                input("\nPress Enter to continue...")
            
            else:
                print("❌ Invalid choice!")
                time.sleep(1)
        
        except ValueError:
            print("❌ Invalid input!")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nQuiz interrupted!")
            break


if __name__ == "__main__":
    run()