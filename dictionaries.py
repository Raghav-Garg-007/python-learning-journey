# dictionaries.py
# Create a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Math", "Physics", "Chemistry"],
    "gpa": 3.8
}

# Access dictionary values
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Courses:", student["courses"])

# Add new key-value pair
student["email"] = "john.doe@email.com"
print("After adding email:", student)

# Update existing value
student["age"] = 21
print("After updating age:", student)

# Loop through dictionary
print("\nAll student information:")
for key, value in student.items():
    print(f"{key}: {value}")