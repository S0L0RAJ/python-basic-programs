# Prime Number Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

# Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
