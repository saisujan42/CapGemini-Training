import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [25, 30, 35, 40],
    'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Selecting a Column
print(df['Name'])

# Selecting Multiple Columns
print(df[['Name', 'Age']])