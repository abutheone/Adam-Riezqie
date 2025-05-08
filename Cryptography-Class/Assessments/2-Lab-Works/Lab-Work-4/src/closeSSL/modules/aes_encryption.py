import os
import sys
import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import clear

BANNER_FILE = "banners/banner-aes.txt"


def show_banner():
    if os.path.exists(BANNER_FILE):
        with open(BANNER_FILE, "r") as f:
            print(f.read())
    else:
        print("[!] banner.txt not found.")


def generate_key():
    key = get_random_bytes(32)  # 256 bits
    print("\n[+] Generated Key (hex):", key.hex())
    return key


def generate_iv():
    iv = get_random_bytes(16)  # 128 bits
    print("\n[+] Generated IV (hex):", iv.hex())
    return iv


def save_to_file(data, path):
    if os.path.exists(path):
        confirm = input(f"[!] File {path} exists. Overwrite? (y/n): ")
        if confirm.lower() != 'y':
            print("[-] Operation cancelled.")
            return
    with open(path, "wb") as f: # KIV - why wb
        f.write(data)
    print(f"[+] Saved to {path}")


def encrypt_file(key, iv, in_path, out_path):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_path, "rb") as f:
        plaintext = f.read()
    # Padding (PKCS7)
    pad_len = 16 - len(plaintext) % 16
    plaintext += bytes([pad_len] * pad_len)
    ciphertext = cipher.encrypt(plaintext)
    save_to_file(ciphertext, out_path)


def decrypt_file(key, iv, in_path, out_path):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_path, "rb") as f:
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    pad_len = plaintext[-1]
    plaintext = plaintext[:-pad_len]
    save_to_file(plaintext, out_path)


def load_hex_file(path):
    with open(path, "r") as f:
        return binascii.unhexlify(f.read().strip()) #KIV - all func


def input_path(prompt_text):
    return prompt(prompt_text, completer=PathCompleter())


def aes_main():
    while True:
        clear()
        show_banner()
        print("1. Encryption")
        print("2. Decryption")
        print("q. Exit")
        choice = input("Select option: ")

        if choice == "1":
            clear()
            show_banner()
            keyOpt = input_path("Enter key file path or press `n` to generate key: ")
            if keyOpt.lower() == 'n':
                key = generate_key()
                key_save = input_path("Save key as: ")
                save_to_file(key.hex().encode(), key_save) #KIV - .encode()

                iv = generate_iv()
                iv_save = input_path("Save IV as: ")
                save_to_file(iv.hex().encode(), iv_save) #KIV - .encode()
            else:
                key = load_hex_file(keyOpt)
                iv_path = input_path("Enter IV file path: ")
                iv = load_hex_file(iv_path)

            file_in = input_path("\nEnter file path to encrypt: ")
            file_out = input_path("Save encrypted file as: ")
            encrypt_file(key, iv, file_in, file_out)
            input("[+] Done. Press Enter to continue...")

        elif choice == "2":
            key_path = input_path("Enter key file path: ")
            iv_path = input_path("Enter IV file path: ")
            file_in = input_path("Enter file path to decrypt: ")
            file_out = input_path("Save decrypted file as: ")

            key = load_hex_file(key_path)
            iv = load_hex_file(iv_path)
            decrypt_file(key, iv, file_in, file_out)
            input("[+] Done. Press Enter to continue...")

        elif choice == "q":
            print("[+] Exiting. Bye!")
            break
        else:
            input("[!] Invalid option. Press Enter to try again...")


if __name__ == "__main__":
    aes_main()
