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

#### Step 1: Implement RSA encryption and decryption in python.

You can check out the full source code here:
📄 [rsa_encryption.py](src/closeSSL/modules/rsa_encryption.py).
> In this section, we will break it down and explain it part by part.
---

**🧠 Main Function:**

```py
if __name__ == "__main__":
    rsa_main()
```
- `rsa_main()`: The main function that runs the RSA encryption tool interface via the command-line.

---

**🔑 Key Generation:**

```python
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    print("[+] Private Key:\n", private_key.decode())
    priv_path = input_path("Save as [private key]: ")
    save_to_file(private_key, priv_path, binary=True)

    print("[+] Public Key:\n", public_key.decode())
    pub_path = input_path("Save as [public key]: ")
    save_to_file(public_key, pub_path, binary=True)
```
- RSA.generate(2048): Generates a new RSA key pair with a key size of 2048 bits. This key pair includes a public and private key.
- .export_key(): Exports the generated RSA key in a format suitable for storage or transmission.
- input_path(): Prompts the user to input a file path where the keys should be saved, using the prompt_toolkit library for improved input handling and file completion.
- save_to_file(): Saves the generated keys to the specified path on the system. The keys are stored in binary format.

---

**🔐 Encryption Logic:**
```python
def encrypt_file_rsa(pub_key_path, in_path, out_path):
    with open(pub_key_path, "rb") as f:
        pub_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(pub_key)
    with open(in_path, "rb") as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)
    save_to_file(ciphertext, out_path, binary=True)
```
- RSA.import_key(): Imports the public key from a file. This key is used to perform the encryption.
- PKCS1_OAEP.new(pub_key): Initializes a cipher using the public key and the OAEP (Optimal Asymmetric Encryption Padding) scheme, which provides enhanced security over traditional RSA padding schemes.
- cipher.encrypt(plaintext): Encrypts the plaintext using the RSA public key. The data is transformed into ciphertext that can only be decrypted with the corresponding private key.
- save_to_file(): Saves the encrypted ciphertext to the specified output file.

---

**🔓 Decryption Logic:**
```python
def decrypt_file_rsa(priv_key_path, in_path, out_path):
    with open(priv_key_path, "rb") as f:
        priv_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(priv_key)
    with open(in_path, "rb") as f:
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    save_to_file(plaintext, out_path, binary=True)
```

- RSA.import_key(): Imports the private key from a file. This key is used to perform the decryption.
- PKCS1_OAEP.new(priv_key): Initializes a cipher using the private key and the OAEP scheme for decryption.
- cipher.decrypt(ciphertext): Decrypts the ciphertext using the RSA private key, recovering the original plaintext.
- save_to_file(): Saves the decrypted plaintext to the specified output file.

---

**💾 File Saving and Input Handling:**
```python
def save_to_file(data, path, binary=False):
    mode = "wb" if binary else "w"
    if os.path.exists(path):
        confirm = input(f"[!] File {path} exists. Overwrite? (y/n): ")
        if confirm.lower() != 'y':
            print("[-] Operation cancelled.")
            return False
    with open(path, mode) as f:
        f.write(data)
    print(f"[+] Saved to {path}")
    return True
```
- save_to_file(): This function handles saving both binary and text data to a file. It ensures that the user is prompted if the file already exists and asks for confirmation to overwrite.
- input_path(): Prompts the user to enter a file path, with path completion support for easier navigation.

---

#### Step 2: Generate an RSA key pair (public and private keys).

1. Run the script:
```bash
python3 rsa_encryption.py
```
---
2. Enter option `3` for generate RSA keys:

```
==================== [Disclaimer: This tools for RSA 2048 bits] ======================

1. Encryption
2. Decryption
3. Generate RSA Keys
q. Exit
Select option: 3
```

---

3. Save private key by enter file name:
   
```
[+] Private Key:
 -----BEGIN RSA PRIVATE KEY-----
...
...
...
-----END RSA PRIVATE KEY-----
Save as [private key]: /home/kali/rsa.key
[+] Saved to /home/kali/rsa.key
```

---

4. save public key by enter file name:

