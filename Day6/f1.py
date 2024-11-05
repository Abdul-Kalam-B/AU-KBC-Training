# Write a program that reads a text file line by line 
# counts how many lines contain a specific Tamil word 

file_path = "C:/Users/pc/Desktop/python practice/Test_1/TVAQueries.txt"

counter = 0

with open(file_path , 'r' , encoding='utf-8') as file1:

    data = file1.readlines()

    for line in data:
        words = line.split()
        first_word = set(words)
        counter = len(first_word)

print(f"The first non-repeating words {first_word} ")      
print(f"The total count of words {counter} ")  
