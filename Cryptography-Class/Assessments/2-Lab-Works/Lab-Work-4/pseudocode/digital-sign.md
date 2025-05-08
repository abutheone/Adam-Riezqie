# Digital Signature 
> using  RSA private key to sign,public key to verify

## Things need to have:
- banner, call from banner-ds.txt
- auto completion using tab prompt_toolkit, allow for path travel `../../` or root dir `/`
- auto completion for overwrite save as file
- clear terminal when enter a new option except the banner

---
```
1. show banner
2. show option: 1- sign, 2- verify, q- Exit
3. case option 1:
	show "Enter key file path (private key):"
    show "Enter file path to sign:"
    show "save as(signed):"
    back to step 2

4. case option 2:
    show "Enter key file path(public):"
    show "Enter file path to verify:"
    show result
    back to step 2

5. case option q:
    end
```