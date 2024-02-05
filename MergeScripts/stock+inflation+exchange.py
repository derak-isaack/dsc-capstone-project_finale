import pandas as pd   

df_exchange = pd.read_csv('Data\Exchange-rates-CBK.csv')
df_stock_inflation = pd.read_csv('MergedData\Stock&inflation.csv')

# Convert the date column to datetime format using the day-month-year.
df_exchange['Date'] = pd.to_datetime(df_exchange['Date'], format='%d/%m/%Y')

# Merge the mean exchange rates on the previous merge.
df_merge2 = pd.merge(df_stock_inflation, df_exchange[['Date','Mean']], on=['Date'], how='left')
df_merge2.to_csv("Stocks,Inflation&ExchangeRates.csv")