"""I'll create examples and add notes as comments while I'm learning recursion.

Notes:
    When to use recursion:
        - When we can easily breakdown a problem into smaller similar sub-problems.
        - When we are fine with extra overhead (both time and space) that comes with it.
        - When we need a quick working solution instead of efficient one.
        - When traverse a tree or graph.
        - When we use memoization in recursion.

    When not to use recursion:
        - If time and space complexity matters for us.
        - Recursion uses more memory. If we use embedded memory. For example an application that
        takes more memory in the phone is not efficient.
        - Recursion can be slow.
"""

def get_factorial(number: int) -> int:
    """Calculate the factorial of a number.

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.
    """
    assert number >= 0 and int(number) == number, "The number must be positive integer only!"
    if number in [0, 1]:
        return 1
    return number * get_factorial(number - 1)

def get_fibonacci(number: int) -> int:
    """Calculate the fibonacci of a number.

    Args:
        number (int): The number to calculate the fibonacci of.

    Returns:
        int: The fibonacci of the number.
    """
    assert number >= 0 and int(number) == number, "The number must be positive integer only!"
    if number in [0, 1]:
        return number
    return get_fibonacci(number - 1) + get_fibonacci(number - 2)

if __name__ == "__main__":
    input_number = int(input("Enter a number: "))
    # print(f"Factorial of {input_number} is {get_factorial(input_number)}")
    print(f"Fibonacci of {input_number} is {get_fibonacci(input_number)}")
