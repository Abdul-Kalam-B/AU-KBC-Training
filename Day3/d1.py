#frequency of each element
items = input("Enter elements of the list separated by spaces: ").split()

frequency = {}

for element in items:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Frequency of elements:", frequency)
