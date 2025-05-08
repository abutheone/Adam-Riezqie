import os
import hashlib
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.shortcuts import clear
from tabulate import tabulate

BANNER_FILE = "banners/banner-sha.txt"

def show_banner():
    try:
        with open(BANNER_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("[!] banner-sha.txt not found.")

def hash_file_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def collect_file_paths():
    paths = []
    print("[*] Enter file paths one by one. Press Enter without input to finish.")
    while True:
        path = prompt("File path: ", completer=PathCompleter())
        if not path.strip():
            break
        paths.append(path.strip())
    return paths

def sha_main():
    while True:
        clear()
        show_banner()

        print("1. Hashing")
        print("q. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            file_paths = collect_file_paths()

            if not file_paths:
                print("[!] No file paths entered.")
                input("Press Enter to return to menu...")
                continue

            result_table = []
            for path in file_paths:
                hash_result = hash_file_sha256(path)
                if hash_result:
                    result_table.append([os.path.basename(path), hash_result])
                else:
                    result_table.append([os.path.basename(path), "[File not found]"])

            print("\nSHA-256 Hash Results:")
            print(tabulate(result_table, headers=["Filename", "SHA-256 Hash"], tablefmt="grid"))

            input("\nPress Enter to return to menu...")

        elif choice == "q":
            print("[+] Exiting SHA-256 hashing tool.")
            break

        else:
            print("[-] Invalid option.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    sha_main()
