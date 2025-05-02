# Lab 3: Hands-on Exploration of Cryptographic Tools: Hashing, Encryption, and Digital Signatures

**🎯 Lab Objective:**
In this lab, we’ll explore the basics of cryptography using **OpenSSL**, a powerful and widely-used command-line toolkit for cryptographic operations.

- We'll go through the following tasks **step-by-step**:
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

### 🔐 Task 1: Symmetric Encryption and Decryption using AES-256-CBC
**🎯 Objective:** In this task, we (me and [Syed](https://github.com/yed-0)) will simulate how to send a confidential message securely using symmetric encryption. We’ll use the AES-256-CBC encryption algorithm in OpenSSL to encrypt and decrypt a message.

<div style="display: flex; justify-content: center; margin-top: 20px;">
  <div style="font-family: monospace; background-color: #0d1117; color: #c9d1d9; padding: 8px 12px; border-radius: 6px;">
    <a href="https://github.com/yed-0" target="_blank" style="color: #58a6ff; text-decoration: none;">syed</a>
    --[confidential 📨]--> 
    <a href="https://github.com/abutheone" target="_blank" style="color: #58a6ff; text-decoration: none;">me</a>
  </div>
</div>

---


#### 🔍 Step 1: Research how to generate a strong, random key using `OpenSSL`.

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
#### ✉️ Step 2: Create a Message to Encrypt
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
#### 🔐Step 3: Encrypt the Message Using AES-256-CBC
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
**Command:**
```bash
ll filename.txt filename.decrypt
diff filename filename.decrypt
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ ll syed.txt syed.decrypt
-rw-rw-r-- 1 syed syed 25 May  2 00:53 syed.decrypt
-rw-rw-r-- 1 syed syed 25 May  2 00:05 syed.txt

┌──(syed㉿NWS23010037)-[~]
└─$ diff syed.txt syed.decrypt

┌──(syed㉿NWS23010037)-[~]                                      
└─$ 
```



---

### Task 2: Asymmetric Encryption and Decryption using RSA

#### Step 1: Generate an RSA private key (2048-bit)

**Command:**
```bash
openssl genpkey -algorithm RSA -out filename -pkeyopt rsa_keygen_bits:2048
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ openssl genpkey -algorithm RSA -out private.key  -pkeyopt rsa_keygen_bits:2048
..+..+....+.........+............+++++++++++++++++++++++++++++++++++++++*........+.......+...........+.......+...+..+.......+++++++++++++++++++++++++++++++++++++++*..+..........+.........+...........+.......+..+.........+.......+...+...............+..+............+.+......+....................+........................+.+...+..+...+...+...+.+...+...+...............+..+.....................+.+......+..+.+.........+....................+.+....................+...............+.......+..++++++
.+.+++++++++++++++++++++++++++++++++++++++*..........+..+.+..+...+.......+++++++++++++++++++++++++++++++++++++++*.......................+..+............+..................+.++++++

┌──(syed㉿NWS23010037)-[~]
└─$ cat private.key
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmoutBA9yAzo/L
YMyC3DzUrCHjfI8e4W48blXtn1MJDPdk3/ybWA6egMv7wF8zZubmlkoFB9P19XsW
dnegy2QyVChzW5+ny4FFKUXYVaMYk/pWcnVV1UB2P+IYXB6gJ/NX+jIoCOeTsXOY
sdWMiozIxvVpCn1hQQb68x2W8tqOg+Bb4sKpIgL0tXDkqWiRpyJnJXosiy836rW5
74kNyyMc4iiRms71lj8urEyN9MyQ364xko7DJFfCpBJ1ABh2yvDbIoF54q+CDpL8
Zg0DA4T83Dp2MLCAYWKdWBCeXjrlOrKdP4YY0EPsLRvjpL/V10ShG6iamGS2jj4L
FY0ShcPrAgMBAAECggEAIM3CvTZK4sqHMTTZnctIaF+IflWHgT9Eqb3YyaILQSVd
0GxtuJERs69MOL+qnh5cRzl/0dS0K9/K/uWMcEmJ7IR3wBnh6LDdvmU9HDTjmhOL
fRgkNCT6fyzdUAlWeBXVSFT3Kb1zBTayOHWNwhCGXYIZTrfjbdFU0/MnOI+Pae2H
lW3NSSo1FUPbdCbyZSA0NOo/qQSyVzOnB/V6ZK4klKFVaEKCv4g1XanaG+m4Z9HX
Pmq1DyuVe3scrBGThxfdalLc1NShCQFZ0Uv8Vn7nt8bST3og1rDUvQyMRX35V9P3
R01sjEDxhkbNZri3Hhb2uFMd8TNWRb+2uTNpSR4TuQKBgQDgRM121VP+BnG1q9MU
Yf/FxpfMhKrMjzWbsNfBe+m1jSZf59IdZUZyjsQXWQvtOOzwr1QPgk/PBPi/MfOg
Kko1wdlS4/tcL+bTwAxZSfmuS94O9NZVug5c5KC8VoYkLTT1kBxabIuXM1Wl3PF9
Cd8ln6z0SkvdokMYuHpFNDfNMwKBgQC+NqAXX7w8Ph9dhlrB/nOx44Dg2rxu7H11
Uca+vyQVjcpoOd9+Huv2iOzJPM93r0pp7ShGFsfhpQXVn+M3EpqntXEpbrwpEsAV
JD7Xo2zKKsQ1M9GphhwwRsiqU9gSeffi3bgm93ja+IzHmU4s+87pZRr2isofTOy8
KIcNKc7+aQKBgQCeHiQ2ikWDrgtxqMlTb5yjVlckLM03GCkVseMMWU73X6MUrx8m
9oZqsllylKeiAyaasyKzJI8cSEcQlilMXUShDiEpHe/UmTlHRfnu4gcVagwPw3Ny
UZFa0R66as58pxrVn1s+LZVlbx4NqO7h15nqrt+EBPXkN0jTHw2lySEmnQKBgBsG
5/hqQfTNXueLD5pA7W95Q/avHdclAy6IUBUKU7Y8T2Y/0uG4ww5kpkBxw4jd/1TN
vcs3sW7+Y7XW4hIRMqhhv5KDiXjMkT5vx/4b2nlfWkG0+zV7OMYjSJ/rCeiWLAKw
PlpLD4ENj/NMdS8vGFdRZmNhlRadd4XEvGvCZQcBAoGAFHtrYMIaGgRMz7b8tKRJ
BbABKXcM3JkpUmHb3j0WlMX1wUpF21V1l1XUtnAW/Q0USwvMClgGnnkEvth/lkA7
9ANRgsB5Fsg/EjUIXVZZ8Rs3rNSeTAsny7vyHpGyn3zsBizUsVVq+NOEOmSfEusr
yiCkQ3SgWYY2hAfUJ0oPr10=
-----END PRIVATE KEY-----
```


#### Step 2: Extract the public key

**Command:**
```bash
 openssl rsa -in filename -pubout -out filename
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]                                                                                          
└─$ openssl rsa -in private.key -pubout -out public.key                                                             
writing RSA key

┌──(syed㉿NWS23010037)-[~]
└─$ cat public.key
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApqLrQQPcgM6Py2DMgtw8
1Kwh43yPHuFuPG5V7Z9TCQz3ZN/8m1gOnoDL+8BfM2bm5pZKBQfT9fV7FnZ3oMtk
MlQoc1ufp8uBRSlF2FWjGJP6VnJ1VdVAdj/iGFweoCfzV/oyKAjnk7FzmLHVjIqM
yMb1aQp9YUEG+vMdlvLajoPgW+LCqSIC9LVw5KlokaciZyV6LIsvN+q1ue+JDcsj
HOIokZrO9ZY/LqxMjfTMkN+uMZKOwyRXwqQSdQAYdsrw2yKBeeKvgg6S/GYNAwOE
/Nw6djCwgGFinVgQnl465TqynT+GGNBD7C0b46S/1ddEoRuomphkto4+CxWNEoXD
6wIDAQAB
-----END PUBLIC KEY-----
```


#### Step 3: Encrypt a message using the public key`OpenSSL`.

**First, generate the secret message:**
```bash
┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ echo "hi syed, long time no see... here secret message for you :143" > secret.txt
```

**Encrypt a message:**
```bash
┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ openssl pkeyutl -encrypt -inkey public.key -pubin -in secret.txt -out secret.enc

┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ cat secret.enc  
�HV▒$�$
       0���f�7,b�����6�U��g����wz4��������▒���[��{r��"�.�~���A��㛌�ᠮ{�k2J��o�E��=1N�{�x'��+[UN�����*���&I���#;3�6����|Y���J6�\$}E�~N���{4C5NaJsT�s�����-SF#���Jj��&�ZF��n;�5}����ܗ�Ma&o+��&�_H���.�
                         I��nڇ�#*��ī�!�S����r�I���<   
```

#### Step 4: Decrypt using the private key.
**Command:**
```bash
openssl pkeyutl -decrypt -inkey filename -in filename -out filename
```

**Result:**
```bash
┌──(syed㉿NWS23010037)-[~]
└─$ openssl pkeyutl -decrypt -inkey private.key -in secret.enc -out secret.decrypt

┌──(syed㉿NWS23010037)-[~]
└─$ cat secret.decrypt                                                                                              
hi syed, long time no see... here secret message for you :143
```

#### Step 5: Verify the decrypted message matches the original.

**Command:**
```bash
cat secret.decrypt secret.txt
ll secret.decrypt secret.txt
diff secret.decrypt secret.txt
```

**Result:**
```bash
                                                                                     
┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ cat secret.decrypt secret.txt
hi syed, long time no see... here secret message for you :143
hi syed, long time no see... here secret message for you :143
                                                                                     
┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ ll secret.decrypt secret.txt
-rw-rw-r-- 1 adamriezqie adamriezqie 62 May  2 14:22 secret.decrypt
-rw-rw-r-- 1 adamriezqie adamriezqie 62 May  2 13:30 secret.txt
                                                                                     
┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ diff secret.decrypt secret.txt
                                                                                     
┌──(adamriezqie㉿NWS23010043)-[~/Downloads/task-2]
└─$ 
```



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

