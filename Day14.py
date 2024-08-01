#1. Complex Number Conversion and Operations

def complex_operations(complex_str, complex_num):
    # Convert the string to a complex number
    complex_number = complex(complex_str)
    
    # Perform operations
    addition = complex_number + complex_num
    subtraction = complex_number - complex_num
    multiplication = complex_number * complex_num
    division = complex_number / complex_num
    
    # Return the results as a tuple
    return addition, subtraction, multiplication, division

# Example usage
result = complex_operations("3+4j", 2-3j)
print(result)

#2. Binary String to Integer and Back

def binary_conversion(binary_str, length):
    # Convert binary string to integer
    integer_value = int(binary_str, 2)
    
    # Convert integer back to binary string with fixed length
    binary_result = format(integer_value, f'0{length}b')
    
    return binary_result

# Example usage
binary_result = binary_conversion("1011", 8)
print(binary_result)

#3. Dictionary to JSON String and Back with Error Handling

import json

def dict_to_json(dict_input):
   
    json_str = json.dumps(dict_input)
    if json_str is None:
        error_msg = "Failed to convert dictionary to JSON string"
        print(f"Error: {error_msg}")
        return dict_input, error_msg
    
    dict_output = json.loads(json_str)
    if dict_output is None:
        error_msg = "Failed to convert JSON string back to dictionary"
        print(f"Error: {error_msg}")
        return dict_input, error_msg
    
    return dict_output

#4. Matrix Addition with Type and Dimension Enforcement

class MatrixDimensionError(Exception):
    pass

def matrix_addition(matrix1, matrix2):
    if not all(isinstance(row, list) for row in matrix1) or not all(isinstance(row, list) for row in matrix2):
        raise TypeError("Both inputs must be matrices (lists of lists).")
    
    if len(matrix1) != len(matrix2) or not all(len(row1) == len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise MatrixDimensionError("Matrices must have the same dimensions.")
    
    result = [[cell1 + cell2 for cell1, cell2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
    
    return result

# Example usage
result = matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print(result)

#5. Prime Factorization with Cumulative Multiplication

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    cumulative_product = 1
    for factor in factors:
        cumulative_product *= factor
    return factors, cumulative_product

# Example usage
result = prime_factors(56)
print(result)

#6. Formatted String Interpolation with Custom Placeholders

def custom_interpolation(template, values):
    for key, value in values.items():
        template = template.replace(f'{{{key}}}', str(value))
    return template

# Example usage
result = custom_interpolation("Hello, {name}! You are {age} years old.", {"name": "Alice", "age": 30})
print(result)

#7. Advanced Anagram Check with Frequency Analysis

from collections import Counter
import re

def advanced_anagram_check(str1, str2):
    # Clean strings: remove non-alphanumeric characters and make lowercase
    clean_str1 = re.sub(r'[^a-zA-Z0-9]', '', str1).lower()
    clean_str2 = re.sub(r'[^a-zA-Z0-9]', '', str2).lower()
    
    # Frequency analysis
    freq1 = Counter(clean_str1)
    freq2 = Counter(clean_str2)
    
    # Check if anagrams
    are_anagrams = freq1 == freq2
    
    return are_anagrams, {"str1_freq": freq1, "str2_freq": freq2}

# Example usage
result = advanced_anagram_check("Listen", "Silent")
print(result)

#8. Nested Data Structure Flattening with Type Preservation

def flatten_list(nested_list, depth=0):
    flattened = []
    current_depth = depth
    
    for item in nested_list:
        if isinstance(item, list):
            flat, new_depth = flatten_list(item, depth + 1)
            flattened.extend(flat)
            current_depth = max(current_depth, new_depth)
        else:
            flattened.append(item)
    
    return flattened, current_depth

# Example usage
result, depth = flatten_list([1, [2, [3, 4], 5], 6])
print(result, depth)

#9. String and Number Pattern Matching

import re

def pattern_matching(string, pattern):
    # Create regex pattern
    regex_pattern = ''.join([r'[a-zA-Z]' if char.isalpha() else r'\d' for char in pattern])
    
    # Match the pattern
    match = re.fullmatch(regex_pattern, string)
    
    return bool(match)

# Example usage
result = pattern_matching("a1b2", "a1b2")
print(result)

#10. Data Normalization and Statistical Analysis

import statistics

def normalize_and_analyze(data):
    if not all(isinstance(num, (int, float)) for num in data) or not data:
        raise ValueError("Input list must contain only numeric values and cannot be empty.")
    
    min_val, max_val = min(data), max(data)
    normalized_data = [(num - min_val) / (max_val - min_val) for num in data]
    
    # Calculate statistics
    mean = statistics.mean(normalized_data)
    median = statistics.median(normalized_data)
    variance = statistics.variance(normalized_data)
    
    return {"normalized_data": normalized_data, "mean": mean, "median": median, "variance": variance}

# Example usage
result = normalize_and_analyze([1, 2, 3, 4, 5])
print(result)