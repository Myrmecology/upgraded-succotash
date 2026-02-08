#!/usr/bin/env python3
"""
Simple Graph Plotter
Create and display simple graphs and charts
"""

import time


def plot_bar_chart(data, title="Bar Chart"):
    """Create a simple ASCII bar chart"""
    if not data:
        print("❌ No data to plot!")
        return
    
    max_value = max(data.values())
    scale = 50 / max_value if max_value > 0 else 1
    
    print("\n" + "="*60)
    print(f"📊 {title}")
    print("="*60)
    
    for label, value in data.items():
        bar_length = int(value * scale)
        bar = "█" * bar_length
        print(f"{label:15} | {bar} {value}")
    
    print("="*60)


def plot_line_graph(data, title="Line Graph"):
    """Create a simple ASCII line graph"""
    if not data:
        print("❌ No data to plot!")
        return
    
    values = list(data.values())
    labels = list(data.keys())
    
    max_value = max(values)
    min_value = min(values)
    
    height = 15
    width = len(values)
    
    # Normalize values to fit in height
    if max_value == min_value:
        normalized = [height // 2] * len(values)
    else:
        normalized = [int((v - min_value) / (max_value - min_value) * (height - 1)) for v in values]
    
    print("\n" + "="*60)
    print(f"📈 {title}")
    print("="*60)
    print(f"Max: {max_value}")
    
    # Draw graph from top to bottom
    for row in range(height - 1, -1, -1):
        line = ""
        for col in range(width):
            if normalized[col] == row:
                line += " ●"
            elif normalized[col] > row:
                line += " │"
            else:
                line += "  "
        print(f"{line}")
    
    # Draw x-axis
    print("─" * (width * 2 + 1))
    
    # Draw labels
    label_line = ""
    for label in labels:
        label_line += f" {str(label)[:1]}"
    print(label_line)
    
    print(f"Min: {min_value}")
    print("="*60)


def plot_pie_chart(data, title="Pie Chart"):
    """Create a simple ASCII pie chart"""
    if not data:
        print("❌ No data to plot!")
        return
    
    total = sum(data.values())
    
    print("\n" + "="*60)
    print(f"🥧 {title}")
    print("="*60)
    print(f"Total: {total}\n")
    
    symbols = ['█', '▓', '▒', '░', '▪', '▫', '●', '○']
    
    for i, (label, value) in enumerate(data.items()):
        percentage = (value / total * 100) if total > 0 else 0
        bar_length = int(percentage / 2)
        symbol = symbols[i % len(symbols)]
        bar = symbol * bar_length
        
        print(f"{label:15} {symbol} {bar} {percentage:.1f}% ({value})")
    
    print("="*60)


def plot_histogram(values, bins=10, title="Histogram"):
    """Create a simple ASCII histogram"""
    if not values:
        print("❌ No data to plot!")
        return
    
    min_val = min(values)
    max_val = max(values)
    
    bin_width = (max_val - min_val) / bins
    
    # Create bins
    bin_counts = [0] * bins
    
    for value in values:
        if value == max_val:
            bin_index = bins - 1
        else:
            bin_index = int((value - min_val) / bin_width)
        
        if 0 <= bin_index < bins:
            bin_counts[bin_index] += 1
    
    print("\n" + "="*60)
    print(f"📊 {title}")
    print("="*60)
    print(f"Range: {min_val:.2f} to {max_val:.2f}")
    print(f"Total values: {len(values)}\n")
    
    max_count = max(bin_counts) if bin_counts else 1
    scale = 40 / max_count if max_count > 0 else 1
    
    for i, count in enumerate(bin_counts):
        bin_start = min_val + (i * bin_width)
        bin_end = bin_start + bin_width
        bar_length = int(count * scale)
        bar = "█" * bar_length
        
        print(f"{bin_start:6.1f}-{bin_end:6.1f} | {bar} {count}")
    
    print("="*60)


def create_custom_chart():
    """Allow user to create a custom chart"""
    print("\n📊 Create Custom Chart")
    print("─"*50)
    
    data = {}
    
    print("\nEnter data points (type 'done' when finished):")
    
    while True:
        label = input(f"\nLabel #{len(data) + 1} (or 'done'): ").strip()
        
        if label.lower() == 'done':
            break
        
        if not label:
            print("❌ Label cannot be empty!")
            continue
        
        try:
            value = float(input(f"Value for '{label}': ").strip())
            data[label] = value
        except ValueError:
            print("❌ Invalid value! Please enter a number.")
    
    if not data:
        print("\n❌ No data entered!")
        return
    
    print("\nSelect chart type:")
    print("  1. Bar Chart")
    print("  2. Line Graph")
    print("  3. Pie Chart")
    
    choice = input("\nYour choice (1-3): ").strip()
    
    if choice == "1":
        plot_bar_chart(data, "Custom Bar Chart")
    elif choice == "2":
        plot_line_graph(data, "Custom Line Graph")
    elif choice == "3":
        plot_pie_chart(data, "Custom Pie Chart")
    else:
        print("❌ Invalid choice!")


def run():
    """Main function for simple graph plotter"""
    
    while True:
        print("\n" + "="*50)
        print("📊  SIMPLE GRAPH PLOTTER  📊")
        print("="*50)
        print("\nOptions:")
        print("  1. Sample Bar Chart")
        print("  2. Sample Line Graph")
        print("  3. Sample Pie Chart")
        print("  4. Sample Histogram")
        print("  5. Create Custom Chart")
        print("  6. Random Data Visualization")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            # Sample bar chart
            data = {
                'Python': 85,
                'JavaScript': 72,
                'Java': 68,
                'C++': 55,
                'Ruby': 45,
            }
            plot_bar_chart(data, "Programming Language Popularity")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            # Sample line graph
            data = {
                'Jan': 45,
                'Feb': 52,
                'Mar': 48,
                'Apr': 65,
                'May': 70,
                'Jun': 85,
                'Jul': 90,
                'Aug': 88,
            }
            plot_line_graph(data, "Monthly Sales")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            # Sample pie chart
            data = {
                'Work': 8,
                'Sleep': 7,
                'Exercise': 2,
                'Leisure': 4,
                'Meals': 2,
                'Commute': 1,
            }
            plot_pie_chart(data, "Daily Time Allocation (hours)")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            # Sample histogram
            import random
            values = [random.gauss(50, 15) for _ in range(100)]
            plot_histogram(values, bins=10, title="Random Normal Distribution")
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            create_custom_chart()
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            import random
            
            print("\n🎲 Random Data Visualization")
            print("─"*50)
            
            # Generate random data
            num_points = random.randint(5, 10)
            data = {}
            
            for i in range(num_points):
                label = f"Item {chr(65 + i)}"
                value = random.randint(10, 100)
                data[label] = value
            
            # Random chart type
            chart_type = random.choice(['bar', 'line', 'pie'])
            
            if chart_type == 'bar':
                plot_bar_chart(data, "Random Bar Chart")
            elif chart_type == 'line':
                plot_line_graph(data, "Random Line Graph")
            else:
                plot_pie_chart(data, "Random Pie Chart")
            
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()