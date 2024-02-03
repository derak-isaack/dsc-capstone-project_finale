import pandas as pd   
from ntscraper import Nitter

scraper = Nitter()

def get_tweets(name, modes, no):
    tweets = scraper.get_tweets(name, mode=modes, number=no)
    final_tweets = []
    for tweet in tweets['tweets']:
        data = [tweet['text'],tweet['date'], tweet['stats']['likes'], tweet['stats']['comments']]
        final_tweets.append(data)
    data= pd.DataFrame(final_tweets, columns=['text','date','No_of_likes','No_of_tweets'])
    return data 

#Scrape EABL Tusker sentiments and store them in  a DataFrame.
data = pd.DataFrame(get_tweets("eabl white cap until:2024-01-21 since:2006-08-01", "term", 80))

data['date'] = pd.to_datetime(data['date'], format="%b %d, %Y · %I:%M %p %Z")

data.to_csv("EABL_WhiteCap_sentiments.csv", index=False)