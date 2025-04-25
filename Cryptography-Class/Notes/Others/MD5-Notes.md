# MD5 Notes - Why It’s Weak AF

Yo, MD5 is that old-school hashing we used in the lab, but it’s straight-up garbage for security. Here’s why it sucks, real quick:

- **Too Fast, Bro:** MD5 hashes stuff super quick, so hackers can guess billions of passwords in seconds with tools like `john` or `hashcat`. We cracked those lab hashes (`password`, `abc123`) in no time.
- **No Salt, Same Hash:** No salt means same passwords = same hash. Like, `admin` and `smithy` had the same hash (`5f4dcc3b5aa765d61d8327deb882cf99`), so hackers can just use pre-made lists to crack ‘em.

**Real-World L:** In 2012, LinkedIn got wrecked ‘cause they used MD5 with no salt. Hackers cracked tons of passwords fast, just like we did in the lab. Use bcrypt or Argon2 instead, way tougher to break.