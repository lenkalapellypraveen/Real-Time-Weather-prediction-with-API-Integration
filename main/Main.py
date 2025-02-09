# Initialize data fetcher
from DataFetcher import DataFetcher
from jinja2 import Environment, FileSystemLoader
from ModelBuilder import ModelBuilder
from WeatherPlotter import WeatherPlotter
from WeatherPredictor import Predictor
import json
import warnings
warnings.filterwarnings("ignore")

fetcher = DataFetcher(base_url="http://api.weatherapi.com/v1/history.json", api_key="5432ef5ea25245c880741124250102",
                      city_name="Boca Raton", start_date="2025-01-01", end_date="2025-01-30")
weather_df = fetcher.fetch_weather_data()

if not weather_df.empty:
    # Plot weather data
    plotter = WeatherPlotter(weather_data=weather_df)
    plotter.plot_weather_data(save_path='C:\\Users\\prave\\Documents\\DataScience\\DataScienceHub\\WeatherPrediction\\src\\main\\temperature_trends.png')

    # Build and evaluate model
    builder = ModelBuilder(weather_data=weather_df)
    model = builder.build_and_evaluate_model()

    # load the template
    file_loader = FileSystemLoader('C:\\Users\\prave\\Documents\\DataScience\\DataScienceHub\\WeatherPrediction\\src\\test')
    env = Environment(loader=file_loader)
    template = env.get_template('Template.txt')

    # Load future weather data from JSON
    with open('C:\\Users\\prave\\Documents\\DataScience\\DataScienceHub\\WeatherPrediction\\src\\test\\future_weather_data.json', 'r') as file:
        data = json.load(file)
        future_weather_data = data['future_weather_data']

    # Make future predictions for each set of data
    predicted_temperatures = []
    predictor = Predictor(model=model)
    for forecast in future_weather_data:
        predicted_temp = predictor.predict_future_temperatures(forecast)
        forecast.update({"predicted_temp": predicted_temp[0]})
        predicted_temperatures.append(forecast)

    # Render the template with all predicted temperatures
    output = template.render(future_weather_data=predicted_temperatures)

    # Print the rendered output or use it in emails, etc.
    print(output)

    # Saving the output to a text file
    with open("C:\\Users\\prave\\Documents\\DataScience\\DataScienceHub\\WeatherPrediction\\src\\test\\weather_predictions_output.txt", "w") as f:
        f.write(output)
