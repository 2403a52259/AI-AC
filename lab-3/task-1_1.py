def factorial(n):
   
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle base cases
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial using iteration
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
   
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 10]
    
    print("Testing factorial function:")
    for num in test_numbers:
        result = factorial(num)
        print(f"factorial({num}) = {result}")
    
    print("\nTesting recursive factorial function:")
    for num in test_numbers:
        result = factorial_recursive(num)
        print(f"factorial_recursive({num}) = {result}")
    
    # Test error handling
    try:
        factorial(-1)
    except ValueError as e:
        print(f"\nError caught: {e}")
    
    try:
        factorial(3.5)
    except TypeError as e:
        print(f"Error caught: {e}")
