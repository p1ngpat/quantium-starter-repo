import pandas as pd

df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

#combine into one dataframe
df = pd.concat([df1, df2, df3], ignore_index=True)

#filter Pink Morsals
df = df[df['product'] == 'pink morsel']

#type conversion
df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)
df["quantity"] = df["quantity"].astype(int)

#create sales column
df['sales'] = df['quantity'] * df['price']

#required columns
df = df[['sales','date', 'region']]


df.to_csv("output.csv", index=False)

print("Data Processed as output.csv")

