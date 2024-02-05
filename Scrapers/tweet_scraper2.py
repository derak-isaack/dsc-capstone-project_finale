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
data = pd.DataFrame(get_tweets("kenya cane until:2013-12-08 since:2006-10-02", "term", 50))

data['date'] = pd.to_datetime(data['date'], format="%b %d, %Y · %I:%M %p %Z")

data.to_csv("Kenya_Cane_sentiments.csv", index=False)