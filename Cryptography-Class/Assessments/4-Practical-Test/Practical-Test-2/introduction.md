# Introduction

## 📌 Scenario

🔐 Ransomware is a malicious real-world application of cryptography. In this exercise, you will act as a cryptography and malware reverse engineer, tasked with analyzing a suspicious binary that simulates ransomware behavior. Your job is to analyze, extract, and break the cryptography used in this malware, and then write a decryption script to recover the victim's files, and save the world.

---
## ⚠️ Important Notes

- This is NOT real ransomware. It is a simulated binary created for educational purposes only.
- However, it mimics real cryptographic behavior used in ransomware.
- Even though it's safe, please use secure practices:
- Analyze it in a dedicated VM or sandbox environment.
- Avoid running unknown ".exe" directly on your host OS.

---

## 🎯 Your Tasks

1. Static Analysis and Reverse Engineering
2. Identify the programming language or packaging tool used.
3. Reverse engineer the binary to recover the source
4. Identify the encryption algorithm and mode used.
5. Recover the encryption key.
6. Analyze cryptographic implementation
7. Describe any flaws, and misuse of cryptography in the binary.

8. Decryption Tool Development (Recover the Victim Files)

Use your understanding to write a working Python script (decrypt.py):

1. Uses the extracted key, algorithm, and mode.
2. Correct key, padding, IV, etc.
3. Correctly decrypts the .enc files
4. and recover the original plaintext

3. Flaw Analysis

1. Explain how and why the cryptography used in the ransomware is flawed.
2. Suggest what a more secure version of encryption could look like.

---

## 📂 Deliverables

Push the following to your public GitHub repo:

| File           | Description                                   |
| -------------- | --------------------------------------------- |
| `analysis.md`  | Static & dynamic analysis, key recovery steps |
| `decrypt.py`   | Script to decrypt `.enc` files                |
| `screenshots/` | Evidence of decryption and analysis           |
| `decrypted/`   | Folder showing decrypted output               |
| `README.md`    | Link to report, and tool references           |

---

## 📤 Submission Instructions

1. Push your walkthrough, code files, and screenshots to your GitHub repository.
2. Submit the repo link in the Google Classroom comment section.
3. Show and run your decryptor script to the instructor to prove it works!
4. Attendance is compulsory; no marks will be awarded for no-shows.
5. Marks will be deducted for incomplete, broken, or undocumented tasks.