#!/usr/bin/env python3
"""
Weather Checker
Simple weather simulation and information tool
"""

import random
import time
from datetime import datetime


class WeatherChecker:
    def __init__(self):
        self.weather_conditions = [
            'Sunny', 'Partly Cloudy', 'Cloudy', 'Overcast',
            'Light Rain', 'Rain', 'Heavy Rain', 'Thunderstorm',
            'Light Snow', 'Snow', 'Blizzard', 'Foggy', 'Windy'
        ]
        
        self.temperature_ranges = {
            'Sunny': (20, 35),
            'Partly Cloudy': (15, 30),
            'Cloudy': (10, 25),
            'Overcast': (8, 20),
            'Light Rain': (10, 20),
            'Rain': (8, 18),
            'Heavy Rain': (5, 15),
            'Thunderstorm': (10, 20),
            'Light Snow': (-5, 5),
            'Snow': (-10, 2),
            'Blizzard': (-20, -5),
            'Foggy': (5, 15),
            'Windy': (10, 25)
        }
        
        self.weather_icons = {
            'Sunny': '☀️',
            'Partly Cloudy': '⛅',
            'Cloudy': '☁️',
            'Overcast': '☁️',
            'Light Rain': '🌦️',
            'Rain': '🌧️',
            'Heavy Rain': '⛈️',
            'Thunderstorm': '⚡',
            'Light Snow': '🌨️',
            'Snow': '❄️',
            'Blizzard': '🌨️',
            'Foggy': '🌫️',
            'Windy': '💨'
        }
        
        self.cities = [
            'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
            'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
            'London', 'Paris', 'Tokyo', 'Sydney', 'Toronto',
            'Berlin', 'Madrid', 'Rome', 'Amsterdam', 'Dubai'
        ]
    
    def generate_weather(self):
        """Generate random weather"""
        condition = random.choice(self.weather_conditions)
        temp_min, temp_max = self.temperature_ranges[condition]
        temperature = random.randint(temp_min, temp_max)
        humidity = random.randint(30, 95)
        wind_speed = random.randint(5, 50)
        
        return {
            'condition': condition,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'icon': self.weather_icons[condition]
        }
    
    def get_weather_advice(self, weather):
        """Get advice based on weather conditions"""
        condition = weather['condition']
        temp = weather['temperature']
        
        advice = []
        
        # Temperature advice
        if temp > 30:
            advice.append("🔥 It's very hot! Stay hydrated and avoid prolonged sun exposure.")
        elif temp > 25:
            advice.append("☀️ Warm weather. Light clothing recommended.")
        elif temp > 15:
            advice.append("👕 Mild weather. Comfortable temperature.")
        elif temp > 5:
            advice.append("🧥 Cool weather. Bring a jacket.")
        elif temp > -5:
            advice.append("🧊 Cold! Dress warmly.")
        else:
            advice.append("❄️ Extremely cold! Bundle up and limit outdoor time.")
        
        # Condition advice
        if 'Rain' in condition or condition == 'Thunderstorm':
            advice.append("☔ Don't forget your umbrella!")
        
        if condition == 'Thunderstorm':
            advice.append("⚡ Stay indoors if possible. Avoid open areas.")
        
        if 'Snow' in condition or condition == 'Blizzard':
            advice.append("❄️ Watch for icy roads. Drive carefully!")
        
        if condition == 'Blizzard':
            advice.append("🚨 Severe weather! Avoid travel if possible.")
        
        if weather['wind_speed'] > 40:
            advice.append("💨 Very windy! Secure loose objects.")
        
        if weather['humidity'] > 80:
            advice.append("💧 High humidity. It might feel muggy.")
        
        return advice
    
    def display_weather(self, city, weather):
        """Display weather information"""
        print("\n" + "="*50)
        print(f"{weather['icon']}  WEATHER FOR {city.upper()}")
        print("="*50)
        print(f"\nCondition:    {weather['condition']} {weather['icon']}")
        print(f"Temperature:  {weather['temperature']}°C ({self.celsius_to_fahrenheit(weather['temperature'])}°F)")
        print(f"Humidity:     {weather['humidity']}%")
        print(f"Wind Speed:   {weather['wind_speed']} km/h")
        print("\n" + "─"*50)
        print("💡 ADVICE:")
        
        advice = self.get_weather_advice(weather)
        for tip in advice:
            print(f"  • {tip}")
        
        print("="*50)
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        return int(celsius * 9/5 + 32)


def check_random_city():
    """Check weather for random city"""
    checker = WeatherChecker()
    city = random.choice(checker.cities)
    
    print(f"\n🌍 Checking weather for {city}...")
    time.sleep(1)
    
    weather = checker.generate_weather()
    checker.display_weather(city, weather)


def check_specific_city():
    """Check weather for specific city"""
    checker = WeatherChecker()
    
    print("\n🌍 CITY SELECTION")
    print("="*50)
    print("\nAvailable Cities:")
    
    for i, city in enumerate(checker.cities, 1):
        print(f"  {i:2}. {city}")
    
    try:
        choice = int(input(f"\nSelect city (1-{len(checker.cities)}): ").strip())
        
        if 1 <= choice <= len(checker.cities):
            city = checker.cities[choice - 1]
            
            print(f"\n🌍 Checking weather for {city}...")
            time.sleep(1)
            
            weather = checker.generate_weather()
            checker.display_weather(city, weather)
        else:
            print("❌ Invalid choice!")
    
    except ValueError:
        print("❌ Invalid input!")


