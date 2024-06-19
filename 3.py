def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Input: User provides a number
number = int(input("Enter a number: "))

# Output: Display the factorial of the number
result = factorial(number)
print(f"The factorial of {number} is {result}.")