# Import section
import pyfiglet
import base64
import codecs
import random
import string
import itertools

def Encrypt():
    print("\nEncrypt Modes:")
    print("0. Normal")
    print("1. Self Insecurity (Random times)")
    print("2. Insecurity (Told times)")
    print("3. Untrust (Different methods)")
    print("4. Paranoia (All methods)")
    mode = input().strip()
    
    pass

def Dcrypt():
    print("\nDecrypt Modes:")
    print("1. Bruteforce (all methods)")
    print("2. Normal (choose methods)")
    mode = input("Select decrypt mode: ").strip()
    
    pass

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
else:
    print("Bruh choos a valid option or just alt + f4")
