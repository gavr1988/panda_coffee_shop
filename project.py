import numpy as np
import pandas as pd

data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 102], 
    'Date': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03', '2023-10-03', '2023-10-01'],
    'Item': ['Latte', 'Espresso', 'Latte', 'Muffin', 'Cappuccino', 'Latte', 'Espresso'],
    'Price': [4.50, 3.00, 4.50, np.nan, 4.00, 4.50, 3.00],
    'Qty': [1, 2, 1, 5, 2, 1, 2],
    'Barista': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob']
}

df = pd.DataFrame(data)
print(df)

print ("information about data frame") #getting a technical summary of the data frame
print (df.info())

#cleaning the data to form a single source of tru

#this will replace the NaN values in price

print ('removing the NaN values')

avg_price= df['Price'].mean()
df['Price'].fillna(value=avg_price, inplace=True)

print (df)

#renaming the columns

print ('renaming the Qty column to Quantity')

df.rename(columns={'Qty':'Quantity'}, inplace = True)

df['Date'] = pd.to_datetime(df['Date'])
 
df['Revenue'] = df['Price'] * df['Quantity']

print ('Data frame after transformations')

print (df)

df.set_index('Date', inplace = True)

print ('finding the sales on October 1,2023')

print (df.loc['2023-10-01'])

print ('Finding the Highest value Orders')

print (df.query('Revenue >= 10'))

print ('finding the lowest value Orders')

print (df.query ('Revenue <=5'))

#topic13 and 14

#Using the group by function

print("Barista performance")

# select multiple columns with a list of column names, not a tuple
barista_performance = df.groupby('Barista')[["Revenue", "Quantity"]].sum()

print(barista_performance)

#specific sales data for individual items in a pivot table

print ('Sales Matrix (Item vs Barista):')

sales_matrix = df.pivot_table (index = 'Item', columns = 'Barista', values = 'Revenue', aggfunc = 'sum', fill_value = 0)

print (sales_matrix)

print ("\n")

#resampling to Daily Totals

print ("resampling to daily totals")

daily_revenue = df['Revenue'].resample('D').sum()
print("Daily Revenue:")
print (daily_revenue)

#getting a two day average

print ("2 day average")

print (daily_revenue.rolling (window = 2).mean())

print ('Day over Day Growth')

growth = daily_revenue - daily_revenue.shift(1)

print (growth)

#using lambda function

print (df)

print ('adding category column')

df['Category'] = df['Revenue'].apply(lambda x: 'High' if x> 10 else 'Std')

print (df)