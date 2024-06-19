def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")
