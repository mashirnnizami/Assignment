import requests

# Replace 'YOUR_API_URL' with the actual URL of your API
API_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'

def get_weather_data(date):
    # Make an HTTP request to fetch the weather data from the API
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'] == date:
                return item['main']['temp']
        return None
    else:
        print('Error fetching weather data from the API.')
        return None

def get_wind_speed(date):
    # Make an HTTP request to fetch the weather data from the API
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'] == date:
                return item['wind']['speed']
        return None
    else:
        print('Error fetching weather data from the API.')
        return None

def get_pressure(date):
    # Make an HTTP request to fetch the weather data from the API
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'] == date:
                return item['main']['pressure']
        return None
    else:
        print('Error fetching weather data from the API.')
        return None

def main():
    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_weather_data(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Data not found for the specified date.")
        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the specified date.")
        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the specified date.")
        elif choice == '0':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
