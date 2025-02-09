from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class ModelBuilder:
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.model = None

    def build_and_evaluate_model(self):
        X_data = [[day['day']['avgtemp_f'], day['day']['maxwind_mph'], day['day']['avghumidity']]
                  for day in self.weather_data['forecast']['forecastday']]
        y_data = [day['day']['avgtemp_f'] - 0.7 * day['day']['maxwind_mph'] + 0.2 * day['day']['avghumidity']
                  for day in self.weather_data['forecast']['forecastday']]

        X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=0)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
        print("Model Coefficients:", self.model.coef_)
        return self.model
