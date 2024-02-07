import pandas as pd  
import re   

df_dividend = pd.read_csv("Data\Dividends-Payout.csv")
df_stock_inflation = pd.read_csv("MergedData\Stocks,Inflation&ExchangeRates.csv")

# Convert columns under interest from object formarts. 
df_dividend['Announced'] = pd.to_datetime(df_dividend['Announced'])

#Regex function toextract the numbers from the amount in dividends.
def extract_numeric(value):
        if isinstance(value, str):
            match = re.search(r'\d+\.\d+', value)
            if match:
                return float(match.group())
        return value

# Apply the function to extract the numerics for the dividends payout.
df_dividend['Amount'] = df_dividend['Amount'].apply(extract_numeric)

#Rename the column for an easier merge. 
df_dividend.rename(columns={"Announced":"Date"}, inplace=True)

#Perform the merge.
merge_final = pd.merge(df_stock_inflation, df_dividend[['Date','Amount']], on=['Date'], how='left')
df_merge1 = pd.read_csv("Data/Kenya_GDP.csv")

df_merge1['Year'] = df_merge1['Year'].astype('int64')

merge_final2 = pd.merge(merge_final, df_merge1[['Year','Annual GDP growth (%)']],on=['Year'], how='left')
merge_final2.to_csv("final_merge2.csv")