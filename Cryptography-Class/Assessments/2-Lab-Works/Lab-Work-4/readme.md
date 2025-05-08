# Lab 4: Implementing Cryptography with Python 🐍
> Hey everyone! In this lab, we're working on some cryptography tools using Python.
> Sounds tough, right? Don't worry!! [Syed](https://github.com/yed-0) and I felt the same way at first.
> But as time went on, we started to really get the hang of it. So hang in there!
> Psss.. we did this with vibe coding ✨

---

**Lab Objective:**
1. Implement symmetric encryption using AES `(AES-256-CBC)`.
2. Implement asymmetric encryption using RSA `(2048-bit)`.
3. Explore hashing using `SHA-256`.
4. Implement digital signatures using RSA.
> We're not covering every type of cryptography out there, but at least we’re getting the idea, right?

---

## Requirements:

Make sure you have Python 3 installed. Then, install the required Python libraries using pip:
```bash
pip3 install cryptography pycryptodome prompt_toolkit tabulate
```
- `cryptography` – Provides high-level tools for AES, RSA, and digital signatures with secure, modern cryptographic practices.
- `pycryptodome` – Offers low-level cryptographic primitives like AES and SHA-256 with more control and flexibility.
- `prompt_toolkit` – Enhances command-line interfaces with features like auto-completion, syntax highlighting, and better input handling.
- `tabulate` – Formats data into nicely structured readable output in the terminal.

> Best practice: Install these libraries in a Python virtual environment.

To create and activate a Python virtual environment, follow these steps:

```bash
# Step 1: Create a virtual environment
python3 -m venv <env_name> # example: crypto_venv

# Step 2: Activate the virtual environment
source <env_name>/bin/activate
source <env_name>/bin/deactive # for deactived

# Step 3: Install the required libraries
pip install cryptography pycryptodome prompt_toolkit tabulate
```

> Remember to activate the virtual environment each time you work on this project to ensure dependencies are isolated.


---

## Lab Tasks:

### Task 1: Symmetric Encryption `(AES-256-CBC)`

---

#### Step 1: Implement AES encryption and decryption in Python.

You can check out the full source code here:
📄 [aes_encryption.py](src/closeSSL/modules/aes_encryption.py).
> In this section, we will break it down and explain it part by part.

---

**🧠 Starting Point: Main Function:**

```py
if __name__ == "__main__":
    aes_main()
```
- `aes_main()` - The core function that runs the whole encryption interface via CLI.

---

**🔑 Key and IV Generation:**

```py
def generate_key():
    key = get_random_bytes(32)  # 256 bits
    print("\n[+] Generated Key (hex):", key.hex())
    return key


def generate_iv():
    iv = get_random_bytes(16)  # 128 bits
    print("\n[+] Generated IV (hex):", iv.hex())
    return iv
```
- `get_random_bytes(n)`: Generates `n` cryptographically secure random bytes using `os.urandom`, essential for secure key/IV creation.
- `.hex()`: Converts bytes to a hexadecimal string for readable key/IV output and storage.

---

**💾 Saving and Loading Files:**
```py
def save_to_file(data, path):
    if os.path.exists(path):
        confirm = input(f"[!] File {path} exists. Overwrite? (y/n): ")
        if confirm.lower() != 'y':
            print("[-] Operation cancelled.")
            return
    with open(path, "wb") as f:
        f.write(data)
    print(f"[+] Saved to {path}")
```
- `os.path.exists(path)`: Checks if a file exists at `path`, preventing overwrites without user consent.
- `open(path, mode)`: Opens a file in specified mode ('wb' for binary write), enabling file I/O operations.
- `f.write(data)`: Writes binary data to an open file, used to save keys, IVs, or ciphertext.
- `save_to_file(data, path)`: Saves binary data to a file with overwrite protection, used for keys, IVs, and encrypted/decrypted files.

```py
def load_hex_file(path):
    with open(path, "r") as f:
        return binascii.unhexlify(f.read().strip())
```
- `f.read()`: Reads the entire content of an open file as a string, used to load hex-encoded key/IV.
- `.strip()`: Removes leading/trailing whitespace from a string, ensuring clean hex string input for decoding.
- `binascii.unhexlify(hex_str)`: Converts a hex string to bytes, used to decode hex-encoded key/IV from files.
- `load_hex_file(path)`: Loads and decodes a hex-encoded file into bytes, used to retrieve keys or IVs for decryption.

