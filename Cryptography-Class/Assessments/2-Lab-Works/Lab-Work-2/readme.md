# Lab 2: Cryptographic Attacks: Cracking Weak Password Hashes and Exploiting Poor Authentication in Databases

**🎯 Main Objective:**
  1. Identify and exploit cryptographic weaknesses in database authentication and password storage.
  2. Perform offline hash cracking after discovering password hashes in a vulnerable database.
  3. Investigate real-world cryptographic failures and propose secure solutions.
  4. Document findings clearly in GitHub (Markdown) and present a short demo/brief.

---

## 💼 Lab Tasks:

### 1. 🖥️ Service Enumeration and Initial Access

**🎯 Objective:** Identify the database service on the target, connect to it from Kali Linux, and analyze any connection issues.

#### Steps:

1. **Scan for Services:**
   - Used [`nmap`](/Cryptography-Class/Notes/Others/nmap_options_notes.md#-sv) to scan the target for open ports, focusing on [common database ports](/Cryptography-Class/Notes/Others/Database%20Notes.md#common-database-ports):
     
     ```sh
     nmap -sV -p 1433,1521,3306,5432,27017 <target-ip>
     ```

     ```sh
     ┌──(adamriezqie㉿NWS23010043)-[~]
     └─$ nmap -sV -p 1433,1521,3306,5432,27017 192.168.109.131
     Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-25 04:24 +08
     Nmap scan report for 192.168.109.131
     Host is up (0.00050s latency).

     PORT      STATE  SERVICE    VERSION
     1433/tcp  closed ms-sql-s
     1521/tcp  closed oracle
     3306/tcp  open   mysql      MySQL 5.0.51a-3ubuntu5
     5432/tcp  open   postgresql PostgreSQL DB 8.3.0 - 8.3.7
     27017/tcp closed mongod
     MAC Address: 00:0C:29:3C:0A:2B (VMware)

     Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
     Nmap done: 1 IP address (1 host up) scanned in 6.43 seconds
     ```
     > After scanning, we know at least two database service port is open: **MySQL** running on port 3306 and **PostgreSQL** running on port 5432
     ---


2. **Connect to the Database:**
   - Attempted to connect to the MySQL and PostgreSQL targets using [common database username](/Cryptography-Class/Notes/Others/Database%20Notes.md#common-database-usernames):
     - **MySQL:**

       ```sh
       mysql -h <targe-ip> -u <username> -p 
       ```

       ```sh
       ┌──(adamriezqie㉿NWS23010043)-[~]
       └─$ mysql -h 192.168.109.131 -u root -p             
       Enter password: 
       ERROR 2026 (HY000): TLS/SSL error: wrong version number
       ```

     - **PostgreSQL:**

       ```sh
       psql -h <targe-ip> -p 5432 -U <username>
       ```

       ```sh
       ┌──(adamriezqie㉿NWS23010043)-[~]
       └─$ psql -h 192.168.109.131 -p 5432 -U postgres                                      
       Password for user postgres: 
       psql: error: connection to server at "192.168.109.131", port 5432 failed: SSL error: unsupported protocol
       This may indicate that the server does not support any SSL protocol version between TLSv1.2 and TLSv1.3.
       connection to server at "192.168.109.131", port 5432 failed: fe_sendauth: no password supplied
       ```
       > The PostgreSQL connection fails due to both an SSL protocol mismatch and missing password. PostgreSQL 8.3 doesn’t support modern TLS versions, causing SSL negotiation to fail unless disabled manually
       ---
  

  3. **Analyze Connection Issues:**
      > During the connection attempts to both MySQL and PostgreSQL services, errors occurred due to TLS/SSL protocol mismatches. PostgreSQL also rejected the login due to incomplete password authentication.

      - **Fix for MySQL SSL Error:**
        - **Problem:**
          ```
          ERROR 2026 (HY000): TLS/SSL error: wrong version number
          ``` 
          > This indicates the client tried to connect with SSL/TLS, but the server (MySQL 5.0.51a) does not support the version or SSL at all.

        - **Solution:** Disable SSL in the client using the legacy-compatible option:
  
          ```
          mysql -h 192.168.109.131 -u root -p --ssl=0
          ```

          ```
          ┌──(adamriezqie㉿NWS23010043)-[~]
          └─$ mysql -h 192.168.109.131 -u root -p --ssl=0
          Enter password: 
          Welcome to the MariaDB monitor.  Commands end with ; or \g.
          Your MySQL connection id is 33
          Server version: 5.0.51a-3ubuntu5 (Ubuntu)

          Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

          Support MariaDB developers by giving a star at https://github.com/MariaDB/server
          Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

          MySQL [(none)]> show DATABASES;
          +--------------------+
          | Database           |
          +--------------------+
          | information_schema |
          | dvwa               |
          | metasploit         |
          | mysql              |
          | owasp10            |
          | tikiwiki           |
          | tikiwiki195        |
          +--------------------+
          7 rows in set (0.005 sec)

          MySQL [(none)]> 

          ```
          > This allowed a successful connection to the MySQL server.
        ---
      
      - **Fix for PostgreSQL SSL + Authentication Error:**
        - **Problem:**
          ```
          psql: error: connection to server at "192.168.109.131", port 5432 failed: SSL error: unsupported protocol
          ...
          connection to server at "192.168.109.131", port 5432 failed: fe_sendauth: no password supplied
          ```

          This means:
          - The client attempted to use SSL (by default) but the server doesn't support it.
          - After retrying in non-SSL mode, authentication failed due to a missing password.
        
        - **Solution:** 
          
          Use environment variable `PGPASSWORD` to pass the password and explicitly disable SSL:

          ```
          PGPASSWORD=postgres psql -h 192.168.109.131 -p 5432 -U postgres "sslmode=disable"
          ```

          ```
          ┌──(adamriezqie㉿NWS23010043)-[~]
          └─$ PGPASSWORD=postgres psql -h 192.168.109.131 -p 5432 -U postgres "sslmode=disable"
          psql (17.4 (Debian 17.4-1+b1), server 8.3.1)
          WARNING: psql major version 17, server major version 8.3.
                  Some psql features might not work.
          Type "help" for help.

          postgres=# SELECT datname FROM pg_database;
            datname  
          -----------
          template1
          template0
          postgres
          (3 rows)

          postgres=# 
          ```



  ---
### 2. 👤 Enumeration of Users and Authentication Weakness

**🎯 Objective:** Enumerate database users and identify those with cryptographic authentication flaws.
> I narrow down for MySQL only, but in my free time I will cover PostgreSQL also.

#### Steps:
**1. List Users:**
   - Queried the database to list users step-by-step:

     ```
     MySQL [(none)]> show DATABASES;
     +--------------------+
     | Database           |
     +--------------------+
     | information_schema |
     | dvwa               |
     | metasploit         |
     | mysql              |
     | owasp10            |
     | tikiwiki           |
     | tikiwiki195        |
     +--------------------+
     7 rows in set (0.001 sec)
     ```

     ```
     MySQL [(none)]> use mysql
     Reading table information for completion of table and column names
     You can turn off this feature to get a quicker startup with -A

     Database changed
     MySQL [mysql]> show TABLES;
     +---------------------------+
     | Tables_in_mysql           |
     +---------------------------+
     | columns_priv              |
     | db                        |
     | func                      |
     | help_category             |
     | help_keyword              |
     | help_relation             |
     | help_topic                |
     | host                      |
     | proc                      |
     | procs_priv                |
     | tables_priv               |
     | time_zone                 |
     | time_zone_leap_second     |
     | time_zone_name            |
     | time_zone_transition      |
     | time_zone_transition_type |
     | user                      |
     +---------------------------+
     17 rows in set (0.001 sec)
     ```

     ```
     MySQL [mysql]> SELECT * FROM user;
     +------+------------------+----------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--
     | Host | User             | Password | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Reload_priv | Shutdown_priv | Process_priv | File_priv | Grant_priv | References_priv | Index_priv | Alter_priv | S
     +------+------------------+----------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--
     |      | debian-sys-maint |          | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y
     | %    | root             |          | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y
     | %    | guest            |          | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y
     +------+------------------+----------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--
     3 rows in set (0.001 sec) 
     ```
     
     ```
     MySQL [mysql]> SELECT User, Password FROM user;
     +------------------+----------+        
     | User             | Password |
     +------------------+----------+
     | debian-sys-maint |          |
     | root             |          |
     | guest            |          |
     +------------------+----------+
     3 rows in set (0.001 sec)

     MySQL [mysql]> 
     ```
      ---

**2. User with cryptographic authentication flaws:**
  - debian-sys-maint
  - root
  - guest

**3. Attempt to login**
   - debian-sys-maint:
      ```
      ┌──(adamriezqie㉿NWS23010043)-[~]
      └─$ mysql -h 192.168.109.131 -u debian-sys-maint -p --ssl=0  
      Enter password: 
      Welcome to the MariaDB monitor.  Commands end with ; or \g.
      Your MySQL connection id is 35
      Server version: 5.0.51a-3ubuntu5 (Ubuntu)

      Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

      Support MariaDB developers by giving a star at https://github.com/MariaDB/server
      Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

      MySQL [(none)]> ^DBye
      ``` 
   - guest:

      ```
      ┌──(adamriezqie㉿NWS23010043)-[~]
      └─$ mysql -h 192.168.109.131 -u guest -p --ssl=0
      Enter password: 
      Welcome to the MariaDB monitor.  Commands end with ; or \g.
      Your MySQL connection id is 36
      Server version: 5.0.51a-3ubuntu5 (Ubuntu)

      Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

      Support MariaDB developers by giving a star at https://github.com/MariaDB/server
      Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

      MySQL [(none)]> ^DBye
      ```
   
  ---
### 3. 🔑 Password Hash Discovery and Hash Identification

**🎯 Objective:** Locate tables with password hashes, extract them, and identify the hashing algorithm.

  ---
### 4. 🔨 Offline Hash Cracking

**🎯 Objective:** Crack the extracted hashes using tools like hashcat or john the ripper

  ---
### 5. 🔬 Cryptographic Analysis and Mitigation

**🎯 Objective:** Summarize cryptographic issues and propose secure alternatives.


---
## References
[MySQL: 4.2.3 Command Options for Connecting to the Server](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl)
