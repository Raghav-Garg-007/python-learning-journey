# functions.py
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate area of rectangle"""
    return length * width

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0

# Test the functions
print(greet("Alice"))
print(f"Area: {calculate_area(5, 3)}")
print(f"Is 4 even? {is_even(4)}")