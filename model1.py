import pandas as pd
import numpy as np 
from xgboost import XGBRegressor, XGBClassifier
import xgboost as xgb   
from sklearn.metrics import classification_report
import joblib
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor, MultiOutputClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit
# from catboost import CatBoostClassifier

df = pd.read_csv('StockLogistic.csv')
# df.drop(columns=['Unnamed: 0','Month'], inplace=True) 
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.drop(columns=['Unnamed: 0','Unnamed: 0.1','Month','Year'], inplace=True)

from xgboost import plot_importance


# Create second class with tuned parameters. 
class XBoostTuned:
    def __init__(self, data):
        self.data = data
        # self.date_convert()
        self.split_data()
        self.train_baseline()
        
    def split_data(self):
        tscv = TimeSeriesSplit(n_splits=3)  # Define the number of splits
        
        # Initialize train and test lists
        train_indices = []
        test_indices = []
        
        for train_index, test_index in tscv.split(self.data):
            train_indices.append(train_index)
            test_indices.append(test_index)
        
        # Concatenate train and test data
        train_indices = [idx for split in train_indices for idx in split]
        test_indices = [idx for split in test_indices for idx in split]
        
        self.train = self.data.iloc[train_indices]
        self.test = self.data.iloc[test_indices]
        #Train the model    
    def train_baseline(self):
        target = ['Target','Target1','Target2','Target3']
        features = self.train.drop(columns=target).values
        target = self.train[target].values
        self.model = xgb.XGBClassifier(iterations=100, learning_rate=0.1, depth=3)
        self.model.fit(features, target)
    
    def predict(self, input_data):
        predictions = self.model.predict(input_data)
        return predictions
    
    def evaluate(self):
        target = ['Target','Target1','Target2','Target3']
        test_features = self.test.drop(columns=target).values
        preds = self.predict(test_features)
        actual = self.test[target]
        acc = classification_report(actual, preds)
        return acc
    
    def plot_feature_importance(self):
        plot_importance(self.model.estimators_[0])
        plt.title('Factors influencing stock price hikes')
        plt.show()

#Save the model in a pickle file.
    @staticmethod 
    def save_model(model, model_path='stock-increement2.pkl'):
         joblib.dump(model, model_path)


# Example usage:
boost_model = XBoostTuned(df)
# boost_model.date_convert()
boost_model.split_data()
boost_model.train_baseline()
accuracy = boost_model.evaluate()
print(accuracy)
boost_model.save_model(boost_model.model)



