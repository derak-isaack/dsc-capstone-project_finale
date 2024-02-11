import joblib 
import pickle   
import streamlit as st 
from save_model import SaveModel
import os
import pandas as pd 
from model1 import XBoostTuned
import sklearn 

import joblib
model_path = 'stock-increement2.pkl'
model = joblib.load(open(model_path, 'rb'))
economic_indicators = ['Open','Close','High','Average']
def main():   
    
    st.title(" EABL Stock Movement Predictor".upper())
    
    info = ''
    opening_price = st.number_input("Enter Last opening price") 
    closing_price = st.number_input("Enter Last closing price")
    high_price = st.number_input("Enter Last High price")
    average_price = st.number_input("Enter Last Average price")

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
            'Open': [opening_price],
            'Close': [closing_price],
            'High': [high_price], 
            'Average': [average_price]
    })
    for indicator in selected_indicators:
        indicator_value = st.number_input(f"Enter {indicator}")
        input_data[indicator] = indicator_value

    predicted_values = model.predict(input_data)
    
    st.write("Predicted values for all three classes:")
    st.write(predicted_values)
    
    # Display prediction for each class
    for i, target_class in enumerate(['Target', 'Target1', 'Target2', 'Target3']):
        st.write(f"Predicted value for {target_class}: {predicted_values[i]}")
    
    # Check if any of the classes predict an increase
    if 1 in predicted_values:
        st.success("At least one class predicts an increase!")
        st.balloons()
    else:
        st.error("None of the classes predict an increase.")
        st.warning("Better luck next time!")

        
#         if st.button("Predict"):
#             input_data = pd.DataFrame({'Date': [text_image], 'Forecast Time': [text_message]})
#             input_data = pd.DataFrame({
#                 'Date': [text_image], 
#                 'Forecast Time': [text_message],
#                 'Open': [opening_price],
#                 'Close': [closing_price],
#                 'High': [high_price], 
#                 'Average': [average_price]
#     })
#     for indicator in selected_indicators:
#         indicator_value = st.number_input(f"Enter {indicator}")
#         input_data[indicator] = indicator_value

#     predicted_values = model.predict(input_data)
    
#     st.write("Predicted values for all three classes:")
#     st.write(predicted_values)
    
#     # Display prediction for each class
#     for i, target_class in enumerate(['Target', 'Target1', 'Target2', 'Target3']):
#         st.write(f"Predicted value for {target_class}: {predicted_values[i]}")
    
#     # Check if any of the classes predict an increase
#     if 1 in predicted_values:
#         st.success("At least one class predicts an increase!")
#         st.balloons()
#     else:
#         st.error("None of the classes predict an increase.")
#         st.warning("Better luck next time!")

        
#         # if st.button("Predict"):
#         #     input_data = pd.DataFrame({'Date': [text_image], 'Forecast Time': [text_message]})
#         #     input_data = pd.DataFrame({
#         #     'Date': [text_image], 
#         #     'Forecast Time': [text_message],
#         #     'Open': [opening_price],
#         #     'Close': [closing_price],
#         #     'High': [high_price], 
#         #     'Average': [average_price]
#         # })
#         #     for indicator in selected_indicators:
#         #         indicator_value = st.number_input(f"Enter {indicator}")
#         #         input_data[indicator] = indicator_value

#         #     predicted_value = model.predict(input_data)
#         #     if predicted_value == 1:
#         #         st.success("The stock value will increase!")
#         #         st.balloons()
#         #     else:
#         #         st.error("The stock value will not increase.")
#         #         st.warning("Better luck next time!")
            
            
# if __name__ == '__main__':
#     main() 
        
        