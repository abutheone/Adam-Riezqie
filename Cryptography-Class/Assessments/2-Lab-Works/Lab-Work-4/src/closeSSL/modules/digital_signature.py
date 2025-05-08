import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import clear

BANNER_FILE = "banners/banner-ds.txt"

def show_banner():
    try:
        with open(BANNER_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("[!] banner-ds.txt not found.")

def load_private_key(path):
    with open(path, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)

def load_public_key(path):
    with open(path, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())

def sign_file(private_key_path, file_path, output_path):
    try:
        private_key = load_private_key(private_key_path)
        with open(file_path, "rb") as f:
            data = f.read()
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        with open(output_path, "wb") as sig_file:
            sig_file.write(signature)
        print("[+] File signed successfully.")
    except Exception as e:
        print(f"[!] Error signing file: {e}")

def verify_signature(public_key_path, file_path, signature_path):
    try:
        public_key = load_public_key(public_key_path)
        with open(file_path, "rb") as f:
            data = f.read()
        with open(signature_path, "rb") as s:
            signature = s.read()
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("[✓] Signature is valid.")
    except InvalidSignature:
        print("[✗] Signature is invalid.")
    except Exception as e:
        print(f"[!] Error verifying signature: {e}")

def ds_main():
    while True:
        clear()
        show_banner()

        print("1. Sign")
        print("2. Verify")
        print("q. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            clear()
            show_banner()
            private_key_path = prompt("Enter key file path (private key): ", completer=PathCompleter())
            file_to_sign = prompt("Enter file path to sign: ", completer=PathCompleter())
            output_path = prompt("Save as (signed): ", completer=PathCompleter())

            sign_file(private_key_path.strip(), file_to_sign.strip(), output_path.strip())
            input("Press Enter to return to menu...")

        elif choice == "2":
            clear()
            show_banner()
            public_key_path = prompt("Enter key file path (public): ", completer=PathCompleter())
            file_to_verify = prompt("Enter file path to verify: ", completer=PathCompleter())
            signature_path = prompt("Enter signature file path: ", completer=PathCompleter())

            verify_signature(public_key_path.strip(), file_to_verify.strip(), signature_path.strip())
            input("Press Enter to return to menu...")

        elif choice == "q":
            print("[+] Exiting Digital Signature tool.")
            break

        else:
            print("[-] Invalid option.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    ds_main()
