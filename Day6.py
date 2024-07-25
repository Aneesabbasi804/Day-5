# Gross Pay Calculation
def gross_pay():
  hours = float(input("Enter the number of hours worked: "))
  rate = float(input("Enter the hourly wage rate: "))
  pay = hours * rate
  print(f"Total pay: ${pay:.2f}")

# Temperature Conversion
def temp_conversion():
  celsius = float(input("Enter temperature in Celsius: "))
  fahrenheit = (celsius * 9/5) + 32
  print(f"{celsius:.2f} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

# Number Sign Check
def number_sign_check():
  number = float(input("Enter a number: "))
  if number > 0:
    print("The number is positive.")
  elif number < 0:
    print("The number is negative.")
  else:
    print("The number is zero.")

# Leap Year Checker
def leap_year_check():
  year = int(input("Enter a year: "))
  if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")

# Basic Arithmetic Operations
def basic_arithmetic():
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  sum = num1 + num2
  difference = num1 - num2
  product = num1 * num2
  quotient = num1 / num2  # Handle division by zero later
  print(f"Sum: {sum:.2f}")
  print(f"Difference: {difference:.2f}")
  print(f"Product: {product:.2f}")
  print(f"Quotient: {quotient:.2f}")  # Print if no division by zero

# Calculate Factorial
def factorial():
  number = int(input("Enter a non-negative number: "))
  if number < 0:
    print("Factorial is not defined for negative numbers.")
    return
  factorial = 1
  for i in range(1, number + 1):
    factorial *= i
  print(f"The factorial of {number} is {factorial}")

# Reverse a String
def reverse_string():
  text = input("Enter a string: ")
  reversed_text = text[::-1]
  print(f"Reversed string: {reversed_text}")

# Multiply Two Numbers
def multiply():
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  product = num1 * num2
  print(f"Product: {product:.2f}")

# Square of a Number
def square():
  number = float(input("Enter a number: "))
  square = number * number
  print(f"Square: {square:.2f}")

# Divide Two Numbers
def divide():
  num1 = float(input("Enter first number (dividend): "))
  num2 = float(input("Enter second number (divisor): "))
  if num2 == 0:
    print("Error: Division by zero is not allowed.")
  else:
    quotient = num1 / num2
    print(f"Quotient: {quotient:.2f}")

# Call the functions in sequence
gross_pay()
temp_conversion()
number_sign_check()
leap_year_check()
basic_arithmetic()
factorial()
reverse_string()
multiply()
square()
divide()

print("All calculations completed!")