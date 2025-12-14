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




