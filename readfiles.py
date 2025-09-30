# Read entire file
with open("sample.txt", "r") as f:
    print("Full content:\n", f.read())

# Read first 10 characters
with open("sample.txt", "r") as f:
    print("\nFirst 10 chars:", f.read(10))

# Read line by line
with open("sample.txt", "r") as f:
    print("\nReading line by line:")
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("\nAs list:", lines)