```
[+] Public Key:
 -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo4KeF8TVCx+Wo0Cn0W8e
NMkMA/Eor9vVEcruH7vQnrAO47V6imGOcsJn4ulPTbKrEB8dnprwic+zZJ5P4Ijx
mQrlgjtMGcB0+sEDbaEHLOMdQf6PsRX3fhgF/pYkLEv/tXO1sxzmW1pv6/R0Z7TC
VJwb+3Js4MdHe425qzb2GfOesQDr6o9jWRasxXsPfFjAA1XnMIzgeCCQI0HBd15q
lwUtg71yuOWM4qhi8rfKGBd5ULLxywxP/PqeFiZQcBO0wK1jOqfg7a19dX9e0nPh
G/FVcMa43UI13xO1fgCLEEkOTXLBBgmlIE7n6s91gYfG/9IUlofcwE0d6i9T6XHO
XQIDAQAB
-----END PUBLIC KEY-----
Save as [public key]: /home/kali/rsa.pub
[+] Saved to /home/kali/rsa.pub
```

---

#### Step 3: Encrypt a short message using the public key.

1. Enter a public key, and message file to be encrypt:
```
Enter public key file path: /home/kali/rsa.pub
Enter file path to encrypt: /home/kali/rsa-message.txt
Save as: /home/kali/rsa-message.enc
[+] Saved to /home/kali/rsa-message.enc
Press Enter to return to menu...
```
---

2. Veify:
```
$ cat rsa-message.txt
Hi syed, looks like this even better

$ cat rsa-message.enc
Q����
     <dk'��^��tl�j��
                    =�9L�r�w�CP�?)�i,H�u�`�
�� 1Q��u��p�)}*�u���=xi�
X�����P�*^V�x�WN�/c�����        ��%ȢCF��a3�w����Xl��~%�s|��H�   ��@��.��f'�␦��q?�d��dg�J&k�u�D�4���*   &�˨\EN0)%
        L��޽
            �
             U����P(XG
```
---

#### Task 4: Decrypt it using the private key.

1. Enter a private key, and message file to be decrypt:
```
Select option: 2
Enter private key file path: /home/kali/rsa.key
Enter file path to decrypt: /home/kali/rsa-message.enc
Save as: /home/kali/rsa-message.dec
[+] Saved to /home/kali/rsa-message.dec
Press Enter to return to menu...
```
---

2. Veify:
```
$ cat rsa-message.txt
Hi syed, looks like this even better

$ cat rsa-message.dec
Hi syed, looks like this even better
```
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

#### Step 2: hashing outputs for different inputs.

1. Run the script:
```bash
python3 sha_hashing.py
```

2. Choose option `1` for hashing:
```
Select option: 1
[*] Enter file paths one by one. Press Enter without input to finish.
File path: /home/kali/aes-message.txt
File path: /home/kali/aes-message.enc
File path: /home/kali/aes-message.dec
File path:
```
**Output:**
```
SHA-256 Hash Results:
+-----------------+------------------------------------------------------------------+
| Filename        | SHA-256 Hash                                                     |
+=================+==================================================================+
| aes-message.txt | 610d7cc4dd40abeedd4137fa854bcd3b5a49f03aed89611c08eb33038ccef62d |
+-----------------+------------------------------------------------------------------+
| aes-message.enc | a626c1c274647b6ee85d1fa5049c5662eb36f2d8803ab022863be7a7c072c195 |
+-----------------+------------------------------------------------------------------+
| aes-message.dec | 610d7cc4dd40abeedd4137fa854bcd3b5a49f03aed89611c08eb33038ccef62d |
+-----------------+------------------------------------------------------------------+
```
> Notice that the hash values for `aes-message.txt` and `aes-message.dec` are identical, confirming that the decrypted file matches the original. However, the hash for `aes-message.enc` is different, as expected, since it represents the encrypted content.

### Task 4: Digital Signatures (RSA)

#### Step 1: Sign A message usign RSA private key:

Enter a private key and file to sign. Then save the file:
```
Enter key file path (private key): /home/kali/rsa.key
Enter file path to sign: /home/kali/task_4.txt
Save as (signed): /home/kali/task_4.sign
[+] File signed successfully.
```
---

#### Step 2: Verify the signature using the corresponding public key.

Enter a public key and file to verify. Then enter a sign file:
```
Enter key file path (public): /home/kali/rsa.pub
Enter file path to verify: /home/kali/task_4.txt
Enter signature file path: /home/kali/task_4.sign
[✓] Signature is valid.
Press Enter to return to menu...
```

---

