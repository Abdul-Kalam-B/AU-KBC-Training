# Function to find common elements and symmetric difference
def find_common_and_symmetric_difference(set1, set2):
    common_elements = set1 & set2
    symmetric_difference = set1 ^ set2
    
    return common_elements, symmetric_difference

set1 = {int(x) for x in input("Enter element 1 : ").split()}
set2 = {int(y) for y in input("Enter element 2 : ").split()}

# Finding common elements and symmetric difference
common, sym_difference = find_common_and_symmetric_difference(set1, set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Common elements:", common)
print("Symmetric difference:", sym_difference)
