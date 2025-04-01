# Function to split the number into two halves
def split_number(number):
    # Convert the number to a string to easily find its length
    num_str = str(number)
    length = len(num_str)
    
    # Find the middle point
    mid = length // 2
    
    # Get the first half and second half
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    
    return first_half, second_half

# Taking input from the user
user_number = input("Enter a number: ")

# Ensure the input is valid (non-empty string of digits)
if user_number.isdigit():
    first_half, second_half = split_number(user_number)
    print(f"First half: {first_half}")
    print(f"Second half: {second_half}")
else:
    print("Invalid input! Please enter a valid number.")
