import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [25, 30, 35, 40],
    'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
}


df = pd.DataFrame(data)

# Prints First 5 Rows of Number is Not Specified
print(df.head())

# Prints the First 2 Rows
print(df.head(2))