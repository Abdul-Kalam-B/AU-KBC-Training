
def is_palindrome(string):
    return string == string[::-1]

def find_palindromes(strings):
    palindromes = []
    for string in strings:
        if is_palindrome(string):
            palindromes.append(string)
    return palindromes

input_strings = input("Enter a list of words separated by spaces: ").split()

palindromes = find_palindromes(input_strings)
print("Palindromes in the list:", palindromes)
