import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, r2_score, mean_squared_error
import joblib
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('MergedData/final_merge.csv')
df.drop(columns=['Unnamed: 0','Year'], inplace=True) 
class LinearRegressor:
    def __init__(self, data):
        self.data = data
        self.date_convert()
        self.fill_missing()
        self.split_data()
        self.fit()
        
    def date_convert(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        
    def fill_missing(self):
        self.data['Mean'].fillna(method='ffill', inplace=True)
        self.data[['Dividends per share','Earnings Per Share']] = self.data[['Dividends per share','Earnings Per Share']].fillna(method='bfill')
        self.data['Annual Average Inflation'].fillna(method='bfill', inplace=True) 
    
    def split_data(self):
        self.X = self.data.drop(columns=['Close','High','Low','Open'], axis=1)
        self.y = self.data[['High', 'Low', 'Close','Open']]
        # self.dates = self.data['Date']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,random_state=42, test_size=0.25)
                                                                                                                   
                                                                                                                    
                                                                                                                
    def fit(self):
        self.model = MultiOutputRegressor(LinearRegression())
        self.model.fit(self.X_train, self.y_train)
        
    def predict(self):
        return self.model.predict(self.X_test) 
    
    def score(self):
        y_pred = self.predict()
        r2_scores = r2_score(self.y_test, y_pred, multioutput='uniform_average')
        mse = mean_squared_error(self.y_test, y_pred, multioutput='uniform_average')
        return r2_scores, mse
    
    # def get_business_days_predictions(self):
    #     test_predictions = self.model.predict(self.X_test)
    #     dates_predictions = pd.DataFrame(test_predictions, index=self.X_test.index, columns=['High', 'Low', 'Close', 'Open'])
    #     dates_predictions = dates_predictions.sort_index()
    #     business_days = dates_predictions[dates_predictions.index.dayofweek < 5]
    #     return business_days

class SaveModel(LinearRegressor):
    def save_model(model, model_path='close-high-low.pkl'):
        joblib.dump(model, open(model_path, 'wb'))
    
linear_regressor = LinearRegressor(df)
# business_day_predictions = pd.DataFrame(linear_regressor.get_business_days_predictions())
# business_day_predictions.head()
# business_day_predictions.to_csv("business_day_predictions.csv")
r2_scores, mse = linear_regressor.score()
print("R2 Scores:", r2_scores)
print("Mean Squared Error:", mse)
pipeline_lgb2 = SaveModel(linear_regressor)
pipeline_lgb2.save_model() 