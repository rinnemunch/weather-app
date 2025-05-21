from flask import Flask, request, render_template
import requests

app = Flask(__name__)

api_key = "fce67aa670f3c98312d40a306b112b8e"
base_url = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET"])
def index():
  city = request.args.get("city")

  if not city:
    return render_template("index.html")

  city = city.strip()


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

    return (
        f"<h2>☀️ Weather Report ☀️</h2>"
        f"<p><strong>City:</strong> {city.title()}<br>"
        f"<strong>Condition:</strong> {description}<br>"
        f"<strong>Temperature:</strong> {temp}°F</p>"
    )

  elif response.status_code == 401:
    return ("Error: Invalid API key. Check your credentials.")

  elif response.status_code == 404:
    return ("Error: City not found. Double-check the spelling.")

  else:
    return (f"Error: Something went wrong. (Code {response.status_code})")

if __name__ == "__main__":
  app.run(debug=True)
