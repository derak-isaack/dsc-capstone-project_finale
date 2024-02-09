import joblib 
import pickle 
import os    
import streamlit as st 
from save_model import SaveModel
import os

import joblib
model = joblib.load('stock-high-low.pkl')

def main():   
    
    st.title("Stock Predictor".upper())
    
    info = ''
    
    with st.expander("Check whether a stock will increase or not"):
        text_image = st.date_input("Input the date")
        text_message = st.date_input("Input forecast time")
        
        if st.button("Predict"):
            input_data = pd.DataFrame({'Date': [text_image], 'Forecast Time': [text_message]})
            predicted_value = model.predict(input_data)
            if predicted_value == 1:
                st.success("The stock value will increase!")
                st.balloons()
            else:
                st.error("The stock value will not increase.")
                st.warning("Better luck next time!")
            
            
if __name__ == '__main__':
    main() 
        
        