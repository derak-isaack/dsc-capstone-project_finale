import pandas as pd 

sentiment_balozi = pd.read_csv('Sentiments/EABL_Balozi_sentiments.csv')
sentiment_guiness =pd.read_csv('Sentiments/EABL_Guinness_sentiments.csv')
sentiment_serengetti = pd.read_csv('Sentiments/EABL_Serengeti_sentiments.csv')
sentiment_tusker = pd.read_csv('Sentiments/tusker_sentiments.csv')
sentiment_pilsner = pd.read_csv('Sentiments/Plisner.csv')

merged_sentiments = pd.concat([sentiment_balozi, 
                               sentiment_guiness, 
                               sentiment_pilsner, 
                               sentiment_serengetti, 
                               sentiment_tusker], 
                               ignore_index=True)
merged_sentiments.to_csv("merged_sentiments.csv", index=False)