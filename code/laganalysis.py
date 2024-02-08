import numpy as np
import statsmodels.api as sm
from scipy.stats import pearsonr

class LagAnalysis:
    """
    A class to perform lag analysis on EABL's stock prices against various market indicators.
    """
    def __init__(self, stock_data, indicators_data):
        self.stock_data = stock_data
        self.indicators_data = indicators_data
        
    def calculate_correlation(self, indicator_column):
        """
        Calculate the Pearson correlation coefficient between EABL's closing stock prices and a given market indicator.
        """
        # Ensuring alignment in dates between stock data and indicators data
        combined_data = self.stock_data[['Close']].merge(self.indicators_data[[indicator_column]], left_index=True, right_index=True, how='inner')
        correlation, p_value = pearsonr(combined_data['Close'], combined_data[indicator_column])
        return correlation, p_value
    
    def perform_lag_analysis(self, indicator_column, max_lag=12):
        """
        Perform lag analysis to determine the time lag effect of changes in market indicators on EABL's stock prices.
        """
        # Aligning the data based on dates for comparison
        combined_data = self.stock_data[['Close']].merge(self.indicators_data[[indicator_column]], left_index=True, right_index=True, how='inner')
        
        lags = range(0, max_lag+1)
        autocorrelations = [combined_data['Close'].autocorr(lag=lag) for lag in lags]
        
        return lags, autocorrelations