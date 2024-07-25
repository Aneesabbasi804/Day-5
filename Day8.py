# Function to print 'Hello, World!' to the console
def print_greeting():
    print("Hello, World!")

print_greeting()  # Call the function

# Function to return the maximum alphabetical character from a string
def max_value(text):
    return max(text)

result = max_value("Hello World")
print("Max character:", result)

# Function to convert an integer to its floating-point representation
def convert_to_float(number):
    return float(number)

float_value = convert_to_float(42)
print("Float:", float_value)

# Function to add two numbers and return the sum
def add_numbers(num1, num2):
    return num1 + num2

summation = add_numbers(10, 20)
print("Sum:", summation)

# Function to print a greeting based on the language code
def greet(language_code):
    greetings = {
        'en': "Hello",
        'es': "Hola",
        'fr': "Bonjour"
    }
    print(greetings.get(language_code, "Invalid language code"))

greet('en')  # Hello
greet('es')  # Hola
greet('fr')  # Bonjour
greet('xx')  # Invalid language code

# Function to calculate weekly pay with overtime
def compute_pay(hours, rate):
    pay = hours * rate
    if hours > 40:
        overtime = hours - 40
        pay += overtime * rate * 1.5
    return pay

weekly_pay = compute_pay(45, 10)
print("Weekly pay:", weekly_pay)

# Function to check if a string can be converted to an integer
def is_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

is_int = is_integer("123")
is_string = is_integer("hello")
print("123 is integer:", is_int)
print("hello is integer:", is_string)

# Function to print the lyrics of a song
def print_lyrics(lyrics):
    print(lyrics)

print_lyrics("This is my song, my wonderful song...")  # Replace with actual lyrics

# Function to multiply two numbers and return the product
def multiply_numbers(num1, num2):
    return num1 * num2

product = multiply_numbers(7, 8)
print("Product:", product)

# Function to evaluate and return the result of an expression
def calculate_expression():
    expression = 1 + 2 * float(3) / 4 - 5
    return expression

result = calculate_expression()
print("Expression result:", result)