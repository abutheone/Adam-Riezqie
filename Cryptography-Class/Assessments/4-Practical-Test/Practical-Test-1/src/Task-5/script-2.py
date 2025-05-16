import hashlib

# Your target MD5 hash
target_hash = "6283293831c84671546324c9373704ca"

# Path to your wordlist file
wordlist_file = "wordlist.txt"

with open(wordlist_file, "r", encoding="utf-8") as file:
    for line in file:
        # Hash the line exactly as it is (includes \n if present)
        hashed = hashlib.md5(line.encode()).hexdigest()

        if hashed == target_hash:
            print(f"[+] Match found:\nPlaintext: {repr(line)}\nMD5: {hashed}")
            break
    else:
        print("[-] No match found.")

