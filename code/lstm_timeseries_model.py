from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

class LSTMTimeSeriesModel:
    def __init__(self, look_back=5, epochs=20, batch_size=20, lstm_units=50):
        self.look_back = look_back
        self.epochs = epochs
        self.batch_size = batch_size
        self.lstm_units = lstm_units
        self.model = None
        self.scaler = MinMaxScaler()

    def preprocess_data(self, data, date_column='Date'):
        data[date_column] = pd.to_datetime(data[date_column])
        data.set_index(date_column, inplace=True)
        
        # Normalize the data
        self.data_scaled = self.scaler.fit_transform(data)
        
        # Split the dataset into training and testing sets
        self.split_idx = int(len(self.data_scaled) * 0.8)
        self.train, self.test = self.data_scaled[:self.split_idx], self.data_scaled[self.split_idx:]
    
    def build_model(self, input_shape):
        self.model = Sequential([
            LSTM(self.lstm_units, activation='relu', input_shape=input_shape),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        
    def train_model(self):
        # Prepare data for LSTM model using TimeseriesGenerator
        train_generator = TimeseriesGenerator(self.train, self.train, length=self.look_back, batch_size=self.batch_size)
        input_shape = (self.look_back, self.train.shape[1])
        
        self.build_model(input_shape)
        self.model.fit(train_generator, epochs=self.epochs, verbose=1)

    def predict(self):
        test_generator = TimeseriesGenerator(self.test, self.test, length=self.look_back, batch_size=1)
        predictions = self.model.predict(test_generator)
        
        # Invert scaling for prediction data
        predictions_inverted = self.scaler.inverse_transform(predictions)
        
        return predictions_inverted
    
    def visualize_and_evaluate(self,predictions, actual, start_idx=0):
        """
        Visualizes the LSTM model predictions against the actual values and calculates performance metrics.

        :param predictions: The predicted values returned by the model.
        :param actual: The actual values to compare against the predictions.
        :param start_idx: The starting index from which to display the actual values. This accounts for the look_back period.
        """
        # Ensure the actual values start from the correct index to align with predictions
        actual_aligned = actual[start_idx:]

        # Calculate metrics
        mae = mean_absolute_error(actual_aligned, predictions)
        rmse = np.sqrt(mean_squared_error(actual_aligned, predictions))

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(actual_aligned, label='Actual', color='blue', marker='o')
        plt.plot(predictions, label='Predicted', color='red', linestyle='--', marker='x')
        plt.title('LSTM Time Series Prediction')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

        # Print metrics
        print(f"Mean Absolute Error (MAE): {mae:.4f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")