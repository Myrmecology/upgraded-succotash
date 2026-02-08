#!/usr/bin/env python3
"""
Password Strength Tester
Test the strength of your passwords and get security tips
"""

import re
import time


def check_password_strength(password):
    """Analyze password strength and return detailed results"""
    score = 0
    feedback = []
    strength = ""
    
    length = len(password)
    
    # Check length
    if length < 6:
        feedback.append("❌ Password is too short (minimum 6 characters)")
    elif length < 8:
        feedback.append("⚠️  Password should be at least 8 characters")
        score += 1
    elif length < 12:
        feedback.append("✅ Good length (8+ characters)")
        score += 2
    else:
        feedback.append("✅ Excellent length (12+ characters)")
        score += 3
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        feedback.append("✅ Contains lowercase letters")
        score += 1
    else:
        feedback.append("❌ Missing lowercase letters")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        feedback.append("✅ Contains uppercase letters")
        score += 1
    else:
        feedback.append("❌ Missing uppercase letters")
    
    # Check for numbers
    if re.search(r'\d', password):
        feedback.append("✅ Contains numbers")
        score += 1
    else:
        feedback.append("❌ Missing numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\\/~`;]', password):
        feedback.append("✅ Contains special characters")
        score += 2
    else:
        feedback.append("❌ Missing special characters (!@#$%^&*)")
    
    # Check for common patterns
    common_patterns = [
        (r'123', "⚠️  Contains sequential numbers (123)"),
        (r'abc', "⚠️  Contains sequential letters (abc)"),
        (r'password', "⚠️  Contains the word 'password'"),
        (r'qwerty', "⚠️  Contains keyboard pattern (qwerty)"),
        (r'(.)\1{2,}', "⚠️  Contains repeated characters"),
    ]
    
    for pattern, message in common_patterns:
        if re.search(pattern, password.lower()):
            feedback.append(message)
            score -= 1
    
    # Determine strength level
    if score <= 2:
        strength = "Very Weak"
        color = "🔴"
    elif score <= 4:
        strength = "Weak"
        color = "🟠"
    elif score <= 6:
        strength = "Moderate"
        color = "🟡"
    elif score <= 8:
        strength = "Strong"
        color = "🟢"
    else:
        strength = "Very Strong"
        color = "🟢"
    
    return {
        'score': max(0, score),
        'max_score': 10,
        'strength': strength,
        'color': color,
        'feedback': feedback,
        'length': length
    }


def generate_password(length=12, include_upper=True, include_numbers=True, include_special=True):
    """Generate a random secure password"""
    import random
    import string
    
    chars = string.ascii_lowercase
    
    if include_upper:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one of each type
    password = []
    
    password.append(random.choice(string.ascii_lowercase))
    
    if include_upper:
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Fill the rest randomly
    for _ in range(length - len(password)):
        password.append(random.choice(chars))
    
    # Shuffle the password
    random.shuffle(password)
    
    return ''.join(password)


def display_tips():
    """Display password security tips"""
    print("\n" + "="*50)
    print("🔐 PASSWORD SECURITY TIPS")
    print("="*50)
    print("""
1. ✅ Use at least 12 characters
2. ✅ Mix uppercase and lowercase letters
3. ✅ Include numbers and special characters
4. ✅ Avoid common words and patterns
5. ✅ Don't reuse passwords across sites
6. ✅ Use a password manager
7. ✅ Enable two-factor authentication
8. ❌ Never share your passwords
9. ❌ Don't use personal information
10. ❌ Avoid sequential characters (123, abc)
    """)
    print("="*50)


def run():
    """Main function for password tester"""
    
    passwords_tested = 0
    
    while True:
        print("\n" + "="*50)
        print("🔐  PASSWORD STRENGTH TESTER  🔐")
        print("="*50)
        
        if passwords_tested > 0:
            print(f"\n📊 Passwords tested this session: {passwords_tested}")
            print("─"*50)
        
        print("\nOptions:")
        print("  1. Test a password")
        print("  2. Generate secure password")
        print("  3. View security tips")
        print("  4. Batch test passwords")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            print("\n" + "─"*50)
            password = input("Enter password to test (won't be stored): ").strip()
            
            if not password:
                print("❌ No password entered!")
                time.sleep(1)
                continue
            
            print("\n🔍 Analyzing password...\n")
            time.sleep(0.5)
            
            result = check_password_strength(password)
            
            print("="*50)
            print(f"{result['color']} Password Strength: {result['strength']}")
            print(f"Score: {result['score']}/{result['max_score']}")
            print(f"Length: {result['length']} characters")
            print("="*50)
            print("\n📋 Feedback:")
            
            for item in result['feedback']:
                print(f"  {item}")
            
            print("\n" + "="*50)
            
            passwords_tested += 1
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            print("\n🔑 Password Generator")
            print("─"*50)
            
            try:
                length = input("Password length (default 12): ").strip()
                length = int(length) if length else 12
                
                if length < 6:
                    print("⚠️  Minimum length is 6. Using 12.")
                    length = 12
                elif length > 50:
                    print("⚠️  Maximum length is 50. Using 50.")
                    length = 50
                
                use_upper = input("Include uppercase? (y/n, default y): ").strip().lower() != 'n'
                use_numbers = input("Include numbers? (y/n, default y): ").strip().lower() != 'n'
                use_special = input("Include special characters? (y/n, default y): ").strip().lower() != 'n'
                
                print("\n⚙️  Generating password...\n")
                time.sleep(0.5)
                
                generated = generate_password(length, use_upper, use_numbers, use_special)
                
                print("="*50)
                print(f"🔑 Generated Password: {generated}")
                print("="*50)
                
                # Test the generated password
                result = check_password_strength(generated)
                print(f"\n{result['color']} Strength: {result['strength']}")
                print(f"Score: {result['score']}/{result['max_score']}")
                
            except ValueError:
                print("❌ Invalid input!")
            
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            display_tips()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print("\n📝 Batch Password Testing")
            print("─"*50)
            print("Enter passwords one by one. Type 'done' when finished.\n")
            
            batch_results = []
            
            while True:
                password = input(f"Password #{len(batch_results) + 1} (or 'done'): ").strip()
                
                if password.lower() == 'done':
                    break
                
                if password:
                    result = check_password_strength(password)
                    batch_results.append({
                        'password': '*' * len(password),  # Hide actual password
                        'strength': result['strength'],
                        'score': result['score']
                    })
                    print(f"  → {result['color']} {result['strength']}")
            
            if batch_results:
                print("\n" + "="*50)
                print("📊 BATCH RESULTS")
                print("="*50)
                
                for i, res in enumerate(batch_results, 1):
                    print(f"{i}. {res['password']} - {res['strength']} ({res['score']}/10)")
                
                avg_score = sum(r['score'] for r in batch_results) / len(batch_results)
                print(f"\nAverage Score: {avg_score:.1f}/10")
                print("="*50)
                
                passwords_tested += len(batch_results)
            else:
                print("\n❌ No passwords tested.")
            
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()