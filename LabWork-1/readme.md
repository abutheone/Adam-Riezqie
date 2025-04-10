# Lab 1: Cryptographic Attacks: Brute Force and Traffic Analysis on Network Protocols

## 🎯 Objective

1. Explore **vulnerabilities** in common network protocols (FTP, TELNET, SSH & HTTP).
3. Perform brute force attacks to recover passwords.
4. Use recovered credentials to sniff network traffic.
5. Analyze the security posture of each protocol.
6. Propose effective mitigation strategies.
---

## 🛠️ Requirement

| Tool               | Purpose                        |
|--------------------|--------------------------------|
| Kali Linux         | Attacker machine               |
| Metasploitable 2   | Target/vulnerable machine      |
| Wordlist           | Password brute-forcing         |
| Nmap               | Port scanning                  |
| Hydra              | Brute force tool               |
| Burp Suite         | HTTP interception & testing    |
---

## 🔍 Lab Tasks

### Task 1: Enumerate the Vulnerable VM to Discover Usernames

#### ✅ Objective:
- Identify potential usernames for brute force attacks.

#### 🚶‍♂️‍➡️ The Process:

1. Performed a port scan using Nmap:
   
    ```
    nmap -sV -p 21,23,22,80 [target-ip]
    ```
    | Option              | Meaning                                                                                                                                       |
   |---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
   | `nmap`              | Runs the Nmap network scanner tool.                                                                                                           |
   | `-sV`               | **Service/version detection** — Nmap will try to determine what software and version is running on each open port.                          |
   | `-p 21,23,22,80`    | Tells Nmap to scan **only** these specific ports: <br>• `21` = FTP <br>• `23` = Telnet <br>• `22` = SSH <br>• `80` = HTTP                    |
   | `[target-ip]`       | Replace with the IP address of the target/vulnerable machine you are scanning.

   ![image](nmap-scan-open-port-on-target-machine.png)
   > Here I only scan FTP(21), TELNET(23), SSH(22) and HTTP(80) port.

3. Connected manually to Telnet to observe any information:
  ```
  telnet [target-ip]
  ```
  ![image](telnet-to-target-machine.png)
  > Here we got the username and password: ```msfadmin:msfadmin```. Bear in mind, we often do not get the credentials as easily as this.


---
### 2.  Perform Brute Force Attacks
#### 2.1. FTP, TELNET, and SSH

#### ✅ Objective:
- Use Hydra perform brute force attacks against the following protocols:

##### FTP
  ```
  hydra -L rockyou.txt -P rockyou.txt ftp://[target-ip]
  ```
  ![image](hydra-bruteforce-ftp.png)
  
##### TELNET
  ```
  hydra -L rockyou.txt -P rockyou.txt telnet://[target-ip]
  ```
  ![image](hydra-bruteforce-telnet.png)

#### 2.2. HTTP
> Since we know the target machine has port 80 open. We can use web browser to open it
![Screenshot 2025-04-08 190606](https://github.com/user-attachments/assets/852e982a-d46c-4da3-bd67-92e6ce375391)

- Here we got DVWA for testing
- ![image](https://github.com/user-attachments/assets/5af3a29e-51f3-4e4f-a8b7-59ff94b26aa9)

- Capure login form using BurpSuite
- ![image](https://github.com/user-attachments/assets/c129ff7a-a8e4-4ebc-bf20-d9a66da853de)

- Right click and send to intruder
- ![image](https://github.com/user-attachments/assets/7477905c-d3cf-4bc9-9e37-5a182966023d)

- Right click hightlight entered username and password and click on add payload position
- ![image](https://github.com/user-attachments/assets/7bea2c54-ae5b-4701-b75f-9d72c36e14dc)

- Load payload wordlist
- ![image](https://github.com/user-attachments/assets/298608c5-29ae-427e-80b9-88fc7828fed3)

- CLick Start Attack
- ![image](https://github.com/user-attachments/assets/d4fa653c-1d25-4956-9554-a6ec3ef77a9e)
