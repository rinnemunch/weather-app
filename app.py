from flask import Flask, request, render_template
import requests

app = Flask(__name__)

api_key = "fce67aa670f3c98312d40a306b112b8e"
base_url = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city")
    units = request.args.get("units", "imperial")  # default to Fahrenheit
    weather = None
    error = None

    if city:
        city = city.strip()

        params = {
            "q": city,
            "appid": api_key,
            "units": units
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": city.title(),
                "temp": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        elif response.status_code == 401:
            error = "Invalid API key."
        elif response.status_code == 404:
            error = "City not found."
        else:
            error = f"Error: {response.status_code}"

    return render_template("index.html", weather=weather, error=error, selected_units=units)


if __name__ == "__main__":
    app.run(debug=True)
