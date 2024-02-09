import joblib 
import pickle   
import streamlit as st 
from save_model import SaveModel
import os
import pandas as pd 
from model1.py import XGBOOST
import sklearn 

import joblib
model_path = 'stock-high-low.pkl'
model = joblib.load(open(model_path, 'rb'))

def main():   
    
    st.title("Stock Predictor".upper())
    
    info = ''
    
    with st.expander("Check whether a stock will increase or not"):
        text_image = st.date_input("Input the date")
        text_message = st.date_input("Input forecast time")
        
        if st.button("Predict"):
            input_data = pd.DataFrame({'Date': [text_image], 'Forecast Time': [text_message]})
            predicted_value = model.predict_proba(input_data)
            if predicted_value > 0.5:
                st.success("The stock value will increase!")
                st.balloons()
            else:
                st.error("The stock value will not increase.")
                st.warning("Better luck next time!")
            
            
if __name__ == '__main__':
    main() 
        
        