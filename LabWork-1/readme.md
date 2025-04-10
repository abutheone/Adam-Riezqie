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
   python3 enum4linux-ng.py -A [target-ip]
   ```

   - Result:
       ```
      ========================================
      |    Users via RPC on 192.168.109.131    |
       ========================================
      [*] Enumerating users via 'querydispinfo'
      [+] Found 35 user(s) via 'querydispinfo'
      [*] Enumerating users via 'enumdomusers'
      [+] Found 35 user(s) via 'enumdomusers'
      [+] After merging user results we have 35 user(s) total:
      '1000':                                                                              
        username: root                                                                     
        name: root                                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1002':                                                                              
        username: daemon                                                                   
        name: daemon                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1004':                                                                              
        username: bin                                                                      
        name: bin                                                                          
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1006':                                                                              
        username: sys                                                                      
        name: sys                                                                          
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1008':                                                                              
        username: sync                                                                     
        name: sync                                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1010':                                                                              
        username: games                                                                    
        name: games                                                                        
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1012':                                                                              
        username: man                                                                      
        name: man                                                                          
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1014':                                                                              
        username: lp                                                                       
        name: lp                                                                           
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1016':                                                                              
        username: mail                                                                     
        name: mail                                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1018':                                                                              
        username: news                                                                     
        name: news                                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1020':                                                                              
        username: uucp                                                                     
        name: uucp                                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1026':                                                                              
        username: proxy                                                                    
        name: proxy                                                                        
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1066':                                                                              
        username: www-data                                                                 
        name: www-data                                                                     
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1068':                                                                              
        username: backup                                                                   
        name: backup                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1076':                                                                              
        username: list                                                                     
        name: Mailing List Manager                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1078':                                                                              
        username: irc                                                                      
        name: ircd                                                                         
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1082':                                                                              
        username: gnats                                                                    
        name: Gnats Bug-Reporting System (admin)                                           
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1200':                                                                              
        username: libuuid                                                                  
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1202':                                                                              
        username: dhcp                                                                     
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1204':                                                                              
        username: syslog                                                                   
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1206':                                                                              
        username: klog                                                                     
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1208':                                                                              
        username: sshd                                                                     
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1210':                                                                              
        username: bind                                                                     
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1212':                                                                              
        username: postfix                                                                  
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1214':                                                                              
        username: ftp                                                                      
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1216':                                                                              
        username: postgres                                                                 
        name: PostgreSQL administrator,,,                                                  
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1218':                                                                              
        username: mysql                                                                    
        name: MySQL Server,,,                                                              
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1220':                                                                              
        username: tomcat55                                                                 
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1222':                                                                              
        username: distccd                                                                  
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1224':                                                                              
        username: telnetd                                                                  
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '1226':                                                                              
        username: proftpd                                                                  
        name: (null)                                                                       
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '3000':                                                                              
        username: msfadmin                                                                 
        name: msfadmin,,,                                                                  
        acb: '0x00000010'                                                                  
        description: (null)                                                                
      '3002':                                                                              
        username: user                                                                     
        name: just a user,111,,                                                            
        acb: '0x00000010'                                                                  
        description: (null)                                                                
      '3004':                                                                              
        username: service                                                                  
        name: ',,,'                                                                        
        acb: '0x00000011'                                                                  
        description: (null)                                                                
      '501':                                                                               
        username: nobody                                                                   
        name: nobody                                                                       
        acb: '0x00000011'                                                                  
        description: (null)
      ```
       > You can run ```python3 enum4linux-ng.py -A [target-ip] | grep "username" | sed 's/username: //'``` to ```grep``` username only.
