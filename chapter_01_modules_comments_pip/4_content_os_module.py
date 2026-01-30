import os   # Importing the OS module to interact with the operating system

# Set the path of the directory you want to list
path = "."

# Get the list of all files and folders in the directory
files = os.listdir(path)

# Print the contents of the directory
print("Contents of this directory:")
for file in files:
    print(file)
