import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import autocorrelation_plot

class TrendAnalysis:
    """
    A class to perform trend analysis on stock prices.
    """
    def __init__(self, data):
        self.data = data
        self.data.set_index('Date', inplace=True)
        
    def decompose_series(self, model='additive', freq='M'):
        """
        Decompose the time series into its trend, seasonal, and residual components.
        """
        # Assuming 'Close' price for analysis
        decomposition = seasonal_decompose(self.data['Close'], model=model, period=self._determine_period(freq))
        return decomposition
    
    def plot_decomposition(self, decomposition):
        """
        Plot the decomposed components of the time series.
        """
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(14, 10))
        decomposition.observed.plot(ax=ax1)
        ax1.set_title('Observed')
        decomposition.trend.plot(ax=ax2)
        ax2.set_title('Trend')
        decomposition.seasonal.plot(ax=ax3)
        ax3.set_title('Seasonal')
        decomposition.resid.plot(ax=ax4)
        ax4.set_title('Residual')
        plt.tight_layout()
    
    def plot_autocorrelation(self):
        """
        Plot the autocorrelation of the 'Close' price to identify any autocorrelation patterns.
        """
        plt.figure(figsize=(14, 7))
        autocorrelation_plot(self.data['Close'])
        plt.title('Autocorrelation of EABL Closing Prices')
        plt.show()
    
    def _determine_period(self, freq):
        """
        Helper method to determine the period for seasonal decomposition based on frequency.
        """
        if freq == 'M':
            return 12  # Monthly data
        elif freq == 'Q':
            return 4  # Quarterly data
        else:
            return 52  # Weekly data, as a default