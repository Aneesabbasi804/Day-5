# Python File Handling Examples

# 1. Opening a File
def open_file():
    file = open('data.txt', 'r')
    print("File opened successfully.")

# 2. Reading a File
def read_file():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# 3. Writing to a File
def write_file():
    with open('output.txt', 'w') as file:
        file.write('Hello, World!')
    print("Written to file successfully.")

# 4. File Not Found
def file_not_found():
    with open('data.txt', 'r') as file:
        pass

# 5. Counting Lines
def count_lines():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

# 6. Searching in a File
def search_file():
    with open('log.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'error' in line.lower():
                print(line.strip())

# 7. Copying Files
def copy_file():
    with open('data.txt', 'r') as source:
        with open('data_copy.txt', 'w') as target:
            target.write(source.read())
    print("File copied successfully.")

# 8. Appending to a File
def append_file():
    with open('output.txt', 'a') as file:
        file.write('End of file')
    print("Appended to file successfully.")

# 9. Using Context Manager
def use_context_manager():
    with open('data.txt', 'r') as file:
        contents = file.read()
        print(contents)

# 10. File Properties
def file_properties():
    import os
    file_size = os.path.getsize('data.txt')
    print(f"File size: {file_size} bytes")

# Run all the functions
open_file()
read_file()
write_file()
file_not_found()
count_lines()
search_file()
copy_file()
append_file()
use_context_manager()
file_properties()