---

**🔐 Encryption Logic:**
```py
def encrypt_file(key, iv, in_path, out_path):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_path, "rb") as f:
        plaintext = f.read()
    # Padding (PKCS7)
    pad_len = 16 - len(plaintext) % 16
    plaintext += bytes([pad_len] * pad_len)
    ciphertext = cipher.encrypt(plaintext)
    save_to_file(ciphertext, out_path)
```
- `AES.new(key, mode, iv)`: Initializes an AES cipher object with key, CBC mode, and IV for encryption operations.
- `f.read()`: Reads the entire file content as bytes, used to load plaintext for encryption.
- `len(data)`: Returns the length of a byte string, used to calculate padding needs for AES block alignment.
- `%`: Modulus operator calculates remainder, used to determine padding length for AES 16-byte block size.
- `bytes([pad_len] * pad_len)`: Creates a byte string of repeated padding bytes (PKCS7), ensuring plaintext aligns with AES block size.
- `plaintext += ...`: Concatenates padding bytes to plaintext, preparing it for AES encryption.
- `cipher.encrypt(plaintext)`: Encrypts padded plaintext using AES-256 CBC, producing ciphertext for secure storage.
- `encrypt_file(key, iv, in_path, out_path)`: Reads file, applies PKCS7 padding, encrypts with AES-256 CBC, and saves ciphertext.

---

**🔓 Decryption Logic:**
```py
def decrypt_file(key, iv, in_path, out_path):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_path, "rb") as f:
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    pad_len = plaintext[-1]
    plaintext = plaintext[:-pad_len]
    save_to_file(plaintext, out_path)
```
- `AES.new(key, mode, iv)`: Initializes an AES cipher object with key, CBC mode, and IV for decryption operations.
- `f.read()`: Reads the entire file content as bytes, used to load ciphertext for decryption.
- `cipher.decrypt(ciphertext)`: Decrypts ciphertext using AES-256 CBC, recovering padded plaintext.
- `plaintext[-1]`: Accesses the last byte of plaintext, which indicates the PKCS7 padding length for removal.
- `plaintext[:-pad_len]`: Slices plaintext to remove padding bytes, restoring the original unencrypted data.
- `decrypt_file(key, iv, in_path, out_path)`: Reads ciphertext, decrypts with AES-256 CBC, removes padding, and saves plaintext.

---

#### Step 2: Encrypt a message with secret key.

1. Run the `aes_encryption.py` script:

```bash
python3 aes_encryption.py
```

---

2. For encrypt a messge using our tools, choose option `1`.
```
=================== [Disclaimer: This tools for aes-256-cbc only] =====================

1. Encryption
2. Decryption
q. Exit
Select option:
```

---

3. Enter a secret key file path or press `n` to generate key:

```
Enter key file path or press `n` to generate key: n

[+] Generated Key (hex): 71d86b5a1709c7d46800e06c4f2de834e1b8388c5abd2ee609aa853c3852d813
Save key as: /home/kali/aes-secret.key
[+] Saved to /home/kali/aes-secret.key

[+] Generated IV (hex): cbec90f1eadf2acaaab3e7707aec6488
Save IV as: /home/kali/aes-secret.iv
[+] Saved to /home/kali/aes-secret.iv

Enter file path to encrypt: /home/kali/aes-message.txt
Save encrypted file as: /home/kali/aes-message.enc
[+] Saved to /home/kali/aes-message.enc
[+] Done. Press Enter to continue...
```

4. Verify the message is encrypted:

```bash
$ cat aes-message.txt
Syed, our secret is secure now with this closeSSL.

$ cat aes-message.enc
��bnO����&���Yz����e���3�L��h
                             }+��QwA���y��DQ���g�]x�{�
```
> See, we cant read it anymore...
---

#### Step 3: Decrypt the ciphertext back to the original message.

1. For decrypt a messge using our tools, choose option `2`.

```
=================== [Disclaimer: This tools for aes-256-cbc only] =====================

1. Encryption
2. Decryption
q. Exit
Select option:
```

2. Enter key, iv and encrypted file. Then save the decrypt file:

