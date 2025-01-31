import os

# Get Current Working Directory
cwd = os.getcwd()
print("Current Working Directory : ", cwd)

# Create New Directory
os.mkdir("New Folder")

# Renaming a Directory
os.rename("New Folder", "Hello")

# Lisiting Files in Current Working Directory
print("Files in Current Directory are : ", os.listdir(cwd))