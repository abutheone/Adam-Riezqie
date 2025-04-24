# Database Notes

## 5W1H of Databases
- **Who**: Database administrators, developers, end-users.
- **What**: Organized collection of data managed by a Database Management System (DBMS).
- **When**: Originated in the 1960s; relational databases popularized in the 1970s.
- **Where**: On-premises servers, virtual machines, and cloud environments.
- **Why**: To store, retrieve, and manage structured data efficiently.
- **How**: Using DBMS software with query languages (e.g., SQL for relational databases).

## Common Database Ports
- **MySQL**: 3306
- **Microsoft SQL Server (MSSQL)**: 1433
- **PostgreSQL**: 5432
- **Oracle Database**: 1521
- **MongoDB**: 27017



## Common Database Usernames
- **MySQL**: `root` [^mysql-root]  
- **Microsoft SQL Server (MSSQL)**: `sa` [^mssql-sa]  
- **PostgreSQL**: `postgres` [^postgres-default]  
- **Oracle Database**: `SYS`, `SYSTEM` [^oracle-default]  
- **MongoDB**: _no default user; commonly create `admin` or `root` once `--auth` is enabled_ [^mongodb-default]  



## Additional Notes
- **Authentication**: Use strong hashing algorithms (e.g., bcrypt, Argon2) and enforce multi-factor authentication (MFA).
- **Weak Password Hashes**: MD5 and SHA-1 are considered insecure and vulnerable to rainbow table attacks.
- **Poor Authentication Practices**: Default credentials, lack of salt, and absence of rate limiting can be exploited.
- **Mitigations**: Implement account lockout policies, use salted hashes, enforce password complexity, and regularly audit access logs.

## References
1. [Wikipedia: Database](https://en.wikipedia.org/wiki/Database)
2. [MySQL Reference Manual – Connection Security](https://dev.mysql.com/doc/refman/8.0/en/security.html)
3. [PostgreSQL Documentation – Client Authentication](https://www.postgresql.org/docs/current/auth-methods.html)
4. [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
