import numpy as np
import matplotlib.pyplot as plt

class VolatilityInsights:
    """
    A class to calculate and analyze stock volatility.
    """
    def __init__(self, data):
        self.data = data
        # Calculate daily returns
        self.data['Daily Returns'] = self.data['Close'].pct_change()
        # Calculate rolling 30-day volatility (standard deviation of daily returns)
        self.data['Volatility'] = self.data['Daily Returns'].rolling(window=30).std() * np.sqrt(252)

    def plot_volatility(self):
        """
        Plot the rolling 30-day volatility.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['Volatility'], label='Rolling 30-Day Volatility')
        plt.title('EABL Stock Volatility Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volatility')
        plt.legend()
        plt.show()

