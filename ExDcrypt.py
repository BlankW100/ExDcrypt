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

# mode 1
    if mode == "1":
        minvalue = int(input("Enter minimum times to encrypt: ").strip())
        if minvalue < 1:
            print("The minvalue must be at least 1")
            return_to_menu()

        maxvalue = int(input("Enter maximum times to encrypt: ").strip())
        random_times = random.randint(minvalue, maxvalue)
        initial_random_times = random_times

    
    text = get_string_input() 
    result = text

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
    method = input("Choose method: ").strip()
    while random_times > 0:
        
        if method == "0":  # Gzip
            result = gzip.compress(result.encode() if isinstance(result, str) else result)

        elif method == "1":  # Bzip2
            result = bz2.compress(result.encode() if isinstance(result, str) else result)

        elif method == "2":  # Hex
            result = result.encode("utf-8").hex() if isinstance(result, str) else result.hex()

        elif method == "3":  # Base64
            result = base64.b64encode(result.encode() if isinstance(result, str) else result)

        elif method == "4":  # Binary
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = " ".join(format(ord(x), '08b') for x in result)

        elif method == "5":  # Morse
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = Morse().encode(result)

        elif method == "6":  # Caesar Cipher
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            input_key = input("Enter shift key (number): ").strip()
            if not input_key.isdigit():
                print("Invalid key! Must be a number.")
                continue
            key = int(input_key)
            result = ''.join(
                chr((ord(char) - 65 + key) % 26 + 65) if char.isupper() else
                chr((ord(char) - 97 + key) % 26 + 97) if char.islower() else char
                for char in result
            )

        elif method == "7":  # Atbash Cipher
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = ''.join(
                chr(155 - ord(char)) if char.isupper() else
                chr(219 - ord(char)) if char.islower() else char
                for char in result
            )

        elif method == "8":  # ROT13
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = codecs.encode(result, 'rot_13')

        elif method == "9":
            return Encrypt()

        else:
            print("Invalid method.")
            continue

        random_times -= 1  # decrement
    print(f"Final encryption result: {result}")   
    print(f"Encrypted times: {initial_random_times}")


# mode 2
    if mode == "2":
        encrypt_times = int(input("Enter amount of times to encrypt: ").strip())
        initial_times = encrypt_times
        text = get_string_input() 
        result = text

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
    method = input("Choose method: ").strip()

    while encrypt_times > 0:
        

        if method == "0":  # Gzip
            result = gzip.compress(result.encode() if isinstance(result, str) else result)

        elif method == "1":  # Bzip2
            result = bz2.compress(result.encode() if isinstance(result, str) else result)

        elif method == "2":  # Hex
            result = result.encode("utf-8").hex() if isinstance(result, str) else result.hex()

        elif method == "3":  # Base64
            result = base64.b64encode(result.encode() if isinstance(result, str) else result)

        elif method == "4":  # Binary
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = " ".join(format(ord(x), '08b') for x in result)

        elif method == "5":  # Morse
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = Morse().encode(result)

        elif method == "6":  # Caesar Cipher
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            input_key = input("Enter shift key (number): ").strip()
            if not input_key.isdigit():
                print("Invalid key! Must be a number.")
                continue
            key = int(input_key)
            result = ''.join(
                chr((ord(char) - 65 + key) % 26 + 65) if char.isupper() else
                chr((ord(char) - 97 + key) % 26 + 97) if char.islower() else char
                for char in result
            )

        elif method == "7":  # Atbash Cipher
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = ''.join(
                chr(155 - ord(char)) if char.isupper() else
                chr(219 - ord(char)) if char.islower() else char
                for char in result
            )

        elif method == "8":  # ROT13
            if isinstance(result, bytes): result = result.decode(errors="ignore")
            result = codecs.encode(result, 'rot_13')

        elif method == "9":
            return Encrypt()

        else:
            print("Invalid method.")
            continue
        random_times -= 1  # decrement
    print(f"Final encryption result: {result}")   
    print(f"Encrypted times: {initial_times}")

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
                result = gzip.decompress(eval(text)).decode()
                print(f"Gzip decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "1": # Bzip2
                text = get_string_input()
                result = bz2.decompress(eval(text)).decode()
                print(f"Bzip2 decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "2": # Hex
                text = get_string_input()
                result = bytes.fromhex(text).decode('utf-8')
                print(f"Hex decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "3": # Base64
                text = get_string_input()
                result = base64.b64decode(text).decode()
                print(f"Base64 decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()    
                break
            elif method == "4": # Binary
                text = get_string_input()
                result = ''.join(chr(int(b, 2)) for b in text.split())
                print(f"Binary decryption result: {result}") 
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "5": # Morse
                text = get_string_input()
                result = Morse().decode(text)
                print(f"Morse decryption result: {result}")
                print(f"Text to decrypt: {text}")
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
                result = ''.join(chr((ord(char) - 65 - int(input_key)) % 26 + 65) if char.isupper() else
                                 chr((ord(char) - 97 - int(input_key)) % 26 + 97) if char.islower() else char for char in text)
                print(f"Caesar Cipher decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "7": # Atbash Cipher
                text = get_string_input()
                result = ''.join(chr(155 - ord(char)) if char.isupper() else
                                 chr(219 - ord(char)) if char.islower() else char for char in text)
                print(f"Atbash Cipher decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "8": # ROT13
                text = get_string_input()
                result = codecs.decode(text, 'rot_13')
                print(f"ROT13 decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
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
