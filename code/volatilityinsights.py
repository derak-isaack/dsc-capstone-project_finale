import numpy as np
import matplotlib.pyplot as plt

class StockVolatility:
    def __init__(self, data):
        self.data = data
        self.returns = None
    
    def calculate_returns(self):
        """Calculate daily returns from the Close prices."""
        self.data['Returns'] = self.data['Close'].pct_change()
        self.returns = self.data['Returns']
    
    def calculate_volatility(self):
        """Calculate the annualized volatility of the stock."""
        daily_volatility = self.returns.std()
        annualized_volatility = daily_volatility * np.sqrt(252)  # Assuming 252 trading days in a year
        return annualized_volatility
    
    def plot_volatility(self):
        """Plot the rolling 30-day volatility of the stock."""
        rolling_volatility = self.returns.rolling(window=30).std() * np.sqrt(252)
        plt.figure(figsize=(10, 6))
        rolling_volatility.plot()
        plt.title('30-Day Rolling Volatility of EABL Stock')
        plt.xlabel('Date')
        plt.ylabel('Annualized Volatility')
        plt.show()
