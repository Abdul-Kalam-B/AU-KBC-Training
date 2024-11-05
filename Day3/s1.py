# Function to find unique elements in a list
def unique_elements(input_list):
    return set(input_list)

elements = input("Enter elements of the list separated by spaces: ").split()

unique_set = unique_elements(elements)

print("Original list:", elements)
print("Unique elements:", unique_set)
