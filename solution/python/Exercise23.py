import numpy as np
import math

# 1. Letter to Number Mapping
letter_to_number = {
    'A': 8, 'B': 7, 'C': 5, 'D': 13, 'E': 9, 'F': 16,
    'G': 18, 'H': 22, 'I': 4, 'J': 23, 'K': 11, 'L': 3,
    'M': 21, 'N': 1, 'O': 6, 'P': 15, 'Q': 12, 'R': 19,
    'S': 2, 'T': 14, 'U': 17, 'V': 20, 'W': 25, 'X': 24,
    'Y': 10, 'Z': 26
}

# 2. Define Matrix C
# Assuming C is a 3x3 matrix as interpreted above
C = np.array([
    [2, 3, 2],
    [1, 4, 2],
    [5, 2, 3]
])

# Check if C is square and nonsingular
if C.shape[0] != C.shape[1]:
    raise ValueError("Matrix C must be square.")
if np.linalg.det(C) == 0:
    raise ValueError("Matrix C must be nonsingular (determinant ≠ 0).")

# 3. Function to Convert Message to Numbers
def message_to_numbers(message):
    numbers = []
    for char in message.upper():
        if char in letter_to_number:
            numbers.append(letter_to_number[char])
        else:
            print(f"Warning: Character '{char}' is not a valid uppercase letter and will be ignored.")
    return numbers

# 4. Function to Create Matrix A
def create_matrix_A(numbers):
    length = len(numbers)
    n = math.ceil(math.sqrt(length))  # Determine the smallest n where n^2 >= length
    total_elements = n * n
    padded_numbers = numbers + [0]*(total_elements - length)  # Pad with zeros if necessary
    A = np.array(padded_numbers).reshape(n, n)
    return A, n

# 5. Function to Encode Message
def encode_message(message, C):
    numbers = message_to_numbers(message)
    A, n = create_matrix_A(numbers)
    
    # Ensure C is compatible with A for multiplication
    if C.shape[1] != A.shape[0]:
        raise ValueError(f"Matrix C's number of columns ({C.shape[1]}) must equal Matrix A's number of rows ({A.shape[0]}).")
    
    encoded_matrix = np.dot(C, A)
    return encoded_matrix, A, n

# 6. Function to Display Matrix
def display_matrix(matrix, name):
    print(f"Matrix {name}:")
    for row in matrix:
        print(' '.join(f"{int(elem):3}" for elem in row))
    print()

# 7. Main Execution
if __name__ == "__main__":
    # Example message
    message = "BILA KOCKA"
    
    try:
        encoded_matrix, A, n = encode_message(message, C)
        
        # Display original matrix A
        display_matrix(A, 'A (Original Message Matrix)')
        
        # Display encoded matrix
        display_matrix(encoded_matrix, 'C × A (Encoded Matrix)')
        
    except ValueError as ve:
        print(f"Error: {ve}")
