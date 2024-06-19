
def checkEvenOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))

result = checkEvenOdd(number)
print(f"The number {number} is {result}.")