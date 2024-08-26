# fibonacci sequence
def fibonacci(n):
    fib_sequence = []
    
    # First two numbers of the sequence
    a, b = 0, 1
    
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b  # Update to the next numbers in the sequence
    
    return fib_sequence

# Input: Number of terms in the Fibonacci sequence to generate
n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

# Output: Fibonacci sequence up to n terms
print(f"The first {n} terms of the Fibonacci sequence are: {fibonacci(n)}")
