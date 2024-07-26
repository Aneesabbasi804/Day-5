# Concatenation and Conversion
def concat_and_convert(str1, str2):
    result = str1 + str2
    if result.isdigit():
        return int(result)
    else:
        return result

# String Indexing
def get_char_at_index(s, index):
   
    if index < 0 or index >= len(s):
        return "Index out of bounds"
    else:
        return s[index]

# String Length
def get_string_lengths(strings):
      return [len(s) for s in strings]

# Looping Through Strings
def print_chars_with_index(s):
       for index, char in enumerate(s):
        print(f"Index {index}: {char}")

# Character Counting
def count_char_occurrences(s, char):
     return s.count(char)

# String Slicing
def get_substring(s, start, end):
    if start < 0:
        start = 0
    if end > len(s):
        end = len(s)
    return s[start:end]

# String Comparison
def compare_strings(str1, str2):
    if str1 < str2:
        return "The first string comes before the second string."
    elif str1 > str2:
        return "The first string comes after the second string."
    else:
        return "Both strings are equal."

# String Methods
def transform_string(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }

# Search and Replace
def search_and_replace(s, search, replace):
    return s.replace(search, replace)

# Whitespace Removal
def remove_whitespace(s):
    s = s.strip()
    return ' '.join(s.split())
