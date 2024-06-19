def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Type 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").upper()
temperature = float(input("Enter the temperature to convert: "))

if choice == 'C':
    converted = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted}°F.")
elif choice == 'F':
    converted = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted}°C.")
else:
    print("Invalid input. Please enter 'C' or 'F'.")
