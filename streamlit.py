import joblib 
import pickle 
import os    
import streamlit as st 

import os

script_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_directory, 'stock-high-low.pkl')
model = joblib.load(open(model_path, 'rb'))



def main():   
    
    st.title("Stock Predictor".upper())
    
    info = ''
    
    with st.expander("Check whether a stock will increase or not"):
        text_image = st.date_input("Input the date")
        text_message = st.date_input("Input forecast time")
        
        if st.button("Predict"):
            info = model.predict([[text_image, text_message]])
            predicted_value = info.iloc[0]['y'] 
            st.success(f"The stock value will increase! {predicted_value}")
            st.balloons() 
            
            
if __name__ == '__main__':
    main() 
        
        