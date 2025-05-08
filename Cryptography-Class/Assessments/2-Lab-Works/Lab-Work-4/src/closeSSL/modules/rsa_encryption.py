from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import clear
import os

RSA_BANNER_FILE = "banners/banner-rsa.txt"

def show_banner_rsa():
    if os.path.exists(RSA_BANNER_FILE):
        with open(RSA_BANNER_FILE, "r") as f:
            print(f.read())
    else:
        print("[!] banner-rsa.txt not found.")

def save_to_file(data, path, binary=False):
    mode = "wb" if binary else "w"
    if os.path.exists(path):
        confirm = input(f"[!] File {path} exists. Overwrite? (y/n): ")
        if confirm.lower() != 'y':
            print("[-] Operation cancelled.")
            return False
    with open(path, mode) as f:
        f.write(data)
    print(f"[+] Saved to {path}")
    return True

def input_path(prompt_text):
    return prompt(prompt_text, completer=PathCompleter())

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    print("[+] Private Key:\n", private_key.decode())
    priv_path = input_path("Save as [private key]: ")
    save_to_file(private_key, priv_path, binary=True)

    print("[+] Public Key:\n", public_key.decode())
    pub_path = input_path("Save as [public key]: ")
    save_to_file(public_key, pub_path, binary=True)

def encrypt_file_rsa(pub_key_path, in_path, out_path):
    with open(pub_key_path, "rb") as f:
        pub_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(pub_key)
    with open(in_path, "rb") as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)
    save_to_file(ciphertext, out_path, binary=True)

def decrypt_file_rsa(priv_key_path, in_path, out_path):
    with open(priv_key_path, "rb") as f:
        priv_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(priv_key)
    with open(in_path, "rb") as f:
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    save_to_file(plaintext, out_path, binary=True)

def rsa_main():
    while True:
        clear()
        show_banner_rsa()
        print("1. Encryption")
        print("2. Decryption")
        print("3. Generate RSA Keys")
        print("q. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            pub_key_path = input_path("Enter public key file path: ")
            in_path = input_path("Enter file path to encrypt: ")
            out_path = input_path("Save as: ")
            encrypt_file_rsa(pub_key_path, in_path, out_path)
            input("Press Enter to return to menu...")

        elif choice == "2":
            priv_key_path = input_path("Enter private key file path: ")
            in_path = input_path("Enter file path to decrypt: ")
            out_path = input_path("Save as: ")
            decrypt_file_rsa(priv_key_path, in_path, out_path)
            input("Press Enter to return to menu...")

        elif choice == "3":
            generate_rsa_keys()
            input("Press Enter to return to menu...")

        elif choice == "q":
            print("[+] Exiting RSA tool.")
            break

        else:
            print("[-] Invalid choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    rsa_main()
