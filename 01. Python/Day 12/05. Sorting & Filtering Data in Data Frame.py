import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [25, 30, 35, 40],
    'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Filtering Rows where Age > 30
print(df[df['Age'] > 30])

# Sorting Data in Descending Order
df_dsc = df.sort_values(by = 'Age', ascending=False)
print(df_dsc)

# Sorting Data in Ascending Order
df_asc = df.sort_values(by = 'Age', ascending=True)
print(df_asc)
