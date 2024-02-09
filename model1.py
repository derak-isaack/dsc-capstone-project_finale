import pandas as pd

from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv('MergedData/final_merge.csv')
df.drop(columns=['Unnamed: 0','Year'], inplace=True) 
df['Tommorow'] = df['Close'].shift(-1)
df['Target'] = (df['Tommorow'] > df['Close']).astype(int)
class XGBOOST:
    def __init__(self, data):
        self.data = data
        
    def date_convert(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data = self.data.set_index('Date')
        
    def split_data(self):
        train_size = int(len(self.data) * 0.8)
        train_data = self.data.iloc[:train_size]
        test_data = self.data.iloc[train_size:]
        self.train = train_data
        self.test = test_data
        
    def train_tree(self):
        # Select all columns except the 'Target' column as predictors
        predictors = self.train.drop(columns=['Target']).columns.tolist()
        target = 'Target'
        self.model = XGBClassifier()
        
        # Drop rows with missing values
        self.train.dropna(inplace=True)
        
        self.model.fit(self.train[predictors], self.train[target])
        return predictors 
    
    def predict_probabilities(self):
        # Use the same predictors used during training
        predictors = self.train.drop(columns=['Target']).columns.tolist()
        
        # Drop rows with missing values
        self.test.dropna(inplace=True)
        
        probs = self.model.predict_proba(self.test[predictors])[:, 1]
        return probs 
    
    def evaluate(self, threshold=0.5):
        probs = self.predict_probabilities()
        preds = (probs >= threshold).astype(int)  
        actual = self.test['Target']  
        acc = classification_report(actual, preds)
        return acc 
class SaveModel(XGBOOST):
    def save_model(model, model_path='stock-high-low2.pkl'):
        joblib.dump(model, open(model_path, 'wb'))


# Example usage:
boost_model = XGBOOST(df)
boost_model.date_convert()
boost_model.split_data()
boost_model.train_tree()
accuracy = boost_model.evaluate()
print(accuracy)
pipeline_xgboost2 = SaveModel(boost_model)
pipeline_xgboost2.save_model() 
