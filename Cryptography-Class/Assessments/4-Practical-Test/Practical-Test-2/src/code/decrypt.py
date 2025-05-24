from Crypto.Cipher import AES
from hashlib import sha256
import os

# Constants to match the original script
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]  # Corrected the slicing here

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        ciphertext = f.read()
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    
    # Save with original filename (removing .enc)
    original_filepath = filepath.replace(".enc", "")
    with open(original_filepath, "wb") as f:
        f.write(plaintext)
    os.remove(filepath)  # Optional: remove encrypted file after decryption

if __name__ == "__main__":
    folder = "locked_files/"
    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            decrypt_file(os.path.join(folder, filename))
