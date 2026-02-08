#!/usr/bin/env python3
"""
Unit Converter
Convert between various units of measurement
"""

import time


class UnitConverter:
    def __init__(self):
        # Length conversions (to meters)
        self.length_units = {
            'meters': 1,
            'kilometers': 1000,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'miles': 1609.34,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254,
        }
        
        # Weight conversions (to kilograms)
        self.weight_units = {
            'kilograms': 1,
            'grams': 0.001,
            'milligrams': 0.000001,
            'pounds': 0.453592,
            'ounces': 0.0283495,
            'tons': 1000,
        }
        
        # Temperature (special handling)
        self.temp_units = ['celsius', 'fahrenheit', 'kelvin']
        
        # Volume conversions (to liters)
        self.volume_units = {
            'liters': 1,
            'milliliters': 0.001,
            'gallons': 3.78541,
            'quarts': 0.946353,
            'pints': 0.473176,
            'cups': 0.236588,
            'fluid_ounces': 0.0295735,
            'tablespoons': 0.0147868,
            'teaspoons': 0.00492892,
        }
        
        # Time conversions (to seconds)
        self.time_units = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800,
            'years': 31536000,
        }
        
        # Speed conversions (to m/s)
        self.speed_units = {
            'meters_per_second': 1,
            'kilometers_per_hour': 0.277778,
            'miles_per_hour': 0.44704,
            'feet_per_second': 0.3048,
            'knots': 0.514444,
        }
    
    def convert_length(self, value, from_unit, to_unit):
        """Convert length units"""
        meters = value * self.length_units[from_unit]
        result = meters / self.length_units[to_unit]
        return result
    
    def convert_weight(self, value, from_unit, to_unit):
        """Convert weight units"""
        kilograms = value * self.weight_units[from_unit]
        result = kilograms / self.weight_units[to_unit]
        return result
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature units"""
        if from_unit == to_unit:
            return value
        
        # Convert to Celsius first
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        
        # Convert from Celsius to target
        if to_unit == 'fahrenheit':
            return celsius * 9/5 + 32
        elif to_unit == 'kelvin':
            return celsius + 273.15
        else:
            return celsius
    
    def convert_volume(self, value, from_unit, to_unit):
        """Convert volume units"""
        liters = value * self.volume_units[from_unit]
        result = liters / self.volume_units[to_unit]
        return result
    
    def convert_time(self, value, from_unit, to_unit):
        """Convert time units"""
        seconds = value * self.time_units[from_unit]
        result = seconds / self.time_units[to_unit]
        return result
    
    def convert_speed(self, value, from_unit, to_unit):
        """Convert speed units"""
        mps = value * self.speed_units[from_unit]
        result = mps / self.speed_units[to_unit]
        return result


def display_units(unit_dict, title):
    """Display available units"""
    print(f"\n{title}:")
    for i, unit in enumerate(unit_dict, 1):
        print(f"  {i}. {unit.replace('_', ' ').title()}")


def get_unit_choice(unit_dict, prompt):
    """Get unit selection from user"""
    units = list(unit_dict)
    
    while True:
        try:
            choice = int(input(prompt).strip())
            if 1 <= choice <= len(units):
                return units[choice - 1]
            else:
                print(f"❌ Please enter a number between 1 and {len(units)}")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def length_converter(converter):
    """Convert length units"""
    print("\n📏 LENGTH CONVERTER")
    print("="*50)
    
    display_units(converter.length_units, "Available Units")
    
    try:
        from_unit = get_unit_choice(converter.length_units, "\nConvert FROM (1-8): ")
        to_unit = get_unit_choice(converter.length_units, "Convert TO (1-8): ")
        
        value = float(input(f"\nEnter value in {from_unit}: ").strip())
        
        result = converter.convert_length(value, from_unit, to_unit)
        
        print("\n" + "="*50)
        print("✅ CONVERSION RESULT")
        print("="*50)
        print(f"{value} {from_unit} = {result:.4f} {to_unit}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input!")


def weight_converter(converter):
    """Convert weight units"""
    print("\n⚖️  WEIGHT CONVERTER")
    print("="*50)
    
    display_units(converter.weight_units, "Available Units")
    
    try:
        from_unit = get_unit_choice(converter.weight_units, "\nConvert FROM (1-6): ")
        to_unit = get_unit_choice(converter.weight_units, "Convert TO (1-6): ")
        
        value = float(input(f"\nEnter value in {from_unit}: ").strip())
        
        result = converter.convert_weight(value, from_unit, to_unit)
        
        print("\n" + "="*50)
        print("✅ CONVERSION RESULT")
        print("="*50)
        print(f"{value} {from_unit} = {result:.4f} {to_unit}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input!")


def temperature_converter(converter):
    """Convert temperature units"""
    print("\n🌡️  TEMPERATURE CONVERTER")
    print("="*50)
    
    print("\nAvailable Units:")
    for i, unit in enumerate(converter.temp_units, 1):
        print(f"  {i}. {unit.title()}")
    
    try:
        from_unit = get_unit_choice(converter.temp_units, "\nConvert FROM (1-3): ")
        to_unit = get_unit_choice(converter.temp_units, "Convert TO (1-3): ")
        
        value = float(input(f"\nEnter temperature in {from_unit}: ").strip())
        
        result = converter.convert_temperature(value, from_unit, to_unit)
        
        print("\n" + "="*50)
        print("✅ CONVERSION RESULT")
        print("="*50)
        print(f"{value}° {from_unit.title()} = {result:.2f}° {to_unit.title()}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input!")


def volume_converter(converter):
    """Convert volume units"""
    print("\n🥤 VOLUME CONVERTER")
    print("="*50)
    
    display_units(converter.volume_units, "Available Units")
    
    try:
        from_unit = get_unit_choice(converter.volume_units, "\nConvert FROM (1-9): ")
        to_unit = get_unit_choice(converter.volume_units, "Convert TO (1-9): ")
        
        value = float(input(f"\nEnter value in {from_unit.replace('_', ' ')}: ").strip())
        
        result = converter.convert_volume(value, from_unit, to_unit)
        
        print("\n" + "="*50)
        print("✅ CONVERSION RESULT")
        print("="*50)
        print(f"{value} {from_unit.replace('_', ' ')} = {result:.4f} {to_unit.replace('_', ' ')}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input!")


def time_converter(converter):
    """Convert time units"""
    print("\n⏰ TIME CONVERTER")
    print("="*50)
    
    display_units(converter.time_units, "Available Units")
    
    try:
        from_unit = get_unit_choice(converter.time_units, "\nConvert FROM (1-6): ")
        to_unit = get_unit_choice(converter.time_units, "Convert TO (1-6): ")
        
        value = float(input(f"\nEnter value in {from_unit}: ").strip())
        
        result = converter.convert_time(value, from_unit, to_unit)
        
        print("\n" + "="*50)
        print("✅ CONVERSION RESULT")
        print("="*50)
        print(f"{value} {from_unit} = {result:.4f} {to_unit}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input!")


def speed_converter(converter):
    """Convert speed units"""
    print("\n🏃 SPEED CONVERTER")
    print("="*50)
    
    display_units(converter.speed_units, "Available Units")
    
    try:
        from_unit = get_unit_choice(converter.speed_units, "\nConvert FROM (1-5): ")
        to_unit = get_unit_choice(converter.speed_units, "Convert TO (1-5): ")
        
        value = float(input(f"\nEnter value in {from_unit.replace('_', ' ')}: ").strip())
        
        result = converter.convert_speed(value, from_unit, to_unit)
        
        print("\n" + "="*50)
        print("✅ CONVERSION RESULT")
        print("="*50)
        print(f"{value} {from_unit.replace('_', ' ')} = {result:.4f} {to_unit.replace('_', ' ')}")
        print("="*50)
        
    except ValueError:
        print("❌ Invalid input!")


def quick_conversions():
    """Quick common conversions"""
    print("\n⚡ QUICK CONVERSIONS")
    print("="*50)
    print("""
