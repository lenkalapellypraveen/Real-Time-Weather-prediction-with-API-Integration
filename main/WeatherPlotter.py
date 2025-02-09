import matplotlib.pyplot as plt

class WeatherPlotter:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def plot_weather_data(self, save_path):
        plt.figure(figsize=(20, 5))
        for i in range(len(self.weather_data['forecast']['forecastday'])):
            date = self.weather_data['forecast']['forecastday'][i]['date']
            max_temp = self.weather_data['forecast']['forecastday'][i]['day']['maxtemp_f']
            plt.plot(date, max_temp, marker='D', label=f'Day {i+1}')

        plt.title('Temperature Trends')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°F)')
        plt.legend()
        plt.grid(True)
        plt.savefig(save_path)
        plt.close()
