import numpy as np
from sympy import Matrix
from unicodedata import normalize
import random
import base64

class HillCipher:
    def __init__(self, key_matrix, alphabet):
        self.alphabet = alphabet
        self.n = len(key_matrix)
        self.m = len(alphabet)
        self.key_matrix = Matrix(key_matrix)
        self.modulus = self.m

        det = int(self.key_matrix.det()) % self.modulus
        if np.gcd(det, self.modulus) != 1:
            raise ValueError("The key matrix is not invertible under modulo alphabet length.")
        self.inv_key = self.key_matrix.inv_mod(self.modulus)

    def _text_to_vector_blocks(self, text):
        nums = [self.alphabet.index(ch) for ch in text]
        while len(nums) % self.n != 0:
            nums.append(random.randint(0, self.m - 1))  # padding random
        blocks = [nums[i:i+self.n] for i in range(0, len(nums), self.n)]
        return blocks

    def _vector_blocks_to_text(self, blocks):
        chars = [self.alphabet[num % self.modulus] for block in blocks for num in block]
        return ''.join(chars)

    def encrypt(self, plaintext):
        original_len = len(plaintext)
        blocks = self._text_to_vector_blocks(plaintext)
        encrypted_blocks = [(self.key_matrix @ Matrix(block)) % self.modulus for block in blocks]
        encrypted_text = self._vector_blocks_to_text(encrypted_blocks)
        full_ciphertext = f"{original_len:03d}" + encrypted_text
        encoded_cipher = base64.b64encode(full_ciphertext.encode('utf-8')).decode('utf-8')
        return encoded_cipher

    def decrypt(self, ciphertext):
        decoded_cipher = base64.b64decode(ciphertext.encode('utf-8')).decode('utf-8')
        original_len = int(decoded_cipher[:3])
        actual_ciphertext = decoded_cipher[3:]
        blocks = self._text_to_vector_blocks(actual_ciphertext)
        decrypted_blocks = [(self.inv_key @ Matrix(block)) % self.modulus for block in blocks]
        raw_text = self._vector_blocks_to_text(decrypted_blocks)
        return raw_text[:original_len]

def get_dynamic_alphabet(text):
    cleaned = normalize('NFC', text.upper())
    unique_chars = sorted(set(cleaned))

    extra_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?'
    idx = 0
    while len(unique_chars) < 3:
        char_to_add = extra_chars[idx]
        if char_to_add not in unique_chars:
            unique_chars.append(char_to_add)
        idx += 1
        
    return ''.join(unique_chars)

def generate_invertible_matrix(modulus, n=2):
    attempt = 0
    while True:
        attempt += 1
        matrix = [[random.randint(0, modulus-1) for _ in range(n)] for _ in range(n)]
        det = int(Matrix(matrix).det()) % modulus
        if np.gcd(det, modulus) == 1:
            return matrix
        if attempt > 1000:
            raise ValueError("Cannot find invertible matrix. Try expanding alphabet or changing n.")

def get_user_input():
    print("\n--- EXTENDED HILL CIPHER ---")
    message = input("Enter message to encrypt (can include Vietnamese, Russian, Chinese, etc.): ").strip().upper()
    alphabet = get_dynamic_alphabet(message)
    print(f"Auto-generated alphabet with {len(alphabet)} characters: {alphabet}")
    return alphabet, message

if __name__ == "__main__":
    try:
        alphabet, message = get_user_input()
        key = generate_invertible_matrix(len(alphabet), n=2)
        print(f"Generated invertible key matrix mod {len(alphabet)}: {key}")

        cipher = HillCipher(key_matrix=key, alphabet=alphabet)

        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)

        print("\n--- RESULT ---")
        print("Original message:", message)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
