import pandas as pd

# Reading a CSV File
df = pd.read_csv("data.csv")
print(df.head())

# Writing to a CSV File
df.to_csv('output.csv', index = False)

# Writing to a JSON File
df.to_json('output.json', index = False)

# Writing to a HTML File
df.to_html('output.html', index = False)