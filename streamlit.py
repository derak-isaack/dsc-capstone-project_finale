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
    
    info = ''
    # opening_price = st.number_input("Enter Last opening price") 
    # closing_price = st.number_input("Enter Last closing price")
    # high_price = st.number_input("Enter Last High price")
    # average_price = st.number_input("Enter Last Average price")

    # Dropdowns for selecting economic indicators
    selected_indicators = st.multiselect("Select economic indicators", stock_indicators)
    
    with st.expander("Check whether a stock will increase or not"):
        # text_image = st.date_input("Input the date")
        # text_message = st.date_input("Input forecast time")
        opening_price = st.number_input("Enter Last opening price") 
        closing_price = st.number_input("Enter Last closing price")
        high_price = st.number_input("Enter Last High price")
        average_price = st.number_input("Enter Last Average price")
        
        
        dividends_per_share = 5.5
        earnings_per_share = 10
        unemployment_rates = 3.7
        exchange_rates = 167
        interest_rates = 12.5
        dividends_announced = 1
        low_price = 104
        inflation = 6.9
        tommorow = 103
        tommorow1 = 104
        tommorow2 = 105
        tommorow3 = 101
        volumes = 100000
        days = 3
        
        if st.button("Predict"):
            # input_data = pd.DataFrame({'Date': [text_image], 'Forecast Time': [text_message]})
            input_data = pd.DataFrame({
            # 'Date': [text_image], 
            # 'Forecast Time': [text_message],
            'Open': [opening_price],
            'Close': [closing_price],
            'High': [high_price], 
            'Average': [average_price],
            'Dividends per share': [dividends_per_share],
            'Earnings per share': [earnings_per_share],
            'Unemployment': [unemployment_rates],
            'Mean': [exchange_rates],
            'Interest rates': [interest_rates],
            'Amount': [dividends_announced],
            'Low': [low_price],
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
            predicted_values = ['Increase' if prob >= threshold else 'Not Increase' for prob in predicted_probabilities]
            


    # Display predictions for all classe

            # Display predictions
            st.write("Movement for Close, High, Open and Low stock prices:")
            st.write(predicted_values)

            df_predicted_values = pd.DataFrame(predicted_values, columns=['Predicted Movement'])
            
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
            st.write("Predicted movement for Close, High, Open and Low stock prices:")
            st.write(df_predicted_values) 


            # Check if any of the classes predict an increase
            if 1 in predicted_values:
                st.success("At least one Price predicts a postive movement!")
                st.balloons()
            else:
                st.error("None of the classes predict an increase.")
                st.warning("Better luck next time!")
                 

if __name__ == '__main__':
    main()
            
        

            