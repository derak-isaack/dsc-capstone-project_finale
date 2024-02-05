import numpy as np
import matplotlib.pyplot as plt

class AbnormalVolumeAnalysis:
    """
    A class to identify and analyze abnormal trade volumes.
    """
    def __init__(self, data):
        self.data = data
        self.data['Volume_Z_Score'] = (self.data['Volume'] - self.data['Volume'].mean()) / self.data['Volume'].std()
        
    def detect_abnormal_volumes(self, threshold=2):
        """
        Identify days with abnormal trading volumes based on the z-score threshold.
        A z-score above the threshold indicates a significant spike in volume.
        """
        self.data['Abnormal_Volume'] = self.data['Volume_Z_Score'].abs() >= threshold
        return self.data[self.data['Abnormal_Volume']]
    
    def plot_abnormal_volumes(self):
        """
        Visualize trading volumes and highlight days with abnormal volumes.
        """
        plt.figure(figsize=(14, 7))
        plt.bar(self.data['Date'], self.data['Volume'], color='blue', label='Daily Volume')
        # Highlight abnormal volume days
        abnormal_days = self.data[self.data['Abnormal_Volume']]
        plt.scatter(abnormal_days['Date'], abnormal_days['Volume'], color='red', label='Abnormal Volume')
        plt.title('EABL Trade Volume with Abnormal Spikes Highlighted')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.legend()
        plt.show()