def weekly_forecast():
    """Generate 7-day forecast"""
    checker = WeatherChecker()
    
    print("\n📅 SELECT CITY FOR FORECAST")
    print("="*50)
    
    city = random.choice(checker.cities[:10])
    print(f"\nGenerating 7-day forecast for {city}...")
    time.sleep(1)
    
    print("\n" + "="*50)
    print(f"📅 7-DAY FORECAST - {city.upper()}")
    print("="*50)
    
    from datetime import datetime, timedelta
    
    today = datetime.now()
    
    for i in range(7):
        date = today + timedelta(days=i)
        day_name = date.strftime("%A")
        date_str = date.strftime("%m/%d")
        
        weather = checker.generate_weather()
        
        temp_c = weather['temperature']
        temp_f = checker.celsius_to_fahrenheit(temp_c)
        
        print(f"\n{day_name}, {date_str}")
        print(f"  {weather['icon']} {weather['condition']}")
        print(f"  🌡️  {temp_c}°C / {temp_f}°F")
        print(f"  💧 Humidity: {weather['humidity']}%")
        
        time.sleep(0.3)
    
    print("\n" + "="*50)


def compare_cities():
    """Compare weather in multiple cities"""
    checker = WeatherChecker()
    
    print("\n🌎 COMPARE CITIES")
    print("="*50)
    
    num_cities = random.randint(3, 5)
    selected_cities = random.sample(checker.cities, num_cities)
    
    print(f"\nComparing weather in {num_cities} cities...\n")
    time.sleep(1)
    
    weather_data = []
    
    for city in selected_cities:
        weather = checker.generate_weather()
        weather_data.append({'city': city, 'weather': weather})
    
    print("="*50)
    print("🌡️  TEMPERATURE COMPARISON")
    print("="*50)
    
    for data in sorted(weather_data, key=lambda x: x['weather']['temperature'], reverse=True):
        city = data['city']
        weather = data['weather']
        temp_c = weather['temperature']
        temp_f = checker.celsius_to_fahrenheit(temp_c)
        
        print(f"{city:15} {weather['icon']} {temp_c:3}°C / {temp_f:3}°F  ({weather['condition']})")
    
    print("="*50)


def weather_quiz():
    """Weather knowledge quiz"""
    questions = [
        {
            'question': 'What does a barometer measure?',
            'options': ['Temperature', 'Humidity', 'Atmospheric Pressure', 'Wind Speed'],
            'answer': 2
        },
        {
            'question': 'What type of cloud produces thunderstorms?',
            'options': ['Cirrus', 'Stratus', 'Cumulonimbus', 'Cumulus'],
            'answer': 2
        },
        {
            'question': 'At what temperature does water freeze in Celsius?',
            'options': ['0°C', '-10°C', '32°C', '100°C'],
            'answer': 0
        },
        {
            'question': 'What is the name of a spinning column of air?',
            'options': ['Hurricane', 'Tornado', 'Cyclone', 'Typhoon'],
            'answer': 1
        },
        {
            'question': 'What causes wind?',
            'options': ['Temperature differences', 'Earth rotation', 'Ocean currents', 'Mountains'],
            'answer': 0
        },
    ]
    
    print("\n📚 WEATHER QUIZ")
    print("="*50)
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{len(questions)}:")
        print(q['question'])
        print()
        
        for j, option in enumerate(q['options'], 1):
            print(f"  {j}. {option}")
        
        try:
            answer = int(input("\nYour answer (1-4): ").strip()) - 1
            
            if answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The answer was: {q['options'][q['answer']]}")
        
        except ValueError:
            print("❌ Invalid input!")
        
        time.sleep(1)
    
    print("\n" + "="*50)
    print(f"🎯 FINAL SCORE: {score}/{len(questions)}")
    print("="*50)


def run():
    """Main function for weather checker"""
    
    while True:
        print("\n" + "="*50)
        print("🌤️   WEATHER CHECKER  🌤️")
        print("="*50)
        print("\nOptions:")
        print("  1. Check Random City")
        print("  2. Check Specific City")
        print("  3. 7-Day Forecast")
        print("  4. Compare Multiple Cities")
        print("  5. Weather Quiz")
        print("  6. Weather Guide")
        print("  0. Return to Main Menu")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            break
        
        elif choice == "1":
            check_random_city()
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            check_specific_city()
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            weekly_forecast()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            compare_cities()
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            weather_quiz()
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            print("\n" + "="*50)
            print("📖 WEATHER GUIDE")
            print("="*50)
            print("""
Weather Terms:
───────────────────────────────────────
☀️  Sunny - Clear skies, bright sun
⛅ Partly Cloudy - Mix of sun and clouds
☁️  Cloudy - Overcast, no direct sun
🌧️  Rain - Precipitation falling
⚡ Thunderstorm - Rain with lightning
❄️  Snow - Frozen precipitation
🌫️  Foggy - Reduced visibility
💨 Windy - Strong air movement

Temperature Scale:
───────────────────────────────────────
> 30°C (86°F)  - Very Hot
25-30°C (77-86°F) - Warm
15-25°C (59-77°F) - Mild
5-15°C (41-59°F)  - Cool
0-5°C (32-41°F)   - Cold
< 0°C (32°F)      - Freezing

Note: This is a simulation tool.
For real weather, check actual weather services!
            """)
            print("="*50)
            input("\nPress Enter to continue...")
        
        else:
            print("❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    run()