# Data Type Conversion Tasks

# 1. Convert String to Integer
def string_to_integer(s):
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return int(s)
    else:
        return None

# 2. Convert Integer to String
def integer_to_string(n):
    return str(n)

# 3. Convert Float to Integer
def float_to_integer(f):
    if f % 1 == 0:
        return int(f)
    else:
        return None

# 4. Convert List of Strings to List of Integers
def list_of_strings_to_list_of_integers(lst):
    result = []
    for s in lst:
        if s.startswith('-') and s[1:].isdigit():
            result.append(int(s))
        elif s.isdigit():
            result.append(int(s))
    return result

# Arithmetic Operation Tasks

# 5. Addition of Two Numbers
def add_two_numbers(a, b):
    return a + b

# 6. Subtraction of Two Numbers
def subtract_two_numbers(a, b):
    return a - b

# 7. Multiplication of Two Numbers
def multiply_two_numbers(a, b):
    return a * b

# 8. Division of Two Numbers
def divide_two_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# String Operation Tasks

# 9. Concatenate Two Strings
def concatenate_two_strings(s1, s2):
    return s1 + s2

# 10. Reverse a String
def reverse_string(s):
    return s[::-1]
