# Import section
import pyfiglet
import base64
import codecs
import random
import string
import itertools
import os
import msvcrt  
import gzip
import bz2
from morse3 import Morse

# --- Function Definitions ---

def get_string_input():
    while True:
        text = input("\nEnter your string: ").strip()
        if text:
            return text
        print("\n\033[91mEmpty input not allowed!\033[0m")
        print("Press any key to try again...")
        msvcrt.getch()


# --- Encrypt Function ---
def Encrypt():
    print("\nEncrypt Modes:")
    print("0. Single")
    print("1. Self Insecurity (Random times)")
    print("2. Insecurity (Told times)")
    print("3. Untrust (Different methods)")
    print("4. Paranoia (All methods)")

    mode = input().strip()
    
    if mode == "0":
        print("\nSelect encryption method:")
        print("0. Gzip")
        print("1. Bzip2")
        print("2. HeX")
        print("3. Base64")
        print("4. Binary")
        print("5. Morse")
        print("6. Caesar Cipher")
        print("7. Atbash Cipher")
        print("8. ROT13")
        print("9. Return")
        while True:

            method = input().strip()
            if method == "0": # Gzip
                text = get_string_input()
                result = gzip.compress(text.encode())
                print(f"Gzip encryption result: {result}")
                print(f"Text to encrypt: {text}")
                return_to_menu()
                break
            elif method == "1": # Bzip2
                text = get_string_input()
                result = bz2.compress(text.encode())
                print(f"Bzip2 encryption result: {result}")
                print(f"Text to encrypt: {text}")
                return_to_menu()
                break
            elif method == "2": # Hex
                text = get_string_input()
                result = text.encode("utf-8").hex()
                print(f"Hex encryption result: {result}")
                print(f"Text to encrypt: {text}")
                return_to_menu()
                break
            elif method == "3": # Base64
                text = get_string_input()
                result = base64.b64encode(text.encode())
                print(f"Text to encrypt: {text}")
                print(f"Base64 encryption result: {result}")
                return_to_menu()
                break
            elif method == "4": # Binary
                text = get_string_input()
                result = " ".join(format(ord(x), '08b') for x in text)
                print(f"Text to encrypt: {text}")
                print(f"Binary encryption result: {result}")
                return_to_menu()
                break
            elif method == "5": # Morse
                text = get_string_input()
                result = Morse().encode(text)
                print(f"Text to encrypt: {text}")
                print(f"Morse encryption result: {result}")
                return_to_menu()
                break
            elif method == "6": # Caesar Cipher
                text = get_string_input()
                input_key = input("Enter shift key (number): ").strip()
                if not input_key.isdigit():
                    print("\n\033[91mInvalid key! Must be a number.\033[0m")
                    print("Press any key to try again...")
                    msvcrt.getch()
                    continue    
                result = ''.join(chr((ord(char) - 65 + int(input_key)) % 26 + 65) if char.isupper() else
                                 chr((ord(char) - 97 + int(input_key)) % 26 + 97) if char.islower() else char for char in text)
                print(f"Caesar Cipher encryption result: {result}")
                print(f"Text to encrypt: {text}")
                return_to_menu()
                break
            elif method == "7": # Atbash Cipher
                text = get_string_input()
                result = ''.join(chr(155 - ord(char)) if char.isupper() else
                                 chr(219 - ord(char)) if char.islower() else char for char in text)
                print(f"Atbash Cipher encryption result: {result}")
                print(f"Text to encrypt: {text}")
                return_to_menu()
                break
            elif method == "8": # ROT13
                text = get_string_input()
                result = codecs.encode(text, 'rot_13')
                print(f"ROT13 encryption result: {result}")
                print(f"Text to encrypt: {text}")
                return_to_menu()
                break
            elif method == "9":
                return Encrypt()
            else:
                print("\n\033[1;91m" + "*" * 30)
                print("        INVALID")
                print("*" * 30 + "\033[0m\n")
    else:
        print("Invalid method selected.")


# --- Decrypt Function ---
def Dcrypt():
    print("\nDecrypt Modes:")
    print("1. Bruteforce (all methods)")
    print("2. Normal (choose methods)")
    mode = input("Select decrypt mode: ").strip()
    
    if mode == "2":
        print("\nSelect decryption method:")
        print("0. Gzip")
        print("1. Bzip2")
        print("2. HeX")
        print("3. Base64")
        print("4. Binary")
        print("5. Morse")
        print("6. Caesar Cipher")
        print("7. Atbash Cipher")
        print("8. ROT13")
        print("9. Return")
        while True:
            method = input("Enter method number: ").strip()
            if method == "0": # Gzip
                text = get_string_input()
                print("Gzip decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "1": # Bzip2
                text = get_string_input()
                print("Bzip2 decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "2": # Hex
                text = get_string_input()
                print("Hex decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "3": # Base64
                text = get_string_input()
                print("Base64 decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "4": # Binary
                text = get_string_input()
                print("Binary decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "5": # Morse
                text = get_string_input()
                print("Morse decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "6": # Caesar Cipher
                text = get_string_input()
                print("Caesar decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "7": # Atbash Cipher
                text = get_string_input()
                print("Atbash decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "8": # ROT13
                text = get_string_input()
                print("ROT13 decryption not implemented yet.")
                print(f"Text to decrypt: {text}")
                break
            elif method == "9":
                return Dcrypt()
            else:
                print("\n\033[1;91m" + "*" * 30)
                print("        INVALID")
                print("*" * 30 + "\033[0m\n")

    elif mode == "1":
        print("Bruteforce mode not implemented yet.")
    else:
        print("Invalid method selected.")

def FileAnalyze():
    print("\nFile Analysis Modes:")
    print("0. Text / String Analysis")
    print("1. File Analysis")
    mode = input().strip()
    
    pass

#prevent shutting down
def return_to_menu():
    print("\nPress 'M' to return to main menu or any other key to exit...")
    key = msvcrt.getch().decode('utf-8').upper()
    if key == 'M':
        os.system('cls' if os.name == 'nt' else 'clear')
        exec(open(__file__, encoding='utf-8').read())
    else:
        exit()


# --- UI and Main Logic ---

ascii_banner = pyfiglet.figlet_format("ExDcrypt")
print(ascii_banner)
print("Welcome to ExDcrypt, by: [    B1u3    ]")

print("\nChoose your mode:")
print("0. Encrypt")
print("1. Dcrypt")
print("2. File Analyze")
print("3. How this works??")

choice = input().strip()

if choice == "0":
    Encrypt()
elif choice == "1":
    Dcrypt()
elif choice == "2":
    FileAnalyze()
elif choice == "3":
    print("\nHow this works??\n")
    print("This tool provides encryption, decryption, and file analysis modes.")
    print("Choose a mode and follow the prompts to use the features.")
    print("\nPress any key to return...")
    msvcrt.getch()
   
    os.system('cls' if os.name == 'nt' else 'clear')
    exec(open(__file__, encoding='utf-8').read())

else:
    print("Bruh choos a valid option or just alt + f4")
