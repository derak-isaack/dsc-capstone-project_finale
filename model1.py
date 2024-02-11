import pandas as pd
from xgboost import XGBRegressor, XGBClassifier
from sklearn.metrics import classification_report
import joblib
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor, MultiOutputClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

df = pd.read_csv('StockLogistic.csv')
# df.drop(columns=['Unnamed: 0','Month'], inplace=True) 

from xgboost import plot_importance


# Create second class with tuned parameters. 
class XBoostTuned:
    def __init__(self, data):
        self.data = data
        self.date_convert()
        self.split_data()
        self.train_baseline()
        
        # Convert the date column and set it as index.
    def date_convert(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data = self.data.set_index('Date')
        
    def fill_missing(self):
         self.data['Mean'].fillna(method='ffill', inplace=True)
         self.data[['Dividends per share','Earnings Per Share']] = self.data[['Dividends per share','Earnings Per Share']].fillna(method='bfill')
         
    # Split the data.
    def split_data(self):
        train_size = int(len(self.data) * 0.8)
        self.train = self.data.iloc[:train_size]
        self.test = self.data.iloc[train_size:]
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

class SaveModel(XBoostTuned):
    def save_model(model, model_path='stock-increement.pkl'):
        joblib.dump(model, open(model_path, 'wb'))


# Example usage:
boost_model = XBoostTuned(df)
boost_model.date_convert()
boost_model.split_data()
boost_model.train_baseline()
accuracy = boost_model.evaluate()
print(accuracy)
pipeline_xgboost2 = SaveModel(boost_model)
pipeline_xgboost2.save_model() 

# df.drop(columns=['Unnamed: 0','Year'], inplace=True) 
# df['Tommorow'] = df['Close'].shift(-1)
# df['Target'] = (df['Tommorow'] > df['Close']).astype(int)
# class XGBOOST:
#     def __init__(self, data):
#          self.data = data
    
#     # Set the date as the index.  
#     def date_convert(self):
#          self.data['Date'] = pd.to_datetime(self.data['Date'])
#          self.data = self.data.set_index('Date')
        
     
#     # Drop ro ws with missing values
#     def fill_missing(self):
#         self.data['Mean'].fillna(method='ffill', inplace=True)
#         self.data[['Dividends per share','Earnings Per Share']] = self.data[['Dividends per share','Earnings Per Share']].fillna(method='bfill')
    
#     # Split data using the TrainTestSplit. 
#     def split_data(self):
#         self.X = self.data.drop(columns=['Close','High','Low','Open'], axis=1)
#         self.y = self.data[['High', 'Low', 'Close','Open']]
#         self.X_train, self.X_test, self.y_train, self.y_test,  = train_test_split(self.X, self.y, random_state=42, test_size=0.25)
    
#     #Fit the model on te mltioutput regressor.                                                                                                           
#     def fit(self):
#         self.model = MultiOutputRegressor(LinearRegression())
#         self.model.fit(self.X_train, self.y_train)
    
#     # Generate predictions for the test set.    
#     def predict(self):
#         preds = self.model.predict(self.X_test) 
#         return preds
    
    # Calculate diffreence between predicted and actual values. 
#     def difference_outputs(self):
#         preds = self.predict()
#         self.y_test['High'] = self.y_test['High'] - preds[:, 0]
#         self.y_test['Low'] = self.y_test['Low'] - preds[:, 1]
#         self.y_test['Close'] = self.y_test['Close'] - preds[:, 2]
#         self.y_test['Open'] = self.y_test['Open'] - preds[:, 3]
#         return self.y_test
    
#     # Evaluate the model. 
#     def score(self):
#         y_pred = self.predict()
#         r2_scores = r2_score(self.y_test, y_pred, multioutput='uniform_average')
#         mse = mean_squared_error(self.y_test, y_pred, multioutput='uniform_average')
#         return r2_scores, mse

# # Save the model.  
# class SaveModel(XGBOOST):
#      def save_model(model, model_path='stock-high-low2.pkl'):
#          joblib.dump(model, open(model_path, 'wb'))


# # Example usage:
# boost_model = XGBOOST(df)
# boost_model.date_convert()
# boost_model.split_data()
# boost_model.train_tree()
# accuracy = boost_model.evaluate()
# print(accuracy)
# pipeline_xgboost2 = SaveModel(boost_model)
# pipeline_xgboost2.save_model() 


