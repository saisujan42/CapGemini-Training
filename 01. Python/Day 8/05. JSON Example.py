import json

# Convert a Python Dictionary to a JSON String
data = {"name" : "John", "age" : 30, "city" : "New York"}
json_data = json.dumps(data)
print("JSON Data : ", json_data)