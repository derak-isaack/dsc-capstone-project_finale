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
            predicted_values = (predicted_probabilities >= threshold).astype(int)
            
            class_targets = {
            'Target': 'Close Price',
            'Target1': 'High Price',
            'Target2': 'Open Price',  # Adjust as per your actual class names
            'Target3': 'Low Price'  # Adjust as per your actual class names
        }

    # Create a dictionary to store predictions
            class_predictions = {}

    # Display predictions for all classe

            # Display predictions
            st.write("Predicted values for all three classes:")
            st.write(predicted_values)

            # Display prediction for each class
            # for i, target_class in enumerate(['Target', 'Target1', 'Target2', 'Target3']):
            #     class_predictions[target_class] = predicted_values[i]
            #     # st.write(f"Predicted value for {target_class}: {predicted_values[i]}")
            #     st.write(f"Predicted value for {class_targets[target_class]}: {predicted_values[i]}")
            for i, (target_class, target_value) in enumerate(class_targets.items()):
                # Access the corresponding predicted value using the class name
                predicted_value = predicted_values[i]
                # Store the prediction
                class_predictions[target_class] = predicted_value
                # Display the prediction
                st.write(f"Predicted value for {target_value}: {predicted_value}")

            # Check if any of the classes predict an increase
            if 1 in predicted_values:
                st.success("At least one class predicts an increase!")
                st.balloons()
            else:
                st.error("None of the classes predict an increase.")
                st.warning("Better luck next time!")
                
            print(class_predictions)

if __name__ == '__main__':
    main()
            
        

                
            # predicted_probabilities = model.predict_proba(input_data)
                
            # targets_labels_mapping = {'Target': 'Close', 'Target1': 'High', 'Target2': 'Open', 'Target3': 'Low'}

            #     # Create a DataFrame to display predicted probabilities with labels
            # probabilities_df = pd.DataFrame(predicted_probabilities, columns=['Probability'])
            # probabilities_df['Label'] = [targets_labels_mapping[target_class] for target_class in model.classes_]

            #     # Display the predicted probabilities table
            # st.write("Predicted probabilities for each target class:")
            # st.write(probabilities_df)

            #     # Check if any of the classes predict an increase
            # if (predicted_probabilities > 0.8).any():
            #     predicted_classes_increasing = probabilities_df[probabilities_df['Probability'] > 0.8]['Label']
            #     st.success(f"At least one of the following classes predicts an increase: {', '.join(predicted_classes_increasing)}")
            #     st.balloons()
            # else:
            #     st.error("None of the classes predict an increase.")
            #     st.warning("Better luck next time!")
                
                
                # predicted_probabilities = model.predict_proba(input_data)

                # # Convert probabilities to binary formart using a threshold
                # threshold = 0.8
                # predicted_values = (predicted_probabilities >= threshold).astype(int)

                #  # Display predictions
                # st.write("Predicted values for all three classes:")
                # st.write(predicted_values)

                #     # Display prediction for each class
                # # Assuming predicted_values is a list of predicted outputs corresponding to ['Target', 'Target1', 'Target2', 'Target3']
                # targets_labels_mapping = {'Target': 'Close', 'Target1': 'High', 'Target2': 'Open', 'Target3': 'Low'}

                #     # Iterate through each target class and display the predicted value with the corresponding label
                # # Iterate over each row in the DataFrame
                # for index, row in predicted_values.iterrows():
                #     # Iterate over each target class and display the predicted value with the corresponding label
                #     for target_class, predicted_value in zip(['Target', 'Target1', 'Target2', 'Target3'], row):
                #         predicted_label = targets_labels_mapping[target_class]
                #         st.write(f"Predicted value for {predicted_label}: {predicted_value}")

                # # Check if any of the classes predict an increase in any of the targets
                # if predicted_values.eq(1).any().any():
                #     # Get the labels of classes predicting an increase
                #     predicted_classes_increasing = [targets_labels_mapping[target_class] for target_class, predicted_value in zip(['Target', 'Target1', 'Target2', 'Target3'], row) if predicted_value == 1]
                #     st.success(f"At least one of the following classes predicts an increase: {', '.join(predicted_classes_increasing)}")
                #     st.balloons()
                # else:
                #     st.error("None of the classes predict an increase.")
                #     st.warning("Better luck next time!")

                # for i, target_class in enumerate(['Target', 'Target1', 'Target2', 'Target3']):
                #     st.write(f"Predicted value for {target_class}: {predicted_values[i]}")

                #     # Check if any of the classes predict an increase
                #     if 1 in predicted_values:
                #         st.success("At least one class predicts an increase!")
                #         st.balloons()
                #     else:
                #         st.error("None of the classes predict an increase.")
                #         st.warning("Better luck next time!")

# if __name__ == '__main__':
#     main()

        
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
        
        