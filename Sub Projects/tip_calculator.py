#!/usr/bin/env python3
"""
Tip Calculator
Calculate tips and split bills easily
"""

import time


def calculate_tip(bill_amount, tip_percentage):
    """Calculate tip amount and total"""
    tip_amount = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip_amount
    return tip_amount, total


def split_bill(total, num_people):
    """Split bill among people"""
    per_person = total / num_people
    return per_person


def format_currency(amount):
    """Format amount as currency"""
    return f"${amount:.2f}"


def simple_tip_calculator():
    """Simple tip calculation"""
    print("\n💵 SIMPLE TIP CALCULATOR")
    print("="*50)
    
    try:
        bill = float(input("\nEnter bill amount: $").strip())
        
        if bill <= 0:
            print("❌ Bill amount must be positive!")
            return
        
        print("\nSelect tip percentage:")
        print("  1. 15%")
        print("  2. 18%")
        print("  3. 20%")
        print("  4. 25%")
        print("  5. Custom")
        
        choice = input("\nYour choice: ").strip()
        
        tip_percentages = {'1': 15, '2': 18, '3': 20, '4': 25}
        
        if choice in tip_percentages:
            tip_percent = tip_percentages[choice]
        elif choice == '5':
            tip_percent = float(input("Enter tip percentage: ").strip())
            if tip_percent < 0:
                print("❌ Tip percentage cannot be negative!")
                return
        else:
            print("❌ Invalid choice!")
            return
        
        tip_amount, total = calculate_tip(bill, tip_percent)
        
        print("\n" + "="*50)
        print("📊 CALCULATION RESULTS")
        print("="*50)
        print(f"Bill Amount:    {format_currency(bill)}")
        print(f"Tip ({tip_percent}%):      {format_currency(tip_amount)}")
        print("─"*50)
        print(f"Total:          {format_currency(total)}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")


def split_bill_calculator():
    """Calculate and split bill"""
    print("\n👥 SPLIT BILL CALCULATOR")
    print("="*50)
    
    try:
        bill = float(input("\nEnter total bill amount: $").strip())
        
        if bill <= 0:
            print("❌ Bill amount must be positive!")
            return
        
        num_people = int(input("Number of people: ").strip())
        
        if num_people <= 0:
            print("❌ Number of people must be positive!")
            return
        
        print("\nInclude tip?")
        print("  1. Yes")
        print("  2. No")
        
        include_tip = input("Your choice: ").strip()
        
        if include_tip == '1':
            print("\nSelect tip percentage:")
            print("  1. 15%")
            print("  2. 18%")
            print("  3. 20%")
            print("  4. 25%")
            print("  5. Custom")
            
            choice = input("\nYour choice: ").strip()
            
            tip_percentages = {'1': 15, '2': 18, '3': 20, '4': 25}
            
            if choice in tip_percentages:
                tip_percent = tip_percentages[choice]
            elif choice == '5':
                tip_percent = float(input("Enter tip percentage: ").strip())
            else:
                print("❌ Invalid choice!")
                return
            
            tip_amount, total = calculate_tip(bill, tip_percent)
        else:
            tip_percent = 0
            tip_amount = 0
            total = bill
        
        per_person = split_bill(total, num_people)
        tip_per_person = tip_amount / num_people if tip_amount > 0 else 0
        
        print("\n" + "="*50)
        print("📊 SPLIT BILL RESULTS")
        print("="*50)
        print(f"Original Bill:  {format_currency(bill)}")
        if tip_amount > 0:
            print(f"Tip ({tip_percent}%):      {format_currency(tip_amount)}")
        print(f"Total:          {format_currency(total)}")
        print("─"*50)
        print(f"Number of People: {num_people}")
        print(f"Per Person:     {format_currency(per_person)}")
        if tip_per_person > 0:
            print(f"  (Bill: {format_currency(per_person - tip_per_person)} + Tip: {format_currency(tip_per_person)})")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")


