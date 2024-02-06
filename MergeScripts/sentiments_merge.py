import pandas as pd 

sentiment_balozi = pd.read_csv('Sentiments/EABL_Balozi_sentiments.csv')
sentiment_guiness =pd.read_csv('Sentiments/EABL_Guinness_sentiments.csv')
sentiment_serengetti = pd.read_csv('Sentiments/EABL_Serengeti_sentiments.csv')
sentiment_tusker = pd.read_csv('Sentiments/tusker_sentiments.csv')
sentiment_pilsner = pd.read_csv('Sentiments/Plisner.csv')
sentiment_chrome = pd.read_csv('Sentiments/Chrome_sentiments.csv')
sentiment_EABL2015 = pd.read_csv('Sentiments/Eabl2015_sentiments.csv')
sentiment_EABL2023 = pd.read_csv('Sentiments/Eabl2023_sentiments.csv')
sentiment_EABLfoundation = pd.read_csv('Sentiments/Eablfoundation_sentiments.csv')
sentiment_KenyaCane = pd.read_csv('Sentiments/Kenya_Cane_sentiments.csv')
sentiment_smirnoff = pd.read_csv('Sentiments/Smirnoff_sentiments.csv')
sentiment_TuskerLite = pd.read_csv('Sentiments/Tusker_Lite_sentiments.csv')
sentiment_TPF = pd.read_csv('Sentiments/TuskerProjectFame_sentiments.csv')
sentiment_waragi = pd.read_csv('Sentiments/Waragi_sentiments.csv')

merged_sentiments = pd.concat([sentiment_balozi, 
                               sentiment_guiness, 
                               sentiment_pilsner, 
                               sentiment_serengetti, 
                               sentiment_tusker,
                               sentiment_chrome,
                               sentiment_EABL2015,
                               sentiment_EABL2023,
                               sentiment_EABLfoundation,
                               sentiment_KenyaCane,
                               sentiment_smirnoff,
                               sentiment_TuskerLite,
                               sentiment_TPF,
                               sentiment_waragi], ignore_index=True)
merged_sentiments.to_csv("merged_sentiments.csv", index=False)