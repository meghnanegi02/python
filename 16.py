from collections import Counter

user_input = input("Enter a string: ")
frequency = Counter(user_input)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
