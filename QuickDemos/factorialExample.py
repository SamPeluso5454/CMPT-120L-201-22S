# Factorial

# Provide a number and we'll calculate the factorial of that number.
def factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(10))