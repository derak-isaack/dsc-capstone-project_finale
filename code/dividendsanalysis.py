import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class DividendsAnalysis:
    """
    A class for analyzing dividend payout trends.
    """
    def __init__(self, data):
        self.data = data
        # Ensure there's a 'Year' column for annual analysis
        if 'Year' not in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data['Year'] = self.data['Date'].dt.year
        self.dividend_data = self.data[['Year', 'Dividends per share']].drop_duplicates().dropna()
        
    def calculate_dividend_growth(self):
        """
        Calculate the year-over-year growth rate of dividends per share.
        """
        self.dividend_data['Growth'] = self.dividend_data['Dividends per share'].pct_change() * 100
        return self.dividend_data
    
    def plot_dividend_trends(self):
        """
        Visualize the trends in dividend payouts over time, including growth rates.
        """
        fig, ax1 = plt.subplots(figsize=(14, 7))

        color = 'tab:red'
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Dividends per Share', color=color)
        ax1.plot(self.dividend_data['Year'], self.dividend_data['Dividends per share'], color=color, label='Dividends per Share')
        ax1.tick_params(axis='y', labelcolor=color)
        
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'tab:blue'
        ax2.set_ylabel('Growth Rate (%)', color=color)  # we already handled the x-label with ax1
        ax2.plot(self.dividend_data['Year'], self.dividend_data['Growth'], color=color, label='Growth Rate')
        ax2.tick_params(axis='y', labelcolor=color)
        
        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        plt.title('EABL Dividends per Share and Growth Rate Over Time')
        plt.show()
