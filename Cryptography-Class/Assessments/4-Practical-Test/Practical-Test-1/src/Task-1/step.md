```bash
┌──(adamriezqie㉿NWS23010043)-[~]
└─$ gpg --full-generate-key
gpg (GnuPG) 2.2.46; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
  (14) Existing key from card
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 1y
Key expires at Sat 16 May 2026 06:29:25 PM +08
Is this correct? (y/N) Y

GnuPG needs to construct a user ID to identify your key.

Real name: MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM
Email address: muhammadadam.alihiraham@student.gmi.edu.my
Comment:
You selected this USER-ID:
    "MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /home/abu/.gnupg/trustdb.gpg: trustdb created
gpg: directory '/home/abu/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/abu/.gnupg/openpgp-revocs.d/244413E5B46029B88E0FFC399FC18FB47132CDB1.rev'
public and secret key created and signed.

pub   rsa4096 2025-05-16 [SC] [expires: 2026-05-16]
      244413E5B46029B88E0FFC399FC18FB47132CDB1
uid                      MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>
sub   rsa4096 2025-05-16 [E] [expires: 2026-05-16]


┌──(adamriezqie㉿NWS23010043)-[~]
└─$
```

```bash
┌──(adamriezqie㉿NWS23010043)-[~]
└─$ gpg --list-keys
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
gpg: next trustdb check due at 2026-05-16
/home/abu/.gnupg/pubring.kbx
----------------------------
pub   rsa4096 2025-05-16 [SC] [expires: 2026-05-16]
      244413E5B46029B88E0FFC399FC18FB47132CDB1
uid           [ultimate] MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>
sub   rsa4096 2025-05-16 [E] [expires: 2026-05-16]
```

```
┌──(adamriezqie㉿NWS23010043)-[~]
└─$ gpg --fingerprint
/home/abu/.gnupg/pubring.kbx
----------------------------
pub   rsa4096 2025-05-16 [SC] [expires: 2026-05-16]
      2444 13E5 B460 29B8 8E0F  FC39 9FC1 8FB4 7132 CDB1
uid           [ultimate] MUHAMMAD ADAM RIEZQIE BIN ALI HIRAHAM <muhammadadam.alihiraham@student.gmi.edu.my>
sub   rsa4096 2025-05-16 [E] [expires: 2026-05-16]
```