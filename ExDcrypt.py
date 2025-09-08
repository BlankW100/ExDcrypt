# Import section
import pyfiglet
import base64
import codecs
import random
import string
import itertools
import os
import msvcrt  

# --- Function Definitions ---

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

            method = input("Enter method number: ").strip()
            if method == "0":
                
                print("Gzip encryption not implemented yet.")
                break
            elif method == "1":
                print("Bzip2 encryption not implemented yet.")
                break
            elif method == "2":
                print("Hex decryption not implemented yet.")
                break
            elif method == "3":
                print("Base64 decryption not implemented yet.")
                break
            elif method == "4":
                print("Binary decryption not implemented yet.")
                break
            elif method == "5":
                print("Morse encryption not implemented yet.")
                break
            elif method == "6":
                print("Ceasar encryption not implemented yet:" )
                break
            elif method == "7":
                print("Atbash encryption not implemented yet:")
                break
            elif method == "8":
                print("ROT13 encryption not implemented yet:")
                break
            elif method == "9":
                return Encrypt()
            else:
                print("\n\033[1;91m" + "*" * 30)
                print("        INVALID")
                print("*" * 30 + "\033[0m\n")
    else:
        print("Invalid method selected.")

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
            if method == "0":
                print("Gzip decryption not implemented yet.")
                break
            elif method == "1":
                print("Bzip2 decryption not implemented yet.")
                break
            elif method == "2":
                print("Hex decryption not implemented yet.")
                break
            elif method == "3":
                print("Base64 decryption not implemented yet.")
                break
            elif method == "4":
                print("Binary decryption not implemented yet.")
                break
            elif method == "5":
                print("Morse decryption not implemented yet.")
                break
            elif method == "6":
                print("Caesar decryption not implemented yet:" )
                break
            elif method == "7":
                print("Atbash decryption not implemented yet:")
                break
            elif method == "8":
                print("ROT13 decryption not implemented yet:")
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
