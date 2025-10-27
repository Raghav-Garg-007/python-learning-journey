# lists.py
# Create a list
fruits = ["apple", "banana", "orange", "grape"]

# List operations
print("Original list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add to list
fruits.append("mango")
print("After append:", fruits)

# Remove from list
fruits.remove("banana")
print("After remove:", fruits)

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("Squared numbers:", squared)