Common Conversions:
───────────────────────────────────────
Length:
  1 inch = 2.54 cm
  1 foot = 30.48 cm
  1 yard = 0.9144 meters
  1 mile = 1.609 km

Weight:
  1 pound = 0.454 kg
  1 ounce = 28.35 grams
  1 kg = 2.205 pounds

Temperature:
  0°C = 32°F = 273.15K
  100°C = 212°F = 373.15K
  -40°C = -40°F

Volume:
  1 gallon = 3.785 liters
  1 cup = 236.6 ml
  1 tablespoon = 14.79 ml
  1 teaspoon = 4.93 ml

Speed:
  1 mph = 1.609 km/h
  1 knot = 1.852 km/h
    """)
    print("="*50)


def run():
    """Main function for unit converter"""
    
    converter = UnitConverter()
    
    while True:
        print("\n" + "="*50)
        print("🔄  UNIT CONVERTER  🔄")
        print("="*50)
        print("\nConversion Categories:")
        print("  1. Length (meters, feet, inches, etc.)")
        print("  2. Weight (kg, pounds, ounces, etc.)")
        print("  3. Temperature (Celsius, Fahrenheit, Kelvin)")
        print("  4. Volume (liters, gallons, cups, etc.)")
        print("  5. Time (seconds, minutes, hours, etc.)")
        print("  6. Speed (mph, km/h, m/s, etc.)")
        print("  7. Quick Reference Guide")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            length_converter(converter)
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            weight_converter(converter)
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            temperature_converter(converter)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            volume_converter(converter)
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            time_converter(converter)
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            speed_converter(converter)
            input("\nPress Enter to continue...")
        
        elif choice == "7":
            quick_conversions()
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()