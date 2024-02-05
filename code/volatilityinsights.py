import numpy as np
import matplotlib.pyplot as plt

class VolatilityInsights:
    """
    A class to calculate and analyze stock volatility, including displaying the calculated volatility rate.
    """
    def __init__(self, data):
        self.data = data
        self.data['Returns'] = self.data['Close'].pct_change()
        
    def calculate_volatility(self, window=252):
        """
        Calculate rolling volatility using the standard deviation of daily returns,
        and return the last calculated volatility rate.
        """
        self.data['Volatility'] = self.data['Returns'].rolling(window=window).std() * np.sqrt(window)
        return self.data['Volatility'].iloc[-1]  # Return the latest volatility rate
    
    def plot_volatility(self):
        """
        Plot the rolling volatility over time, including the latest calculated volatility rate.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['Volatility'], label='Rolling Volatility')
        plt.title('EABL Stock Volatility Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volatility')
        plt.legend()
        plt.show()
        
        # Display the latest calculated volatility rate
        latest_volatility_rate = self.data['Volatility'].iloc[-1]
        print(f"Calculated Volatility Rate: {latest_volatility_rate * 100:.2f}%")
