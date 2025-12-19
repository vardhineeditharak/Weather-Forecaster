from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
            error_message = "API Configuration missing."
            return render_template("index.html", error_message=error_message)

        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&units=metric&appid={api_key}"
        )

        try:
            response = requests.get(weather_url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "City not found."
        except Exception:
            error_message = "Connection error."

    return render_template("index.html", 
                           weather_data=weather_data, 
                           error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)