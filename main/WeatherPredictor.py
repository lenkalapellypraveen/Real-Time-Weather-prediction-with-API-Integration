import pandas as pd
import logging

class Predictor:
    def __init__(self, model):
        self.model = model
        logging.basicConfig(level=logging.INFO)

    def predict_future_temperatures(self, future_data):
        try:
            # Ensure future_data contains all necessary columns
            if not all(key in future_data for key in ['avgtemp_f', 'maxwind_mph', 'avghumidity']):
                raise ValueError(
                    "Missing data in future_data; all predictions require 'avgtemp_f', 'maxwind_mph', and 'avghumidity' keys.")

            future_df = pd.DataFrame([future_data])
            logging.info("DataFrame created successfully for future data.")
            predictions = self.model.predict(future_df)
            logging.info("Predictions completed successfully.")
            return predictions
        except Exception as e:
            logging.error(f"Prediction failed: {e}")
            raise
