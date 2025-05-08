# AES-256-CBC Encryption and Decryption Tool
> for this aes enc, use aes-256-cbc

## Things need to have:
- banner, call from banner.txt
- auto completion using tab prompt_toolkit, allow for path travel `../../` or root dir `/`
- auto completion for overwrite save as file
- clear terminal when enter a new option except the banner
- use hex 32 bytes for generate key
- use hex 16 bytes for generete iv

---
```
1. show banner
2. show option: 1- Encryption, 2- Decryption, q- Exit
3. case option 1:
	show "Enter key file path or press `n` for generate key:"
	if n:
	    generate key
        show key
	    show "Save as:"

        generate iv
        show iv
        show "save as:"

	else, key file entered:
   	    show "enter key file path:"
        show "enter iv file path:"

    show "Enter file path to encrypt:"
        show "save as:"
        back to step 2

4. case option 2:
    show "Enter key file path:"
    show "Enter iv file path:"
    show "Enter file path to decrypt:"
    show "save as:"
    back to step 2

5. case option q:
    end
```