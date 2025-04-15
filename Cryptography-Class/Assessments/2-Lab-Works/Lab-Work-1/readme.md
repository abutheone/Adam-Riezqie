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
| enum4linux-ng      |                                |
---

## 🔥 Pre-Heat
Performed a port scan using Nmap:
   ```
   nmap -sV -p 21,23,22,80 [target-ip]
   ```
   | Option              | Meaning                                                                                                                                       |
   |---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
   | `nmap`              | Runs the Nmap network scanner tool.                                                                                                           |
   | `-sV`               | **Service/version detection** — Nmap will try to determine what software and version is running on each open port.                          |
   | `-p 21,23,22,80`    | Tells Nmap to scan **only** these specific ports: <br>• `21` = FTP <br>• `23` = Telnet <br>• `22` = SSH <br>• `80` = HTTP                    |
   | `[target-ip]`       | Replace with the IP address of the target/vulnerable machine you are scanning.

   - Result:
     ![image](https://github.com/user-attachments/assets/901e865f-eb77-4f8e-9f43-42515ba29026)
     > Here I only scan FTP(21), TELNET(23), SSH(22) and HTTP(80) port.
---

## 🔍 Lab Tasks

### Task 1: Enumerate the Vulnerable VM to Discover Usernames

#### ✅ Objective:
- Identify potential usernames for brute force attacks.
---

#### 🚶‍♂️‍➡️ The Process:
1. Create Python Virtual Environment:
   ```
   python3 -m venv crypto-Venv
   source crypto-Venv/bin/activate
   ```
   
2. Install enum4linux-ng:
   ```
      git clone https://github.com/cddmp/enum4linux-ng.git
      cd enum4linux-ng
      python3 -m pip install -r requirements.txt
   ```
   - Result:
     ![image](https://github.com/user-attachments/assets/b104cbfa-c729-45ae-a366-f0ae84834952)

3. Run the script:
   ```
   python3 enum4linux-ng.py -A [target-ip] | grep "username:" | sed 's/username: //' >> list-username.txt
   ```
   - Result:
      ```
      ┌──(abu㉿kali)-[~/enum4linux-ng]
      └─$ python3 enum4linux-ng.py -A 192.168.109.131 | grep "username:" | sed 's/username: //' >> list-username.txt

      ┌──(abu㉿kali)-[~/enum4linux-ng]
      └─$ cat list-username.txt
        root
        daemon
        bin
        sys
        sync
        games
        man
        lp
        mail
        news
        uucp
        proxy
        www-data
        backup
        list
        irc
        gnats
        libuuid
        dhcp
        syslog
        klog
        sshd
        bind
        postfix
        ftp
        postgres
        mysql
        tomcat55
        distccd
        telnetd
        proftpd
        msfadmin
        user
      ```
      > Here I execute the script and filter the output to extract lines containing username:. Then, I strip the username: prefix and save the resulting usernames to a file named list.username.txt.
      
      **Potential usernames for brute force attacks:**
         ```
            root
            ftp
            postgres
            mysql
            tomcat55
            proftpd
            msfadmin
            user
         ```

---

### Task 2: Perform Brute Force Attacks
#### 2.1: FTP, TELNET, and SSH
     
