# Reads a sequence of numbers from the user, calculates their sum and average, and prints both.
def calculate_sum_and_average():
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == 'done':
            break

        if user_input.replace('.', '', 1).isdigit():
            num = float(user_input)
            total += num
            count += 1
        else:
            print("Invalid input. Please enter a number or 'done'.")

    if count == 0:
        print("No numbers were entered.")
    else:
        average = total / count
        print(f"Sum: {total}")
        print(f"Average: {average}")

# Takes a list of numbers and prints only those that are greater than a given threshold.
def filter_values():
    numbers = [12, 45, 7, 23, 56, 89, 34]
    threshold = 30

    print("Numbers greater than", threshold, "are:")

    for num in numbers:
        if num > threshold:
            print(num)

filter_values()

# Finds the largest and smallest numbers in a list of integers provided by the user
def find_largest_and_smallest():
    numbers = input("Enter a list of numbers separated by space: ").split()
    numbers = [int(num) for num in numbers]

    # Find the largest number
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    # Find the smallest number
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    print("Largest number is:", largest)
    print("Smallest number is:", smallest)

# Removes duplicates from a list of integers.
def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    print(f"List without duplicates: {unique_numbers}")

# Reads lines of text from the user until they enter 'done'. Skips lines starting with '#'.
def break_and_continue():
    while True:
        line = input("Enter a line of text (or 'done' to finish): ")
        if line == 'done':
            break
        if line.startswith('#'):
            continue
        print(line)

# Prompts the user to guess a pre-defined number, limiting attempts to 10.
def guess_number():
    secret_number = 7
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = input("Guess the number: ")
        if guess.isdigit() and int(guess) == secret_number:
            print("Congratulations! You guessed the number.")
            return
        else:
            print("Incorrect guess. Try again.")
        attempts = attempts + 1
    
    print("Sorry, you've reached the maximum number of attempts.")

# Calculates the sum of the squares of the first N natural numbers, where N is provided by the user.
def sum_of_squares():
    N = int(input("Enter a number: "))
    sum_squares = sum(i**2 for i in range(1, N + 1))
    print(f"Sum of squares of first {N} natural numbers: {sum_squares}")

# 8. Reverse a String: Takes a string as input and prints the string in reverse order.
def print_reverse_string():
    string = input("Enter a string: ")

    print("Reversed string is:", string[::-1])

# 9. Fibonacci Sequence: Prints the first N numbers in the Fibonacci sequence, where N is provided by the user.
def print_fibonacci_sequence():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))

    if n <= 0:
        print("Please enter a positive integer.")
        return

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    print("The first", n, "numbers in the Fibonacci sequence are:")
    for i, num in enumerate(fibonacci_sequence):
        print(f"Fibonacci number {i}: {num}")

# Usage of the functions
if __name__ == "__main__":
    print("1. Sum and Average")
    calculate_sum_and_average()

    print("\n2. Filtering Values")
    numbers = [10, 15, 3, 7, 20, 5, 25]
    threshold = 10
    filter_values(numbers, threshold)

    print("\n3. Finding the Largest and Smallest")
    find_largest_and_smallest(numbers)

    print("\n4. Removing Duplicates")
    numbers_with_duplicates = [10, 15, 3, 7, 20, 5, 25, 10, 3]
    remove_duplicates(numbers_with_duplicates)

    print("\n5. Break and Continue")
    break_and_continue()

    print("\n6. Infinite Loop Prevention")
    guess_number()

    print("\n7. Sum of Squares")
    sum_of_squares()

    print("\n8. Reverse a String")
    print_reverse_string()

    print("\n9. Fibonacci Sequence")
    print_fibonacci_sequence()