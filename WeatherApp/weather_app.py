import requests
import json

# Replace with your actual API key
API_KEY = "9e340b46784d86bae16c3b0f6c26f171"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        # Make the API request
        response = requests.get(
            base_url,
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"  # For Celsius (use "imperial" for Fahrenheit)
            }
        )
        
        # Check if request was successful
        if response.status_code == 200:
            weather_data = response.json()
            
            # Extract important information
            temp = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            description = weather_data["weather"][0]["description"]
            
            # Print the weather information
            print(f"\n🌦️ Weather in {city}:")
            print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌬️ Wind: {wind_speed} m/s")
            print(f"☁️ Conditions: {description.capitalize()}")
            
            # Save to file
            with open(f"{city}_weather.txt", "w") as file:
                file.write(f"Weather in {city}:\n")
                file.write(f"Temperature: {temp}°C (Feels like {feels_like}°C)\n")
                file.write(f"Humidity: {humidity}%\n")
                file.write(f"Wind: {wind_speed} m/s\n")
                file.write(f"Conditions: {description.capitalize()}\n")
            
            print(f"\n✅ Weather data saved to '{city}_weather.txt'")
            
        else:
            print(f"Error: {response.status_code} - Could not fetch weather data")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main program
if __name__ == "__main__":
    print("🌤️ Simple Weather App 🌤️")
    city = input("Enter city name: ")
    get_weather(city)