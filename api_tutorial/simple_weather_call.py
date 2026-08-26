import requests

# Open-Meteo needs no API key. Latitude/longitude for Ames, Iowa.
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=42.03&longitude=-93.62&current_weather=true"

response = requests.get(API_URL)

print(response.status_code)
print(response.text)
