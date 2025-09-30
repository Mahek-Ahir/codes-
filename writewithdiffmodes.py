# "w" → write (overwrites file)
# "a" → append
# "x" → create (error if file exists)

# Overwrite
with open("data.txt", "w") as f:
    f.write("This overwrites the file.\n")

# Append
with open("data.txt", "a") as f:
    f.write("This is appended.\n")

# Create new file (error if already exists)
try:
    with open("newfile.txt", "x") as f:
        f.write("This file is created new.\n")
except FileExistsError:
    print("newfile.txt already exists.")
