import os

filename = "example.txt"

# Check if file exists
if os.path.exists(filename):
    print(f"{filename} exists.")

    # Rename the file
    os.rename(filename, "new_example.txt")
    print("File renamed to new_example.txt")

    # Delete the file
    os.remove("new_example.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")
