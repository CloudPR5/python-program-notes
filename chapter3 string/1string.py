# Initializing strings
first_name = "John"
last_name = "Doe"

# String concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String slicing
first_three_letters = full_name[:3]  # First 3 letters
last_three_letters = full_name[-3:]  # Last 3 letters
print("First 3 letters:", first_three_letters)
print("Last 3 letters:", last_three_letters)

# String methods
uppercase_name = full_name.upper()  # Convert to uppercase
lowercase_name = full_name.lower()  # Convert to lowercase
length_of_name = len(full_name)  # Get length of the string

print("Uppercase Name:", uppercase_name)
print("Lowercase Name:", lowercase_name)
print("Length of Full Name:", length_of_name)

# String replace
replaced_name = full_name.replace("Doe", "Smith")  # Replace 'Doe' with 'Smith'
print("Replaced Full Name:", replaced_name)

# String check
is_john_in_name = "John" in full_name  # Check if 'John' is in the full name
print("Is 'John' in the full name?", is_john_in_name)

# Using f-strings for formatting
greeting = f"Hello, my name is {full_name}."
print(greeting)
