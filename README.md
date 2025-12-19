# Weather-Forecaster 🌤️

A simple web application that shows real-time weather information for any city.

Built using **Python (Flask)** and a public weather API, this project focuses on clean UI, API integration, and backend-frontend interaction.

---

## Screenshots

![Home](sample-image-1.png)
![Weather Result](sample-image-2.png)

---

## Features

- Search weather by city name
- Shows:
  - Current temperature
  - Date and location
  - Weather condition
  - Humidity
  - Wind speed
- Simple, responsive card-based UI
- Error handling for invalid inputs

---

## Tech Stack

- Python
- Flask
- HTML, CSS, JavaScript
- Weather API

---

## Project Structure
```bash
Weather-Forecaster/
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
├── static/
  ├── css/
  └── js/

---

## Live Demo
https://weather-forecaster-y9pe.onrender.com

---

## Setup (Local)

```bash
git clone https://github.com/vardhineeditharak/Weather-Forecaster.git
cd Weather-Forecaster
pip install -r requirements.txt
python app.py

## Create a .env file:
API_KEY=your_weather_api_key

## Open
http://localhost:5000

## Deployment
Deployed using Render with environment variables for API security.