```
Select option: 2
Enter key file path: /home/kali/aes-secret.key
Enter IV file path: /home/kali/aes-secret.iv
Enter file path to decrypt: /home/kali/aes-message.enc
Save decrypted file as: /home/kali/aes-message.dec
[+] Saved to /home/kali/aes-message.dec
[+] Done. Press Enter to continue..
```

3. Verify the message has been decrypt and not been tampered:

```bash
$ cat aes-message.dec
Syed, our secret is secure now with this closeSSL.

$ diff aes-message.txt aes-message.dec

$
```

---

### Task 2: Asymmetric Encryption (RSA)

---

### Task 3: Hashing (SHA-256)

---

#### Step 1: Implement SHA Hashing in Python.

You can check out the full source code here:
📄 [sha_hashing.py](src/closeSSL/modules/sha_hashing.py).
> In this section, we’ll break it down part by part to understand what each function does.
---

**🧠 Entry Point:**

```python
if __name__ == "__main__":
    sha_main()
```

* **`sha_main()`** – Runs the interactive terminal-based hashing tool.

---

**📁 Collecting File Paths:**

```python
def collect_file_paths():
    paths = []
    print("[*] Enter file paths one by one. Press Enter without input to finish.")
    while True:
        path = prompt("File path: ", completer=PathCompleter())
        if not path.strip():
            break
        paths.append(path.strip())
    return paths
```

- `prompt(prompt_text, completer)`: Uses `prompt_toolkit` to display an interactive prompt with file path auto-completion for user input.
- `PathCompleter()`: Provides file system path auto-completion, enhancing user experience during file path entry.
- `path.strip()`: Removes leading/trailing whitespace from the input path, ensuring clean file path strings.
- `paths.append(path)`: Adds each valid file path to a list for processing, building a collection of files to hash.
- `if not path.strip()`: Checks for an empty input (after stripping whitespace) to exit the input loop.
- `collect_file_paths()`: Gathers multiple file paths via an interactive CLI, returning a list of paths when the user submits an empty input.

---

**🔐 SHA-256 Hashing Logic:**

```python
def hash_file_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None
```

- `hashlib.sha256()`: Initializes a SHA-256 hash object from Python’s `hashlib` module for cryptographic hashing.
- `open(file_path, "rb")`: Opens the specified file in binary read mode to access its raw bytes for hashing.
- `f.read(4096)`: Reads the file in 4KB chunks to efficiently handle large files without loading them entirely into memory.
- `while chunk := ...`: Assigns each chunk to `chunk` and continues looping until no more data is read (empty chunk).
- `sha256.update(chunk)`: Updates the SHA-256 hash object with each chunk, incrementally building the hash.
- `sha256.hexdigest()`: Returns the final SHA-256 hash as a 64-character hexadecimal string.
- `try ... except FileNotFoundError`: Catches file-not-found errors, returning `None` to indicate an invalid file path.
- `hash_file_sha256(file_path)`: Computes the SHA-256 hash of a file by reading it in chunks, returning the hex hash or `None` if the file is missing.

---

**📊 Hash Results Display:**

```python
result_table = []
for path in file_paths:
    hash_result = hash_file_sha256(path)
    if hash_result:
        result_table.append([os.path.basename(path), hash_result])
    else:
        result_table.append([os.path.basename(path), "[File not found]"])

print("\nSHA-256 Hash Results:")
print(tabulate(result_table, headers=["Filename", "SHA-256 Hash"], tablefmt="grid"))
```
- `os.path.basename(path)`: Extracts the filename from a file path, used for concise display in the output table.
- `hash_file_sha256(path)`: Calls the hashing function to compute the SHA-256 hash for each file path.
- `result_table.append([...])`: Builds a list of lists, where each inner list contains a filename and its hash (or "[File not found]" if invalid).
- `if hash_result`: Checks if the hash is valid (not `None`), determining whether to display the hash or an error message.
- `tabulate(result_table, headers, tablefmt)`: Formats the results as a grid-style table using the `tabulate` library, with "Filename" and "SHA-256 Hash" as headers.
- `print(...)`: Outputs the formatted table to the terminal, presenting the hashing results in a readable format.

---

### Task 4: Digital Signatures (RSA)

---

