import requests
api_key = "94e2a957a69a54c46201c096117b4fc2"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching data from the API...")
    try: 
        response = requests.get(api_url)
        response.raise_for_status() 
        print("API response received successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-03-24 21:59', 'localtime_epoch': 1774389540, 'utc_offset': '-4.0'}, 'current': {'observation_time': '01:59 AM', 'temperature': 4, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '06:53 AM', 'sunset': '07:13 PM', 'moonrise': '10:05 AM', 'moonset': '01:16 AM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 30}, 'air_quality': {'co': '301.85', 'no2': '47.85', 'o3': '27', 'so2': '8.65', 'pm2_5': '16.95', 'pm10': '17.05', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 21, 'wind_degree': 196, 'wind_dir': 'SSW', 'pressure': 1028, 'precip': 0, 'humidity': 48, 'cloudcover': 0, 'feelslike': 0, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}