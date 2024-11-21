# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Read from an existing file and write modified content to a new file
def read_and_write_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: converting to uppercase)
        modified_content = content.upper()
        
        # Open the output file for writing
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"Content has been successfully written to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify input and output files
input_file = "input.txt"   # Ensure this file exists or create it
output_file = "output.txt"

# Call the function
read_and_write_file(input_file, output_file)


# Question 2
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
def read_file_with_error_handling():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename: ")
        
        # Try to open the file for reading
        with open(filename, "r") as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the file name and try again.")
    except PermissionError:
        print(f"Error: You don't have the necessary permissions to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file_with_error_handling()
