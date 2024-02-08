import numpy as np
import matplotlib.pyplot as plt

class TradeVolumeAnalysis:
    def __init__(self, data):
        self.data = data
    
    def detect_spikes(self, threshold=2):
        """Identify days with abnormal trade volume spikes.
        
        Args:
            threshold (float): The number of standard deviations from the mean to consider a spike.
        
        Returns:
            DataFrame: A subset of the original DataFrame with only the days of abnormal volume spikes.
        """
        self.data['Volume_Mean'] = self.data['Volume'].rolling(window=30).mean()
        self.data['Volume_Std'] = self.data['Volume'].rolling(window=30).std()
        self.data['Z_Score'] = (self.data['Volume'] - self.data['Volume_Mean']) / self.data['Volume_Std']
        
        # Filter rows where the Z-score is above the threshold
        spikes = self.data[self.data['Z_Score'] > threshold]
        return spikes
    
    def plot_volume_spikes(self):
        """Plot the daily trade volume with highlights on days of abnormal spikes."""
        plt.figure(figsize=(20, 8))
        plt.plot(self.data['Date'], self.data['Volume'], label='Daily Volume')
        
        # Detect spikes
        spikes = self.detect_spikes()
        
        plt.scatter(spikes['Date'], spikes['Volume'], color='red', label='Volume Spikes')
        plt.title('EABL Trade Volume with Abnormal Spikes Highlighted')
        plt.xlabel('Date')
        plt.ylabel('Trade Volume')
        plt.legend()
        plt.show()

        return spikes