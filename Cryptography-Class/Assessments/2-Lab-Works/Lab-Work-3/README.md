# Lab 3: Hands-on Exploration of Cryptographic Tools: Hashing, Encryption, and Digital Signatures

**🎯 Lab Objective:**
In this lab, we’ll explore the basics of cryptography using **OpenSSL**, a powerful and widely-used command-line toolkit for cryptographic operations.

We'll go through the following tasks **step-by-step**:
- **Encrypt** and **decrypt** files using **AES (symmetric encryption)** and **RSA (asymmetric encryption)**
- **Generate** and **verify** **SHA-256 hashes** to ensure data integrity
- **Create** and **verify** **digital signatures** using **RSA** and **SHA-256**

> By the end of this walkthrough, you’ll have hands-on experience with key cryptographic concepts and how they’re applied using OpenSSL.

---

## 📦 Tools Used:
1. OpenSSL
2. [Wormhole](https://wormhole.app/) (end-to-end encryption private file sharing)

---

## 💼 Lab Tasks:

### Task 1: Symmetric Encryption and Decryption using AES-256-CBC
**🎯 Objective:** In this task, we (me and [Syed](https://github.com/yed-0)) will simulate how to send a confidential message securely using symmetric encryption. We’ll use the AES-256-CBC encryption algorithm in OpenSSL to encrypt and decrypt a message.

<div style="display: flex; justify-content: center; margin-top: 20px;">
  <div style="font-family: monospace; background-color: #0d1117; color: #c9d1d9; padding: 8px 12px; border-radius: 6px;">
    <a href="https://github.com/yed-0" target="_blank" style="color: #58a6ff; text-decoration: none;">syed</a>
    --[confidential 📨]--> 
    <a href="https://github.com/abutheone" target="_blank" style="color: #58a6ff; text-decoration: none;">me</a>
  </div>
</div>

---


#### Step 1: Research how to generate a strong, random key using `OpenSSL`.

**Command for create [key](Assets/Task-1/key):**
```bash
openssl rand -hex 32 > key
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ openssl rand -hex 32 > key

┌──(syed㉿NWS23010037)-[~]
└─$ cat key
595369a67de06fa9619e2cab404180e958e07dc258423b6509b11dfd4c4aa8f3
```


**Command for create [iv](Assets/Task-1/iv):**
```bash
openssl rand -hex 16 > iv
```
**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ openssl rand -hex 16 > iv

┌──(syed㉿NWS23010037)-[~]
└─$ cat iv
bac6130b2c33397a5afbf851cfd0acb9
```


**Based on our discussion**, here’s a breakdown of the research process for generating a strong, random key using OpenSSL for AES-256-CBC encryption. Keeping it short and to the point.
- `openssl rand` command generates cryptographically secure random data.
- For AES-256, a 32-byte key is needed. `openssl rand -hex 32` outputs 64 hex characters (32 bytes).
- For CBC mode, a 16-byte IV is required. `openssl rand -hex 16` outputs 32 hex characters (16 bytes).
- Hex format is **compatible** with OpenSSL’s `-K` and `-iv` options for direct key/IV input.

---
#### Step 2: Create a Message to Encrypt
Here syed create a message to encrypt.

**Command for create a message:**
```bash
echo "isi message sini syed" > syed.txt
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ echo "kelisa putih nampak rare" > "syed.txt"
```

---
#### Step 3: Encrypt the Message Using AES-256-CBC
Next, Syed encrypted the message using AES-256-CBC with the key and IV.

**The OpenSSL command is:**
```bash
openssl enc -e -aes-256-cbc -K $(cat key) -iv $(cat iv) -in filename -out filename.enc
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ openssl enc -e -aes-256-cbc -K $(cat key) -iv $(cat iv) -in syed.txt -out syed.txt.enc
```

#### Step 4: Decrypt the Message
**The OpenSSL command is:**
```bash
openssl enc -d -aes-256-cbc -K $(cat key) -iv $(cat iv) -in filename.enc -out filename.decrypt
```

**Result:**
```bash
┌──(adamriezqie㉿NWS23010043)-[~/Downloads]
└─$ openssl enc -d -aes-256-cbc -K $(cat key) -iv $(cat iv) -in syed.txt.enc -out syed.decrypt

┌──(adamriezqie㉿NWS23010043)-[~/Downloads]
└─$ cat syed.decrypt
kelisa putih nampak rare
```


#### Step 5: Verify the Decrypted Message



---

### Task 2: Asymmetric Encryption and Decryption using RSA

#### Step 1: Research how to generate an RSA private key of at least 2048 bits using `OpenSSL`.
#### Step 2: Research how to extract the corresponding public key from the private key using `OpenSSL`.
#### Step 3: Labu (simulated by you) encrypts a message (save it in `rahsia.txt`) using Labi's public key with `OpenSSL`.
#### Step 4: Labi (simulated by you) decrypts the ciphertext using his private key with `OpenSSL`.
#### Step 5: Verify that the decrypted message matches the original secret message.

---

### Task 3: Hashing and Message Integrity using SHA-256

#### Step 1: Create a text file (e.g., `<Your Name>.txt`) with some content.
#### Step 2: Research how to generate the SHA-256 hash of the document using `openssl`.
#### Step 3: Simulate a modification to the `<Your Name>.txt` file (e.g., change a single character).
#### Step 4: Generate the SHA-256 hash of the modified document using the same tool.
#### Step 5: Compare the two hash values and observe the difference. Explain what this demonstrates about

---

### Task 4: Digital Signatures using RSA

#### Step 1: Use the RSA private key generated in Task 2 (representing Labu's private key).
#### Step 2: Create a text file (e.g., `agreement.txt`) that Labu wants to sign.
#### Step 3: Research how to use `OpenSSL` to generate a digital signature for the `agreement.txt` file using Labu's private key and the SHA-256 hashing algorithm.
#### Step 4: Research how to use `OpenSSL` and Labu's public key (generated in Task 2) to verify the digital signature of the `agreement.txt` file.
#### Step 5: Simulate a modification to the `agreement.txt` file and attempt to verify the original signature. Observe the result and explain why it occurs.

---

### Analyze Problems Encountered

