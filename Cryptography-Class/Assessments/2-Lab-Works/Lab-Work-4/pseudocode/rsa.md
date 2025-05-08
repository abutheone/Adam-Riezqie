# RSA Encryption and Decryption Tool
> for this RSA enc, we used 2048 bits

## Things need to have:
- banner, call from banner-rsa.txt
- auto completion using tab prompt_toolkit, allow for path travel `../../` or root dir `/`
- auto completion for overwrite save as file
- clear terminal when enter a new option except the banner

---

```
1. show banner
2. show option: 1- Encryption, 2- Decryption, 3- Generate RSA Keys, q- Exit
3. case option 1:
	show "Enter public key file path:"
    key file entered:
    show "Enter file path to encrypt:"
    show "save as:"
    back to step 2

4. case option 2:
    show "Enter private key file path:"
    show "Enter file path to decrypt:"
    show "save as:"
    back to step 2

5. case option q:
    Generate Private key
    print private Key
    show "Save as [private key]:"

    Extract Public Key from private key
    print public key
    show "Save as [public key]:"
    back to step 2

6. case option 4:
    end
```