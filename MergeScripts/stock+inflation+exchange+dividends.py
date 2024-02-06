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
merge_final.to_csv("final_merge.csv")