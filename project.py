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

#cleaning the data to form a single source of truth

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

#Merge and concatenate data

new_data = {
    'Date': ['2023-10-04', '2023-10-04'],
    'Item': ['Latte', 'Muffin'],
    'Price': [4.50, 4.10],
    'Quantity': [2, 1],
    'Barista': ['Gavan', 'Albie'],
    'Revenue': [9.00, 4.10]
}

#1st convert to new data frame

df_new_day = pd.DataFrame (new_data)

#convert date to date.time (Clean new data)

df_new_day['Date'] = pd.to_datetime(df_new_day['Date'])

df_new_day.set_index('Date',inplace=True)

print ("New Data: ")

print (df_new_day)
#Concatenating df_new_day with orignial date - you must state if it is vertucal or horizontal concat. axis = 0 is new row)

full_history = pd.concat([df,df_new_day], axis=0)
                         
print ("Full data")

print (full_history)

print ('========Merging Cost data===============')

#create new data frame df_costs
# 1. Create the cost data frame
cost_data = {
    'Item': ['Latte', 'Espresso', 'Muffin', 'Cappuccino'],
    'Cost': [1.50, 0.80, 1.00, 1.20]
}
df_costs = pd.DataFrame(cost_data)

# 2. Reset the index of full_history
# This moves 'Date' from the index back into a normal column
full_history_reset = full_history.reset_index()

# 3. Clean the 'Item' column strings
# We use .str.strip() to remove any accidental leading/trailing spaces
full_history_reset['Item'] = full_history_reset['Item'].str.strip()
df_costs['Item'] = df_costs['Item'].str.strip()

# 4. Merge the two DataFrames
# This joins the cost information to every transaction based on the 'Item' name
df_with_costs = pd.merge(full_history_reset, df_costs, on='Item', how='left')

print('Data Frame With costs after merging costs:')
print(df_with_costs)

# 5. Final Lambda Categorization on the merged data
df_with_costs['Category'] = df_with_costs['Revenue'].apply(lambda x: 'High' if x > 10 else 'Std')

print('\nFinal Categorized Data:')
print(df_with_costs[['Date', 'Item', 'Barista', 'Revenue', 'Cost', 'Category']])