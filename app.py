import requests

api_key = "fce67aa670f3c98312d40a306b112b8e"
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ").strip()

if city == "":
  print("Please enter a valid city name.")
else:
  params = {
    "q": city,
    "appid": api_key,
    "units": "imperial"
  }

  response = requests.get(base_url, params=params)

  if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"{city.title()} Weather: {description}, {temp}°F")
  else:
    print("City not found or API error.")
