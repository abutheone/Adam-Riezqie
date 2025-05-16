import hashlib

# Your target SHA-256 hash
target_hash = "2bc92f33a2ede5ada3d65b468a81f617d0229d843d87c63313833e509e5a6782"

# Path to your wordlist
wordlist_file = "wordlist.txt"

with open(wordlist_file, "r", encoding="utf-8") as file:
    for line in file:
        # Preserve the line exactly as-is (including newlines)
        hashed = hashlib.sha256(line.encode()).hexdigest()

        if hashed == target_hash:
            print(f"[+] Match found:\nPlaintext: {repr(line)}\nSHA-256: {hashed}")
            break
    else:
        print("[-] No match found.")

