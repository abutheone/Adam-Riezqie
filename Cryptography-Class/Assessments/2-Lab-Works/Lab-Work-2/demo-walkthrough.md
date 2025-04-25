# Cryptographic Attacks Demo Walkthrough

This document provides a brief walkthrough for a class demo based on the lab report "[Lab 2: Cryptographic Attacks: Cracking Weak Password Hashes and Exploiting Poor Authentication in Databases.](/Cryptography-Class/Assessments/2-Lab-Works/Lab-Work-2/readme.md)" The demo is designed to be humorous and appealing to a Gen Z audience while remaining professional, with an estimated duration of 8-10 minutes.

## Introduction (1 minute)

Hey class, welcome to our demo on Lab 2: Cryptographic Attacks! Today, we’re diving into the world of ethical hacking. We’ll scan databases, crack weak passwords, and learn how to secure systems—all in a fun, legal way. Think of us as cyber detectives solving a digital mystery. Ready? Let’s go!

## Service Enumeration and Initial Access (2 minutes)

First, we need to scope out our target, like using digital binoculars. We use a tool called `nmap` to scan for database services on the target IP (192.168.109.131). The command is:

```bash
nmap -sV -p 1433,1521,3306,5432,27017 192.168.109.131
```

This reveals MySQL running on port 3306 and PostgreSQL on port 5432. When we try to connect, it’s like the database says, “Prove yourself!” But we hit SSL/TLS errors. For MySQL, we disable SSL with:

```bash
mysql -h 192.168.109.131 -u root -p --ssl=0
```

For PostgreSQL, we use:

```bash
PGPASSWORD=postgres psql -h 192.168.109.131 -p 5432 -U postgres "sslmode=disable"
```

Once connected, we list the databases with `show DATABASES;` for MySQL and `SELECT datname FROM pg_database;` for PostgreSQL. Boom, we’re in!

## User Enumeration and Authentication Weakness (2 minutes)

Now, in MySQL, we check the `user` table to see who’s got access. We run:

```sql
use mysql;
SELECT User, Password FROM user;
```

Shockingly, users like `root` and `guest` have *no passwords*! It’s like finding a treasure chest without a lock. We test this by logging in:

```bash
mysql -h 192.168.109.131 -u guest -p --ssl=0
```

No password needed—yikes! This isn’t a cryptographic issue per se, but it’s a massive security fail, like posting your address online and saying, “Come on in!”

## Password Hash Discovery and Identification (2 minutes)

Next, we hunt for password hashes in databases like `dvwa` and `tikiwiki195`. In `dvwa`, we run:

```sql
use dvwa;
select * from users;
```

We find hashes like `5f4dcc3b5aa765d61d8327deb882cf99`. In `tikiwiki195`, we use:

```sql
use tikiwiki195;
select userId, login, password, hash from users_users;
```

We get another hash: `f6fdffe48c908deb0f4c3bd36c032e72`. Using `hash-identifier`, we confirm these are MD5 hashes. MD5 is super outdated, like using a flip phone in 2025—easy to crack and not secure.

## Offline Hash Cracking (2 minutes)

Time to crack those hashes! We save them in `hashes.txt` and use `john the ripper`, which sounds like a horror movie villain but is actually a password-cracking tool. The command is:

```bash
john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

In seconds, we crack passwords like `password`, `abc123`, and `letmein`. This shows why weak passwords are a hacker’s dream. It’s like using “1234” as your phone passcode—don’t do it!

## Cryptographic Analysis and Mitigation (1 minute)

Let’s recap the issues: no passwords for some users, weak MD5 hashing, and unencrypted connections. To fix this, we need:
- **Strong passwords**: Treat them like your Netflix account—unique and complex.
- **Better hashing**: Use algorithms like bcrypt or Argon2, not MD5.
- **Secure connections**: Enable SSL/TLS to encrypt data.

These steps make our databases Fort Knox-level secure.

## Conclusion (1 minute)

That’s a wrap! We scanned databases, found weak spots, cracked passwords, and learned how to lock things down. Understanding these attacks helps us build stronger defenses. Thanks for joining, and keep your passwords strong—like your Wi-Fi signal!
