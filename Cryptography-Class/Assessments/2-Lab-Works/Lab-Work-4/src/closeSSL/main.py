import os
from prompt_toolkit.shortcuts import clear

# Import module main functions
from modules.aes_encryption import aes_main
from modules.rsa_encryption import rsa_main
from modules.sha_hashing import sha_main
from modules.digital_signature import ds_main

BANNER_FILE = "banners/banner.txt"

def show_banner():
    try:
        with open(BANNER_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("[!] Main banner file not found.")

def main():
    while True:
        clear()
        show_banner()
        print("\n===========================[Main Menu]===========================")
        print("1. AES Encryption (AES-256-CBC)")
        print("2. RSA Encryption (2048-bit)")
        print("3. SHA-256 Hashing")
        print("4. Digital Signature")
        print("q. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            aes_main()
        elif choice == "2":
            rsa_main()
        elif choice == "3":
            sha_main()
        elif choice == "4":
            ds_main()
        elif choice == "q":
            print("[+] Exiting closeSSL.")
            break
        else:
            print("[-] Invalid option.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
