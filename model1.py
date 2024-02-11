import pandas as pd
from xgboost import XGBRegressor, XGBClassifier
from sklearn.metrics import classification_report
import joblib
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor, MultiOutputClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit

df = pd.read_csv('StockLogistic.csv')
# df.drop(columns=['Unnamed: 0','Month'], inplace=True) 
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.drop(columns=['Unnamed: 0','Month','Year'], inplace=True)

from xgboost import plot_importance


# Create second class with tuned parameters. 
class XBoostTuned:
    def __init__(self, data):
        self.data = data
        # self.date_convert()
        self.split_data()
        self.train_baseline()
        
        # Convert the date column and set it as index.
    # def date_convert(self):
    #     self.data['Date'] = pd.to_datetime(self.data['Date'])
    #     self.data = self.data.set_index('Date')
        
    # def fill_missing(self):
    #      self.data['Mean'].fillna(method='ffill', inplace=True)
    #      self.data[['Dividends per share','Earnings Per Share']] = self.data[['Dividends per share','Earnings Per Share']].fillna(method='bfill')
         
    # Split the data.
    # def split_data(self):
    #     train_size = 3400
    #     self.train = self.data[:train_size]
    #     self.test = self.data[train_size:]
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
        self.model = MultiOutputClassifier(XGBClassifier(learning_rate=0.2, n_estimators=300, max_depth=4))
        
        # Train the best model
        self.model.fit(self.train.drop(columns=target), self.train[target])
        
    def predict_classes(self):
        target = ['Target','Target1','Target2','Target3'] 
        probs = self.model.predict(self.test.drop(columns=target))
        return probs 
    # Evaluate the model.
    def evaluate(self):
        target = ['Target','Target1','Target2','Target3']
        probs = self.predict_classes()
        actual = self.test[target] 
        acc = classification_report(actual, probs)
        return acc 
    # Plot the features. 
    def plot_feature_importance(self):
        plot_importance(self.model.estimators_[0])
        plt.title('Factors influencing stock price hikes')
        plt.show()

#Save the model in a pickle file. 
    def save_model(model, model_path='stock-increement.pkl'):
         joblib.dump(model, open(model_path, 'wb'))


# Example usage:
boost_model = XBoostTuned(df)
# boost_model.date_convert()
boost_model.split_data()
boost_model.train_baseline()
accuracy = boost_model.evaluate()
print(accuracy)
boost_model.save_model()



