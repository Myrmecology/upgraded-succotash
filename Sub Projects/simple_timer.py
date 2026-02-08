#!/usr/bin/env python3
"""
Simple Timer
Countdown timer and stopwatch with multiple features
"""

import time
import sys


def countdown_timer(seconds):
    """Countdown from specified seconds"""
    print(f"\n⏱️  Starting {seconds} second countdown...\n")
    
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            
            # Format time display
            if hours > 0:
                timeformat = f'{hours:02d}:{mins:02d}:{secs:02d}'
            else:
                timeformat = f'{mins:02d}:{secs:02d}'
            
            print(f'\r⏱️  {timeformat}', end='', flush=True)
            time.sleep(1)
            seconds -= 1
        
        print('\r⏱️  00:00    ')
        print('\n🔔 TIME\'S UP! 🔔\n')
        
        # Beep sound (text)
        for _ in range(3):
            print('🔔 BEEP!', end=' ', flush=True)
            time.sleep(0.5)
        print('\n')
        
    except KeyboardInterrupt:
        print('\n\n⏸️  Timer stopped!')


def stopwatch():
    """Simple stopwatch"""
    print("\n⏱️  Stopwatch Started!")
    print("Press Ctrl+C to stop\n")
    
    start_time = time.time()
    
    try:
        while True:
            elapsed = time.time() - start_time
            
            hours, remainder = divmod(int(elapsed), 3600)
            mins, secs = divmod(remainder, 60)
            
            # Include milliseconds
            millisecs = int((elapsed - int(elapsed)) * 100)
            
            timeformat = f'{hours:02d}:{mins:02d}:{secs:02d}.{millisecs:02d}'
            
            print(f'\r⏱️  {timeformat}', end='', flush=True)
            time.sleep(0.01)
    
    except KeyboardInterrupt:
        print('\n')
        final_time = time.time() - start_time
        hours, remainder = divmod(int(final_time), 3600)
        mins, secs = divmod(remainder, 60)
        millisecs = int((final_time - int(final_time)) * 100)
        
        print(f'⏹️  Final Time: {hours:02d}:{mins:02d}:{secs:02d}.{millisecs:02d}\n')


def pomodoro_timer():
    """Pomodoro technique timer (25 min work, 5 min break)"""
    print("\n🍅 POMODORO TIMER")
    print("="*50)
    print("Work: 25 minutes | Break: 5 minutes")
    print("="*50)
    
    session = 1
    
    try:
        while True:
            print(f"\n📚 Session {session} - WORK TIME (25 minutes)")
            countdown_timer(25 * 60)
            
            take_break = input("\nTake a 5-minute break? (y/n): ").strip().lower()
            if take_break != 'y':
                break
            
            print(f"\n☕ Session {session} - BREAK TIME (5 minutes)")
            countdown_timer(5 * 60)
            
            session += 1
            
            continue_pomodoro = input("\nStart next session? (y/n): ").strip().lower()
            if continue_pomodoro != 'y':
                break
        
        print(f"\n✅ Completed {session} Pomodoro session(s)!")
    
    except KeyboardInterrupt:
        print(f"\n\n⏸️  Pomodoro stopped after {session} session(s)!")


def interval_timer():
    """Create custom interval timer"""
    print("\n⏱️  INTERVAL TIMER")
    print("="*50)
    
    intervals = []
    
    print("\nCreate your intervals (type 'done' when finished):")
    
    while True:
        name = input(f"\nInterval #{len(intervals) + 1} name (or 'done'): ").strip()
        
        if name.lower() == 'done':
            break
        
        if not name:
            print("❌ Name cannot be empty!")
            continue
        
        try:
            duration = int(input(f"Duration in seconds for '{name}': ").strip())
            if duration <= 0:
                print("❌ Duration must be positive!")
                continue
            
            intervals.append((name, duration))
        except ValueError:
            print("❌ Invalid duration!")
    
    if not intervals:
        print("\n❌ No intervals created!")
        return
    
    # Show summary
    print("\n" + "="*50)
    print("📋 Interval Summary:")
    for i, (name, duration) in enumerate(intervals, 1):
        print(f"  {i}. {name}: {duration} seconds")
    
    total_time = sum(d for _, d in intervals)
    print(f"\nTotal Time: {total_time} seconds ({total_time // 60} min {total_time % 60} sec)")
    print("="*50)
    
    start = input("\nStart interval timer? (y/n): ").strip().lower()
    if start != 'y':
        return
    
    try:
        for i, (name, duration) in enumerate(intervals, 1):
            print(f"\n▶️  Interval {i}/{len(intervals)}: {name}")
            countdown_timer(duration)
            
            if i < len(intervals):
                input("Press Enter for next interval...")
        
        print("\n🎉 All intervals complete!")
    
    except KeyboardInterrupt:
        print("\n\n⏸️  Interval timer stopped!")


def quick_timer():
    """Quick preset timers"""
    presets = {
        '1': ('1 Minute', 60),
        '2': ('3 Minutes', 180),
        '3': ('5 Minutes', 300),
        '4': ('10 Minutes', 600),
        '5': ('15 Minutes', 900),
        '6': ('30 Minutes', 1800),
        '7': ('1 Hour', 3600),
    }
    
    print("\n⚡ QUICK TIMER PRESETS")
    print("="*50)
    
    for key, (name, _) in presets.items():
        print(f"  {key}. {name}")
    
    choice = input("\nSelect preset: ").strip()
    
    if choice in presets:
        name, duration = presets[choice]
        print(f"\n🎯 Starting {name} timer...")
        countdown_timer(duration)
    else:
        print("❌ Invalid choice!")


def run():
    """Main function for simple timer"""
    
    while True:
        print("\n" + "="*50)
        print("⏱️   SIMPLE TIMER  ⏱️")
        print("="*50)
        print("\nTimer Options:")
        print("  1. Countdown Timer")
        print("  2. Stopwatch")
        print("  3. Pomodoro Timer (25/5 min)")
        print("  4. Interval Timer")
        print("  5. Quick Timer Presets")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            try:
                duration = input("\nEnter countdown duration in seconds: ").strip()
                seconds = int(duration)
                
                if seconds <= 0:
                    print("❌ Duration must be positive!")
                    time.sleep(1)
                    continue
                
                countdown_timer(seconds)
                input("\nPress Enter to continue...")
            
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
                time.sleep(1)
        
        elif choice == "2":
            stopwatch()
            input("Press Enter to continue...")
        
        elif choice == "3":
            pomodoro_timer()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            interval_timer()
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            quick_timer()
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()