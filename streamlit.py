import joblib 
import pickle   
import streamlit as st 
from save_model import SaveModel
import os
import pandas as pd 
from model1 import XBoostTuned
import sklearn 

import joblib
model_path = 'stock-increement3.pkl'
model = joblib.load(open(model_path, 'rb'))
stock_indicators = ['Open','Close','High','Low']
def main():   
    
    st.title(" EABL Stock Movement Predictor".upper())
    
    st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #ffd700, #ffd700 50%, #ffffff 50%, #ffffff); /* Golden to White gradient */
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
    info = ''
    
    selected_indicators = st.multiselect("Select economic indicators", stock_indicators)
    
    with st.expander("Check whether a stock will increase or not"):
        # text_image = st.date_input("Input the date")
        # text_message = st.date_input("Input forecast time")
        opening_price = st.number_input("Enter Last opening price") 
        closing_price = st.number_input("Enter Last closing price")
        high_price = st.number_input("Enter Last High price")
        low_price = st.number_input("Enter Last Low price")
        average_price = st.number_input("Enter Last Average price")
        
        
        dividends_per_share = 5.5
        earnings_per_share = 10
        unemployment_rates = 3.7
        exchange_rates = 167
        interest_rates = 13
        dividends_announced = 1
        inflation = 6.9
        tommorow = 103
        tommorow1 = 104
        tommorow2 = 105
        tommorow3 = 101
        volumes = 100000
        days = 3
        
        if st.button("Predict"):
            input_data = pd.DataFrame({
            'Open': [opening_price],
            'Close': [closing_price],
            'High': [high_price], 
            'Low': [low_price],
            'Average': [average_price],
            'Dividends per share': [dividends_per_share],
            'Earnings per share': [earnings_per_share],
            'Unemployment': [unemployment_rates],
            'Mean': [exchange_rates],
            'Interest rates': [interest_rates],
            'Amount': [dividends_announced],
            '12-Month Inflation': [inflation],
            'Tomorrow': [tommorow],
            'Tomorrow1': [tommorow1],
            'Tomorrow2': [tommorow2],
            'Tomorrow3': [tommorow3],
            'Volume': [volumes],
            'Day': [days]
    })
            
            
            predicted_probabilities = model.predict_proba(input_data)

            # Convert probabilities to binary predictions using a threshold
            threshold = 0.8
            predicted_values = (predicted_probabilities >= threshold).astype(int)
            
            predicted_names = ['Close', 'High', 'Open', 'Low']
            
            if 1 in predicted_values:
                st.success("At least one class predicts an increase!")
                st.balloons()
                
                # Create DataFrame with class names and reshaped predicted values
                df_class_predictions = pd.DataFrame({'Class': predicted_names, 'Predicted': predicted_values.reshape(-1)})

                # Display the DataFrame
                st.write(df_class_predictions)
            else:
                st.error("None of the classes predict an increase.")
                st.warning("Better luck next time!")

                 

if __name__ == '__main__':
    main()
            
                
                