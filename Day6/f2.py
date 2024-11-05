# Create a program that reads the file and identifies the longest line
# based on character count. Print that line and its length.

file_path = "C:/Users/pc/Desktop/python practice/TVAQueries.txt"

longest_line = ''
max = 0

with open(file_path , 'r' , encoding='utf-8') as file1: 
    data = file1.readlines()
    for line in data:
        line_length = len(line.strip())

        if line_length > max:
            max = line_length
            longest_line = line.strip()

print(f"Longest line is {longest_line} ")
print(f"Max count of word {max} ")       
