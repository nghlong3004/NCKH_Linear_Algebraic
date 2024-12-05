import numpy as np

# Hill cipher matrix (enciphering matrix)
key_matrix = np.array([[4, 1], [3, 2]])

# Message to decode
ciphertext = "KNOXAOJX"

# Mapping letters to numbers (A=0, B=1, ..., Z=25)
def letter_to_number(letter):
    return ord(letter) - ord('A')

def number_to_letter(number):
    return chr(number + ord('A'))

# Prepare the ciphertext in numerical form
cipher_numbers = [letter_to_number(letter) for letter in ciphertext]

# Reshape ciphertext into pairs (as Hill cipher works with 2x2 blocks)
cipher_pairs = np.array(cipher_numbers).reshape(-1, 2)

# Calculate the inverse of the key matrix modulo 26
def mod_inverse(matrix, mod):
    det = int(np.linalg.det(matrix)) % mod
    det_inv = pow(det, -1, mod)  # Modular inverse of the determinant
    if det_inv is None:
        raise ValueError("Matrix is not invertible.")
    adjugate = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])
    inverse_matrix = (det_inv * adjugate) % mod
    return inverse_matrix

# Inverse of the key matrix modulo 26
inverse_key_matrix = mod_inverse(key_matrix, 26)

# Decrypt the ciphertext by multiplying the inverse key matrix with each pair of numbers
plaintext_numbers = []
for pair in cipher_pairs:
    decrypted_pair = np.dot(inverse_key_matrix, pair) % 26
    plaintext_numbers.extend(decrypted_pair)

# Convert the numbers back to letters
plaintext = ''.join([number_to_letter(int(round(num))) for num in plaintext_numbers])
print("Decrypted message:", plaintext)
