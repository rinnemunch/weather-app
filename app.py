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
    temp = round(data["main"]["temp"])
    description = data["weather"][0]["description"].title()

    print("\n☀️ Weather Report ☀️")
    print(f"City: {city.title()}")
    print(f"Condition: {description}")
    print(f"Temperature: {temp}°F")

  elif response.status_code == 401:
    print("Error: Invalid API key. Check your credentials.")

  elif response.status_code == 404:
    print("Error: City not found. Double-check the spelling.")

  else:
    print(f"Error: Something went wrong. (Code {response.status_code})")
