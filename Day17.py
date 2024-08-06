# 1. Creating Lists
def create_list():
    fruits = ['apple', 'banana', 'cherry']
    print(fruits)

# 2. Accessing List Elements
def access_list_elements():
    numbers = [10, 20, 30, 40, 50]
    print(numbers[1])  # second element
    print(numbers[3])  # fourth element

# 3. List Slicing
def slice_list():
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    print(colors[:3])  # first three elements

# 4. Modifying Lists
def modify_list():
    animals = ['cat', 'dog', 'rabbit']
    animals[2] = 'hamster'  # change third element
    print(animals)

# 5. Appending to Lists
def append_to_list():
    zoo = ['lion', 'tiger', 'bear']
    zoo.append('elephant')
    print(zoo)

# 6. Inserting into Lists
def insert_into_list():
    fruits = ['apple', 'banana', 'cherry']
    fruits.insert(1, 'grape')  # insert between 'apple' and 'banana'
    print(fruits)

# 7. Removing from Lists
def remove_from_list():
    fruits = ['apple', 'banana', 'cherry']
    fruits.remove('banana')
    print(fruits)

# 8. List Length
def list_length():
    languages = ['Python', 'Java', 'C++', 'JavaScript']
    print(len(languages))

# 9. List Concatenation
def concatenate_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(list1 + list2)

# 10. List Comprehension
def list_comprehension():
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(squares)

# Run all the functions
create_list()
access_list_elements()
slice_list()
modify_list()
append_to_list()
insert_into_list()
remove_from_list()
list_length()
concatenate_lists()
list_comprehension()