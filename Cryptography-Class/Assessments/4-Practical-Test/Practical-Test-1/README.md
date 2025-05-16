## Task 1: Generate Your GPG Key Pair

Objective: Use `gpg` to generate an RSA key pair tied to your identity.

- Input:

- Name: Your Name
- Email: Your academic email
- Key Type: RSA
- Key Size: 4096 bits
- Expiry: 1y

- Expected Output: GPG key fingerprint, with `gpg --list-keys` showing your identity.

## Task 2: Encrypt and Decrypt a File

Objective: Perform GPG encryption and decryption.

- Create a file `message.txt` containing:
`This file was encrypted by [Your Name] ([Your Student ID])`

- Encrypt `message.txt` using your own public key (for self-decryption).

- Decrypt the resulting file and verify the contents.

- Expected Output: Clear file content recovered.

## Task 3: Sign and Verify a Message

Objective: Digitally sign a message and verify its authenticity.

- Step A: Create a signed message file `signed_message.txt` that contains:
`I, [Your Name], declare this is my work.`

- Step B: Sign the file using GPG (`--clearsign` or `--detach-sign`)

- Step C: Verify your signature using `gpg --verify`

## Task 4: Configure Passwordless SSH Authentication

Objective: Set up SSH key-based login to a simulated server (or localhost if isolation is used).

- Generate an SSH key pair using your name and ID as comment.
`ssh-keygen -C "[Your Name]-[ID]"`

- Configure passwordless login to a test VM or localhost (`~/.ssh/authorized_keys`).

- Test authentication by logging in and creating a file `Your_Name.txt` containing “[Your_Student_ID]”

- Evidence Required:

- Show the SSH key comment in the public key.
- Show login command working without password.
- Screenshot of `ssh user@ssh-server "echo Your_Student_ID > Your_Name.txt"` from your local computer
- Screenshot of `whoami` from remote shell.

## Task 5: Hash Cracking Challenge

Objective: Crack provided hashes.

- Hashes Provided (Variety of types):

- SnZlcmV4IEF2IEpmcmNyZSBFeiBCcnJl
- 6283293831c84671546324c9373704ca
- 2bc92f33a2ede5ada3d65b468a81f617d0229d843d87c63313833e509e5a6782

- Expected Output:

- Plaintext value for each hash
- Tool/wordlist/method used for cracking
Submission Instructions

1. Push walkthrough, code files, and screenshots to your GitHub repository.
2. Submit the repo link in the Google Classroom comment section.
3. Attendance is compulsory; no marks for no-shows.
4. Marks deducted for incomplete tasks.