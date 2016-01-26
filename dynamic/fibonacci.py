# Calculates the n-th Fibonacci number

fibonacci_buffer = [None for x in range(10000)]


def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    if fibonacci_buffer[n] is not None:
        return fibonacci_buffer[n]
    fibonacci_buffer[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_buffer[n]


print fibonacci(0)
print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(100)
