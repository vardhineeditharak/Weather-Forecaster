from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
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
            error_message = "API Key missing. Please check your .env file."
            return render_template("index.html", error_message=error_message)

        # OpenWeatherMap Current Weather API URL
        # Using units=metric for Celsius
        weather_url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&units=metric&appid={api_key}"
        )

        try:
            response = requests.get(weather_url)
            
            if response.status_code == 200:
                weather_data = response.json()
            elif response.status_code == 404:
                error_message = "City not found. Please try again."
            else:
                error_message = "An error occurred with the weather service."
                
        except requests.exceptions.RequestException:
            error_message = "Could not connect to the weather service."

    return render_template(
        "index.html",
        weather_data=weather_data,
        error_message=error_message
    )

if __name__ == "__main__":
    # In a production environment at Google, we wouldn't use debug=True
    # But for local development, it's perfect.
    app.run(debug=True)