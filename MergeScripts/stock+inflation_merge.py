import pandas as pd  

data = pd.read_csv('Data\EABL-2006-2024_JAN_STOCKS.csv')

data_new = data.copy()

# Convert the 'Date' column to a datetime object.
data_new['Date'] = pd.to_datetime(data_new['Date'])
data_new['Volume'] = data_new['Volume'].astype(int)

# Extract the month, year, and day from the 'Date' column.
data_new['Month'] = data_new['Date'].dt.month
data_new['Year'] = data_new['Date'].dt.year 
data_new['Day'] = data_new['Date'].dt.day 

# Read the inflation rates from a CSV file and convert the 'Month' column to an integer.
df_inflation = pd.read_csv('Data\Inflation Rates.csv')
df_inflation['Month'].astype(str)

# Apply a mapper for the month column.
months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
df_inflation['Month'] = df_inflation['Month'].map(months)

#Merge the two dataframes using the 'Month' and 'Year' columns to have an inflation rate for each column.
df_merge = pd.merge(data_new,df_inflation, on=['Month','Year'], how='left')

#Save the merged dataframe to a CSV file.
df_merge.to_csv("Stock&inflation.csv")