def custom_split_calculator():
    """Split bill with custom amounts per person"""
    print("\n🎯 CUSTOM SPLIT CALCULATOR")
    print("="*50)
    print("Perfect for when people ordered different amounts!\n")
    
    try:
        total_bill = float(input("Enter total bill amount: $").strip())
        
        if total_bill <= 0:
            print("❌ Bill amount must be positive!")
            return
        
        tip_percent = float(input("Tip percentage: ").strip())
        
        if tip_percent < 0:
            print("❌ Tip percentage cannot be negative!")
            return
        
        num_people = int(input("Number of people: ").strip())
        
        if num_people <= 0:
            print("❌ Number of people must be positive!")
            return
        
        print("\nEnter each person's bill amount (before tip):")
        
        people_amounts = []
        for i in range(num_people):
            amount = float(input(f"Person {i+1}: $").strip())
            people_amounts.append(amount)
        
        subtotal = sum(people_amounts)
        
        # Check if amounts match the bill
        if abs(subtotal - total_bill) > 0.01:
            print(f"\n⚠️  Warning: Individual amounts (${subtotal:.2f}) don't match total bill (${total_bill:.2f})")
            print("Using individual amounts...")
            total_bill = subtotal
        
        tip_amount, total_with_tip = calculate_tip(total_bill, tip_percent)
        
        print("\n" + "="*50)
        print("📊 CUSTOM SPLIT RESULTS")
        print("="*50)
        print(f"Subtotal:       {format_currency(total_bill)}")
        print(f"Tip ({tip_percent}%):      {format_currency(tip_amount)}")
        print(f"Total:          {format_currency(total_with_tip)}")
        print("─"*50)
        print("Per Person Breakdown:")
        
        for i, amount in enumerate(people_amounts):
            person_tip = (amount / total_bill) * tip_amount
            person_total = amount + person_tip
            print(f"\nPerson {i+1}:")
            print(f"  Bill:  {format_currency(amount)}")
            print(f"  Tip:   {format_currency(person_tip)}")
            print(f"  Total: {format_currency(person_total)}")
        
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")


def tip_percentage_guide():
    """Display tip percentage guide"""
    print("\n" + "="*50)
    print("💡 TIP PERCENTAGE GUIDE")
    print("="*50)
    print("""
Service Quality          Tip Percentage
───────────────────────────────────────
Poor Service             10-12%
Adequate Service         15%
Good Service             18-20%
Excellent Service        20-25%
Outstanding Service      25%+

Special Situations:
- Takeout/Pickup         0-10%
- Buffet                 10%
- Delivery               15-20%
- Bartender              $1-2 per drink or 15-20%
- Valet                  $2-5
- Hotel Housekeeping     $2-5 per night
- Hair Salon             15-20%
- Taxi/Uber              15-20%
    """)
    print("="*50)


def quick_tip_reference():
    """Quick tip reference table"""
    print("\n💵 QUICK TIP REFERENCE")
    print("="*50)
    
    try:
        bill = float(input("\nEnter bill amount: $").strip())
        
        if bill <= 0:
            print("❌ Bill amount must be positive!")
            return
        
        print("\n" + "="*50)
        print(f"Quick Tip Calculator for {format_currency(bill)}")
        print("="*50)
        print(f"{'Tip %':<10} {'Tip Amount':<15} {'Total':<15}")
        print("─"*50)
        
        percentages = [10, 15, 18, 20, 25, 30]
        
        for percent in percentages:
            tip, total = calculate_tip(bill, percent)
            print(f"{percent}%{'':<7} {format_currency(tip):<15} {format_currency(total):<15}")
        
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")


def run():
    """Main function for tip calculator"""
    
    while True:
        print("\n" + "="*50)
        print("💵  TIP CALCULATOR  💵")
        print("="*50)
        print("\nOptions:")
        print("  1. Simple Tip Calculator")
        print("  2. Split Bill Evenly")
        print("  3. Custom Split (Different Amounts)")
        print("  4. Quick Tip Reference")
        print("  5. Tip Percentage Guide")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            simple_tip_calculator()
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            split_bill_calculator()
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            custom_split_calculator()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            quick_tip_reference()
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            tip_percentage_guide()
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()