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

**Steps:**

#### 1. **Scan for Services:**
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


#### 2. **Connect to the Database:**
- Attempted to connect to the MySQL and PostgreSQL targets using [common database username](/Cryptography-Class/Notes/Others/Database%20Notes.md#common-database-usernames):
  - ##### **MySQL:**

    ```sh
    mysql -h <targe-ip> -u <username> -p 
    ```

    ```sh
    ┌──(adamriezqie㉿NWS23010043)-[~]
    └─$ mysql -h 192.168.109.131 -u root -p             
    Enter password: 
    ERROR 2026 (HY000): TLS/SSL error: wrong version number
    ```

  - ##### **PostgreSQL:**

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
  
#### 3. **Analyze Connection Issues:**
  > During the connection attempts to both MySQL and PostgreSQL services, errors occurred due to TLS/SSL protocol mismatches. PostgreSQL also rejected the login due to incomplete password authentication.

- ##### **Fix for MySQL SSL Error:**
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

- ##### **Fix for PostgreSQL SSL:**
  - **Problem:**
    ```
    psql: error: connection to server at "192.168.109.131", port 5432 failed: SSL error: unsupported protocol
    ```
    > This mean, I attempted to use SSL (by default) but the server doesn't support it.
  
  - **Solution:** 
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

**Steps:**
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
> Going through all the databases and tables, I found several hash that catch my eyes.

#### Password Hash Discovery 
**1. DVWA:**

```
MySQL [tikiwiki195]> use dvwa
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed
```

```
MySQL [dvwa]> show tables;
+----------------+
| Tables_in_dvwa |
+----------------+
| guestbook      |
| users          |
+----------------+
2 rows in set (0.001 sec)
```

```
MySQL [dvwa]> select * from users;
+---------+------------+-----------+---------+----------------------------------+-------------------------------------------------------+
| user_id | first_name | last_name | user    | password                         | avatar                                                |
+---------+------------+-----------+---------+----------------------------------+-------------------------------------------------------+
|       1 | admin      | admin     | admin   | 5f4dcc3b5aa765d61d8327deb882cf99 | http://172.16.123.129/dvwa/hackable/users/admin.jpg   |
|       2 | Gordon     | Brown     | gordonb | e99a18c428cb38d5f260853678922e03 | http://172.16.123.129/dvwa/hackable/users/gordonb.jpg |
|       3 | Hack       | Me        | 1337    | 8d3533d75ae2c3966d7e0d4fcc69216b | http://172.16.123.129/dvwa/hackable/users/1337.jpg    |
|       4 | Pablo      | Picasso   | pablo   | 0d107d09f5bbe40cade3de5c71e9e9b7 | http://172.16.123.129/dvwa/hackable/users/pablo.jpg   |
|       5 | Bob        | Smith     | smithy  | 5f4dcc3b5aa765d61d8327deb882cf99 | http://172.16.123.129/dvwa/hackable/users/smithy.jpg  |
+---------+------------+-----------+---------+----------------------------------+-------------------------------------------------------+
5 rows in set (0.001 sec)
```

**2. tikiwiki195:**
```
MySQL [tikiwiki195]> show databases;
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
MySQL [tikiwiki195]> use tikiwiki195;
```

```
MySQL [tikiwiki195]> show tables;
+------------------------------------+
| Tables_in_tikiwiki195              |
+------------------------------------+
| galaxia_activities                 |
| galaxia_activity_roles             |
| ...                                |
| ...                                |
| ...                                |
| users_usergroups                   |
| users_users                        |
+------------------------------------+
```

```
MySQL [tikiwiki195]> select * from users_users;
+--------+-------+-------+----------+----------+---------------+------------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+
| userId | email | login | password | provpass | default_group | lastLogin  | currentLogin | registrationDate | challenge | pass_due | hash                             | created | avatarName | avatarSize | avatarFileType | avatarData | avatarLibName | avatarType | score |
+--------+-------+-------+----------+----------+---------------+------------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+
|      1 |       | admin | admin    | NULL     | NULL          | 1271712540 |   1271712540 |             NULL | NULL      |     NULL | f6fdffe48c908deb0f4c3bd36c032e72 |    NULL | NULL       |       NULL | NULL           | NULL       | NULL          | NULL       |     0 |
+--------+-------+-------+----------+----------+---------------+------------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+
1 row in set (0.001 sec)
```

```
MySQL [tikiwiki195]> select userId, login, password, hash from users_users;
+--------+-------+----------+----------------------------------+
| userId | login | password | hash                             |
+--------+-------+----------+----------------------------------+
|      1 | admin | admin    | f6fdffe48c908deb0f4c3bd36c032e72 |
+--------+-------+----------+----------------------------------+
1 row in set (0.001 sec)
```

##### Table with Hash found:
**From users.DVWA database:**
| User    | Hash Password                    |
| ------- | -------------------------------- |
| admin   | 5f4dcc3b5aa765d61d8327deb882cf99 |
| gordonb | e99a18c428cb38d5f260853678922e03 |
| pablo   | 0d107d09f5bbe40cade3de5c71e9e9b7 |
| 1337    | 8d3533d75ae2c3966d7e0d4fcc69216b |
| smithy  | 5f4dcc3b5aa765d61d8327deb882cf99 |

**From users_users.tikiwiki195 database:**
| login | Password | Hash                             |
| ----- | -------- | -------------------------------- |
| admin | admin    | f6fdffe48c908deb0f4c3bd36c032e72 |

---

##### list of hash found:
```
5f4dcc3b5aa765d61d8327deb882cf99
e99a18c428cb38d5f260853678922e03
8d3533d75ae2c3966d7e0d4fcc69216b
0d107d09f5bbe40cade3de5c71e9e9b7
5f4dcc3b5aa765d61d8327deb882cf99
f6fdffe48c908deb0f4c3bd36c032e72
```
> save into hashes.txt

---
#### Hash Identification

**1. Identify the hash:**
> going through one by one using hash-identifier give result of MD5:

```
HASH: 5f4dcc3b5aa765d61d8327deb882cf99

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

```
HASH: e99a18c428cb38d5f260853678922e03

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

```
 HASH: 8d3533d75ae2c3966d7e0d4fcc69216b

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

`and so on...`

  ---
### 4. 🔨 Offline Hash Cracking

**🎯 Objective:** Crack the extracted hashes using tools like hashcat or john the ripper

**Cracck the hashes:**
```
└─$ john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
Using default input encoding: UTF-8
Loaded 5 password hashes with no different salts (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=6
Press 'q' or Ctrl-C to abort, almost any other key for status
password         (?)     
abc123           (?)     
letmein          (?)     
charley          (?)     
adminadmin       (?)     
5g 0:00:00:00 DONE (2025-04-25 11:22) 250.0g/s 18393Kp/s 18393Kc/s 18624KC/s alana11..acesso
Warning: passwords printed above might not be all those cracked
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed. 
```
  ---
### 5. 🔬 Cryptographic Analysis and Mitigation

**🎯 Objective:** Summarize cryptographic issues and propose secure alternatives.

#### Summary of Issues

- **Authentication Flaws:** No passwords required for MySQL access.
- **Weak Password Hashing:** MD5 without salting.
- **Data Transmission:** Unencrypted due to disabled SSL.

#### Proposed Mitigations

- **Authentication:** Enforce strong, unique passwords; consider multi-factor authentication.
- **Hashing:** Use bcrypt, scrypt, or Argon2 with salting.
- **Transmission:** Enable SSL/TLS for encrypted connections.

---
## References
[MySQL: 4.2.3 Command Options for Connecting to the Server](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl)
