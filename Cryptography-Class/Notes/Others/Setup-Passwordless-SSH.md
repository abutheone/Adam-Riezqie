## SSH From Laptop Windows to VM Kali Linux
---
1. **On your Windows Laptop, use PowerShell or CMD:**
```bash
ssh kali_user@<Kali_VM_IP>
```


## Setup Passwordless SSH (from Windows → Kali)
---
1. **On Windows, generate SSH keys:**
```bash
ssh-keygen
```

**Output:**
```
C:\>ssh-keygen
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\riezq/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase): 
Enter same passphrase again:
Your identification has been saved in C:\Users\riezq/.ssh/id_ed25519
Your public key has been saved in C:\Users\riezq/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:IxyyDzvIqYFhwU7ia5m5BRQ39p3z8sXqQ8DEqihzHbU riezq@X13
The key's randomart image is:
+--[ED25519 256]--+
| . +  .          |
|. + o oo.        |
|.=  .o==         |
|* . .=E+o .      |
|.=..+.o.S. o     |
|=+B+.+ .ooo      |
|+O+.o . .o       |
|.oo  .  ..       |
|..       ..      |
+----[SHA256]-----+
```

2. **Then, transfer the public key to Kali via scp:**

```bash
scp <public/key/path> <kali_user>@<Kali_VM_IP>:/home/<kali_user>/.ssh/authorized_keys
```

3. **Verify Password Less:**
```bash
ssh kali_user@<Kali_VM_IP>
```


