# Import pandas library
import pandas as pd

# Define the relative path to the csv file
csv_path = r"C:\Users\ADMIN\OneDrive\Desktop\EABL\EABL-Stock-Performance-Analysis-with-Data\data\raw\stockdata.csv"

import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def explore_time_series_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    
    # Display descriptive summary
    print("Descriptive Summary:")
    print(data.describe())
    print("\n")
    
    # Convert to datetime and set index
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Plot the time series
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], color='blue')
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.grid(True)
    plt.show()
    
    # Check for stationarity
    result = adfuller(data['Value'])
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'   {key}: {value}')
    if result[1] <= 0.05:
        print("The series is likely stationary.")
    else:
        print("The series is likely non-stationary.")

# Example usage:
if __name__ == "__main__":
    explore_time_series_data( r"C:\Users\ADMIN\OneDrive\Desktop\EABL\EABL-Stock-Performance-Analysis-with-Data\data\raw\stockdata.csv")
