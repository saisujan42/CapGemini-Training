import pandas as pd

data = {
    'Region' : ['North', 'North', 'South', 'South', 'East', 'East'],
    'State' : ['Punjab', 'Delhi', 'Tamil Nadu', 'Karnataka', 'Telangana', 'Odisha'],
    'Year' : [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales' : [75000, 82000, 69000, 72000, 67000, 71000],
    'Profit' : [95000, 10200, 85000, 91000, 77000, 88000]
}

df = pd.DataFrame(data)
df.set_index(['Region', 'State', 'Year'], inplace = True)
print(df)

print(df.loc[('South', 'Tamil Nadu', 2021), 'Sales'])