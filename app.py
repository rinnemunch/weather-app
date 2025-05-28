from flask import Flask, request, render_template, jsonify
from datetime import timedelta
import requests
from db import init_db, add_city, get_recent_cities, clear_history as clear_db_history
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = "dev"


api_key = os.getenv("API_KEY")
base_url = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/detect-location")
def detect_location():
    try:
        ip_response = requests.get("https://ipinfo.io/json")
        if ip_response.status_code == 200:
            data = ip_response.json()
            return jsonify({"city": data.get("city", "")})
        else:
            return jsonify({"city": ""})
    except:
        return jsonify({"city": ""})


@app.route("/clear-history", methods=["POST"])
def clear_history():
    clear_db_history()
    return "", 204  # No content clear it all up!


@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city")
    units = request.args.get("units", "imperial")
    weather = None
    error = None

    history = get_recent_cities()

    if city:
        city = city.strip()
        city_title = city.title()

        if city_title not in history:
            add_city(city_title)

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

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        selected_units=units,
        history=history,
        api_key=api_key
    )




init_db()

if __name__ == "__main__":
    app.run(debug=True)
