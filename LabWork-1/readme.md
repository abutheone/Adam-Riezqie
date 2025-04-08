# Lab 1: Cryptographic Attacks: Brute Force and Traffic Analysis on Network Protocols

## 🎯 Objective
The goal of this lab is to explore the vulnerabilities of common network protocols (FTP, TELNET, SSH, HTTP) by performing brute force attacks to recover passwords and then using those credentials to sniff network traffic. Will also analyze the security of these protocols and propose mitigation strategies.

---

## 🛠️ Tools Used

- Kali Linux
- Metasploitable 2
- Nmap
- Hydra

---

## 🔍 Lab Tasks

### 1. Enumerate the Vulnerable VM to Discover Usernames

#### ✅ Objective:
- Identify potential usernames for brute force attacks.
- Document the usernames found.

#### 🔧 Steps Taken:

- Performed a port scan using Nmap:
  ```
  nmap -sV -p 21,23,22,80 [target-ip]
  ```
  ![image](https://github.com/user-attachments/assets/2c34570b-4073-4b21-82e7-e24b5da34909)

- Connected manually to Telnet to observe any information:
  ```
  telnet [target-ip]
  ```
  ![image](https://github.com/user-attachments/assets/3c80d78e-9904-4c9d-a4ab-e29bcb667df0)
  > Here we got the username and password: ```msfadmin:msfadmin```. Bear in mind, we often do not get the credentials as easily as this.


---
### 2.  Perform Brute Force Attacks
#### 2.1. FTP, TELNET, and SSH
- Use Hydra perform brute force attacks against the following protocols:
- FTP
  ```
  hydra -L rockyou.txt -P rockyou.txt ftp://[target-ip]
  ```
  ![image](https://github.com/user-attachments/assets/136b15fc-d644-4f87-b0c3-ba123adb8c57)
  
- TELNET
  ```
  hydra -L rockyou.txt -P rockyou.txt telnet://[target-ip]
  ```
  ![image](https://github.com/user-attachments/assets/5ba8dca6-6fd2-48b3-86a8-adedb3d78b46)



