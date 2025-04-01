''' write a python program to print the contents of a directory using the os module search online
  for the function which does that '''

import os

def print_directory_contents(directory):
    # Check if the directory exists
    if not os.path.exists(directory): 
        print(f"Directory '{directory}' does not exist.") 
        return
    
    # List all files and directories in the specified directory
    print(f"Contents of directory '{directory}':")
    for item in os.listdir(directory):
        print(item)

# Example usage:
directory_path = '/path/to/your/directory'  # Replace with your directory path
print_directory_contents(directory_path)  
