from flask import Flask, request, render_template, session
from datetime import timedelta
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.permanent_session_lifetime = timedelta(days=1)

api_key = "fce67aa670f3c98312d40a306b112b8e"
base_url = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city")
    units = request.args.get("units", "imperial")
    weather = None
    error = None

    # session
    session.permanent = True
    history = session.get("history", [])

    if city:
        city = city.strip()
        city_title = city.title()

        # Updating search history
        if city_title not in history:
            history.insert(0, city_title)
            history = history[:5]
            session["history"] = history

        params = {
            "q": city,
            "appid": api_key,
            "units": units
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": city_title,
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

    return render_template("index.html", weather=weather, error=error, selected_units=units, history=session.get("history", []))



if __name__ == "__main__":
    app.run(debug=True)
