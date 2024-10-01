import random
import requests

# List of random cities
cities = ["New York", "Tokyo", "Paris", "Sydney", "Rio de Janeiro", "Cape Town", "Moscow", "Toronto", "Dubai", "Mumbai"]

# OpenWeatherMap API key (you need to sign up for free and get your own key)
API_KEY = "your_openweathermap_api_key"

# Function to get random city
def get_random_city():
    return random.choice(cities)

# Function to get weather for a city using OpenWeatherMap API
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"Weather in {city}: {weather_description}, Temperature: {temperature}°C"
    else:
        return "Sorry, couldn't fetch weather data."

# Function to get fun facts about the city (using Wikipedia)
def get_city_facts(city):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        extract = data.get("extract", "Sorry, no facts available.")
        return extract
    else:
        return "Sorry, no facts available."

# Main function to run the city explorer
def main():
    print("Welcome to the Random City Explorer!")
    
    while True:
        input("Press Enter to explore a random city, or type 'quit' to exit: ").strip().lower()
        
        # Get a random city
        city = get_random_city()
        
        # Get city facts
        print(f"\nExploring {city}...\n")
        facts = get_city_facts(city)
        print(f"City Facts:\n{facts}\n")
        
        # Get weather information
        weather = get_weather(city)
        print(f"{weather}\n")
        
        # Ask if the user wants to continue
        cont = input("Would you like to explore another city? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Thanks for exploring cities with us!")
            break

if __name__ == "__main__":
    main()

