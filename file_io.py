# file_io.py
# Write to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is line 1!\n")
    file.write("This is line 2.\n")
    file.write("And this is line 3.\n")

print("File written successfully!")

# Read from the file
print("\nReading the entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
print("Reading line by line:")
with open("sample.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")