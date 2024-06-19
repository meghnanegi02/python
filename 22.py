def min_max(lst):
    return min(lst), max(lst)

lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
minimum, maximum = min_max(lst)
print(f"The minimum value in the list is {minimum} and the maximum value is {maximum}.")
