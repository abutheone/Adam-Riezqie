# Lab 1: Cryptographic Attacks: Brute Force and Traffic Analysis on Network Protocols

## 🎯 Objective
The goal of this lab is to explore the vulnerabilities of common network protocols (FTP, TELNET, SSH, HTTP) by performing brute force attacks to recover passwords and then using those credentials to sniff network traffic. Will also analyze the security of these protocols and propose mitigation strategies.

---

## 🛠️ Tools Used

- Kali Linux
- Metasploitable 2
- Nmap

---

## 🔍 Lab Tasks

### 1. Enumerate the Vulnerable VM to Discover Usernames

#### ✅ Objective:
- Identify potential usernames for brute force attacks.
- Document the usernames found.

#### 🔧 Steps Taken:

- Performed a port scan using Nmap:
  ```nmap -sV -p 21,23,22,80 [target-ip]```
![image](https://github.com/user-attachments/assets/2c34570b-4073-4b21-82e7-e24b5da34909)

- Connected manually to services like FTP and Telnet to observe any banner or prompt information:
```
ftp [target-ip]
telnet [target-ip]
```
![image](https://github.com/user-attachments/assets/3c80d78e-9904-4c9d-a4ab-e29bcb667df0)
> Here we got username and password is ```msfadmin:msfadmin```. Bare in mind, often we not get the password as easy as this.


---
### 2.  Perform Brute Force Attacks
