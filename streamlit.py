import joblib 
import pickle   
import streamlit as st 
from save_model import SaveModel
import os
import pandas as pd 
from model1 import XBoostTuned
import sklearn 

import joblib
model_path = 'stock-high-low3.pkl'
model = joblib.load(open(model_path, 'rb'))
economic_indicators = ['Inflation Rate', 'Exchange Rate', 'Unemployment Rate']
def main():   
    
    st.title(" EABL Stock Movement Predictor".upper())
    
    info = ''
    dividends_payout = st.number_input("Enter dividends payout")
    earnings_per_share = st.number_input("Enter earnings per share")

    # Dropdowns for selecting economic indicators
    selected_indicators = st.multiselect("Select economic indicators", economic_indicators)
    
    with st.expander("Check whether a stock will increase or not"):
        text_image = st.date_input("Input the date")
        text_message = st.date_input("Input forecast time")
        
        if st.button("Predict"):
            input_data = pd.DataFrame({'Date': [text_image], 'Forecast Time': [text_message]})
            input_data = pd.DataFrame({
            'Date': [text_image], 
            'Forecast Time': [text_message],
            'Dividends Payout': [dividends_payout],
            'Earnings Per Share': [earnings_per_share]
        })
            for indicator in selected_indicators:
                indicator_value = st.number_input(f"Enter {indicator}")
                input_data[indicator] = indicator_value

            predicted_value = model.predict(input_data)
            if predicted_value == 1:
                st.success("The stock value will increase!")
                st.balloons()
            else:
                st.error("The stock value will not increase.")
                st.warning("Better luck next time!")
            
            
if __name__ == '__main__':
    main() 
        
        