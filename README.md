# 🌤️ ClimaTest (Weather App)

A polished weather app built with Flask, Bootstrap, and the OpenWeatherMap API.

- ✅ Real-time weather data by city
- 🌎 Location detection by IP
- 🌓 Dark mode toggle
- 🌀 Loading spinner
- 💾 Recent search memory (session)
- 🔒 API key securely hidden using `.env`

---

## 🚀 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/rinnemunch/weather-app.git
cd weather-app
```

2. Set Up Virtual Environment
   python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate on Windows

3. Install Dependencies
   pip install -r requirements.txt

4. Create .env File
   Create a .env file in the project root and add your OpenWeather API key:
   API_KEY=your_api_key_here
   You can get a free key at openweathermap.org.

5. Run the App
   python app.py
   Then visit: http://localhost:5000

📦 Stack

- Python / Flask

- HTML / Bootstrap 5

- JavaScript

- OpenWeatherMap API

- dotenv for secret management

## 📸 Screenshot

![Screenshot](screenshot.png)

🛡️ Notes
This is a learning/demo project and not meant for production use.
The API key is securely handled with environment variables.

Created by Shaun Fulton
