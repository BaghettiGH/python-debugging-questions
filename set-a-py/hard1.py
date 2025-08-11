# Expected output: 120 for factorial(5)

def factorial(n):
    return n * factorial(n - 1)

print(factorial(5))
