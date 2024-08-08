# 1. Creating a Dictionary
my_dict = {}
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'
print(my_dict)

# 2. Accessing Dictionary Values
def get_value(dictionary, key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print(f"Key '{key}' not found.")

my_dict = {'name': 'John', 'age': 30}
get_value(my_dict, 'name')
get_value(my_dict, 'country')

# 3. Updating Dictionary Values
my_dict = {'name': 'John', 'age': 30}
print("Before update:", my_dict)
my_dict['age'] = 31
print("After update:", my_dict)

# 4. Counting Word Occurrences
def count_words(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

text = "This is a test. This test is only a test."
print(count_words(text))

# 5. Retrieving Dictionary Keys and Values
def get_keys_and_values(dictionary):
    print("Keys:", list(dictionary.keys()))
    print("Values:", list(dictionary.values()))

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
get_keys_and_values(my_dict)

# 6. Dictionary Default Values
def get_value(dictionary, key):
    return dictionary.get(key, 0)

my_dict = {'name': 'John', 'age': 30}
print(get_value(my_dict, 'name'))
print(get_value(my_dict, 'country'))

# 7. Nested Dictionaries
students = {
    'John': {'age': 20, 'grades': {'Math': 90, 'Science': 85}},
    'Jane': {'age': 22, 'grades': {'Math': 95, 'Science': 90}},
    'Bob': {'age': 21, 'grades': {'Math': 80, 'Science': 75}}
}
print(students)

# 8. Merging Dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

dict1 = {'name': 'John', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}
print(merge_dictionaries(dict1, dict2))

# 9. Dictionary Tracebacks
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Key '{key}' not found.")

my_dict = {'name': 'John', 'age': 30}
print(get_value(my_dict, 'name'))
print(get_value(my_dict, 'country'))

# 10. Finding the Most Common Word
def most_common_word(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        max_count = max(word_counts.values())
        most_common_word = [word for word, count in word_counts.items() if count == max_count]
        return most_common_word[0], max_count

# Test the function
file_name = 'example.txt'
print(most_common_word(file_name))