import requests
import pandas as pd

class DataFetcher:
    def __init__(self, base_url, api_key, city_name, start_date, end_date):
        self.base_url = base_url
        self.api_key = api_key
        self.city_name = city_name
        self.start_date = start_date
        self.end_date = end_date

    def fetch_weather_data(self):
        url = f"{self.base_url}?key={self.api_key}&q={self.city_name}&dt={self.start_date}&end_dt={self.end_date}"
        try:
            response = requests.get(url)
            weather_data = response.json()
            print('Weather Data Fetched:', weather_data)
            return pd.DataFrame(weather_data)
        except requests.exceptions.RequestException as e:
            print("HTTP Request failed:", e)
            return pd.DataFrame()
        except Exception as e:
            print("An unexpected error occurred:", e)
            return pd.DataFrame()
