import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api_key = "a4779959b9e5d2d0b985138f2bdc41b4"  # Replace with your actual API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def fetch_weather_data(city):
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

cities = ["London", "New York", "Tokyo", "Sydney", "Mumbai"]
weather_data = []

for city in cities:
    data = fetch_weather_data(city)

    # Check if the response contains the expected data
    if data.get("cod") != "404":
        try:
            weather_data.append({
                "cities": city,
                "Temperature": data["main"]["temp"],
                "Humidity": data["main"]["humidity"],
                "Cloudiness": data["clouds"]["all"],
                "Wind Speed": data["wind"]["speed"]
            })
        except KeyError as e:
            print(f"KeyError: {e} for city: {city}. Response: {data}")
    else:
        print(f"City {city} not found. Response: {data}")

# Convert the collected data into a Pandas DataFrame
df = pd.DataFrame(weather_data)

# Check if DataFrame is empty
if df.empty:
    print("No valid weather data was collected.")
else:
    # Create visualizations
    plt.figure(figsize=(10, 6))

    # Temperature vs. City
    sns.scatterplot(data=df, x='cities', y='Temperature', hue='Humidity', size='Wind Speed', sizes=(20, 200))
    plt.title('Temperature vs. Country')
    plt.xlabel('Country')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.show()

    # Humidity vs. City
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='cities', y='Humidity')
    plt.title('Humidity vs. Country')
    plt.xlabel('Country')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.show()
