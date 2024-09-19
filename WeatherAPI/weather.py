import requests

API_KEY = "64e138e7ab802d064e79e5ea8df63b32"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city name:")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code ==200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather:", weather)
    temperature = round(data['main']['temp'] - 273.15,2)
    print("Temperature:",temperature, "C")

else:
    print("Error in fetching data")
   

