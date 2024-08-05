#Task 1: Complex Number Arithmetic with Error Handling
def complex_arithmetic(num1, num2, op):
    if op not in ['+', '-', '*', '/']:
     raise ValueError("Invalid operation")
    if num2 == (0, 0) and op == '/':
     raise ZeroDivisionError("Cannot divide by zero")
    real1, imag1 = num1
    real2, imag2 = num2
    if op == '+':
     return (real1 + real2, imag1 + imag2)
    elif op == '-':
     return (real1 - real2, imag1 - imag2)
    elif op == '*':
     return (real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2)
    elif op == '/':
     denominator = real2 ** 2 + imag2 ** 2
     return ((real1 * real2 + imag1 * imag2) / denominator, (imag1 * real2 - real1 * imag2) / denominator)

#Task 2: Conditional Polynomial Evaluation with Multiple Conditions
def evaluate_polynomial(coefficients, x):
    degree = len(coefficients) - 1
    if degree == 0:
     return coefficients[0]
    elif degree == 1:
      return coefficients[0] + coefficients[1] * x
    elif degree == 2:
      return coefficients[0] + coefficients[1] * x + coefficients[2] * x ** 2
    else:
       result = 0
       for i, coeff in enumerate(coefficients):
            result += coeff * x ** i
       return result

#Task 3: Recursive Fibonacci with Depth Limitation
def fibonacci(n, depth_limit=100):
    if n <= 1:
        return n
    elif depth_limit <= 0:
        return "Depth limit reached"
    else:
        return fibonacci(n-1, depth_limit-1) + fibonacci(n-2, depth_limit-1)

#Task 4: Higher-order Functions for Adaptive Integration
def adaptive_integration(func, a, b, tol=1e-6):
    def integrate(func, a, b, tol):
        mid = (a + b) / 2
        left = integrate(func, a, mid, tol)
        right = integrate(func, mid, b, tol)
        if abs(left + right - func(mid)) < tol:
            return left + right
        else:
          return integrate(func, a, mid, tol/2) + integrate(func, mid, b, tol/2)
    return integrate(func, a, b, tol)

#Task 5: Optimized Prime Number Generator with Caching
def prime_generator(limit):
    cache = {}
    def is_prime(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        cache[n] = True
        return True
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

#Task 6: Memoized Fibonacci Sequence with Iterative Fallback
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

    if len(memo) > 1000:  # fallback to iterative approach

        a, b = 0, 1

        for _ in range(n):

            a, b = b, a + b

        return a

#Task 7: Regular Expression Based String Parsing
import re
def extract_dates(s):
    pattern = r'\d{4}-\d{2}-\d{2}'
    return re.findall(pattern, s)

#Task 8: Advanced String Transformation with Multiple Conditions
def transform_string(s):
    words = s.split()
    transformed_words = []
    for word in words:
        if len(word) > 5:
            word = word[::-1]
        transformed_words.append(word)
    s = ' '.join(transformed_words)
    s = s.title()
    return s

#Task 9: Dynamic Expression Evaluator with Variable Substitution
def complex_arithmetic(num1, num2, op):

   # Check if the inputs are valid
    if not isinstance(num1, tuple) or not isinstance(num2, tuple):
        raise ValueError("Both numbers must be tuples")
    if len(num1) != 2 or len(num2) != 2:
        raise ValueError("Both tuples must have exactly two elements")
    if not all(isinstance(x, (int, float)) for x in num1 + num2):
        raise ValueError("All elements of the tuples must be numbers")

    # Check if the operation is valid
    if op not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operation")
    
   # Perform the operation
    real1, imag1 = num1
    real2, imag2 = num2
    if op == '+':
        return (real1 + real2, imag1 + imag2)
    elif op == '-':
        return (real1 - real2, imag1 - imag2)
    elif op == '*':
        return (real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2)
    elif op == '/':
        
    # Check for division by zero
        if real2 == 0 and imag2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        denominator = real2 ** 2 + imag2 ** 2
        return ((real1 * real2 + imag1 * imag2) / denominator, (imag1 * real2 - real1 * imag2) / denominator)

#Here's an example of how you can use this function:

print(complex_arithmetic((1, 2), (3, 4), '+'))  # Output: (4, 6)

print(complex_arithmetic((1, 2), (3, 4), '-'))  # Output: (-2, -2)

print(complex_arithmetic((1, 2), (3, 4), '*'))  # Output: (-5, 10)

print(complex_arithmetic((1, 2), (3, 4), '/'))  # Output: (0.44, 0.08)