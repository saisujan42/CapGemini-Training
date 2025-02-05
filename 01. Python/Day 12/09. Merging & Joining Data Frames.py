import pandas as pd

data = {
    'Region' : ['North', 'North', 'South', 'South', 'East', 'East'],
    'State' : ['Punjab', 'Delhi', 'Tamil Nadu', 'Karnataka', 'Telangana', 'Odisha'],
    'Year' : [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales' : [75000, 82000, 69000, 72000, 67000, 71000],
    'Profit' : [95000, 10200, 85000, 91000, 77000, 88000]
}

df = pd.DataFrame(data)

df_sales = pd.DataFrame({'State' : ['Delhi', 'Tamil Nadu', 'Telangana'], 'Sales' : [157000, 141000, 138000]})
df_profit = pd.DataFrame({'State' : ['Delhi', 'Tamil Nadu', 'Telangana'], 'Profit' : [185000, 165000, 155000]})
df_merged = pd.merge(df_sales, df_profit, on = 'State', how = 'inner')
print(df_merged)