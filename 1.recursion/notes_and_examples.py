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
        - Recursion canb be slow.
"""

def factorial(n):
    """Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.
    """
    assert n >= 0 and int(n) == n, "The number must be positive integer only!"
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Ask for a number
    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial(number)}")
