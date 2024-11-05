
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {terms} terms:", fibonacci(terms))
