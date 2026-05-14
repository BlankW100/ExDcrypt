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
import binascii
import re
import ast
from morse3 import Morse as m

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
    print("5. Return")

    mode = input().strip()

    # --- MODE 0: Single Encryption ---
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
                result = m(text).stringToMorse()  
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
                return
            else:
                print("\n\033[1;91m" + "*" * 30)
                print("        INVALID")
                print("*" * 30 + "\033[0m\n")

# --- MODE 1: Self Insecurity (Random times) ---
    elif mode == "1":
        try:
            minvalue = int(input("Enter minimum times to encrypt: ").strip())
            if minvalue < 1:
                print("The minvalue must be at least 1")
                return_to_menu()
                return

            maxvalue = int(input("Enter maximum times to encrypt: ").strip())
            if maxvalue < minvalue:
                print("\n\033[91mMax value must be greater than or equal to min value!\033[0m")
                return_to_menu()
                return
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

            caesar_key = None
            if method == "6":
                while True:
                    input_key = input("Enter shift key (number): ").strip()
                    if input_key.isdigit():
                        caesar_key = int(input_key)
                        break
                    print("Invalid key! Must be a number.")

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
                    result = m(result).stringToMorse()

                elif method == "6":  # Caesar Cipher
                    if isinstance(result, bytes): result = result.decode(errors="ignore")
                    result = ''.join(
                        chr((ord(char) - 65 + caesar_key) % 26 + 65) if char.isupper() else
                        chr((ord(char) - 97 + caesar_key) % 26 + 97) if char.islower() else char
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
                    s = result.decode(errors="ignore") if isinstance(result, bytes) else str(result)
                    result = s.translate(str.maketrans(
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
                    ))

                elif method == "9":
                    return

                else:
                    print("Invalid method.")
                    continue

                random_times -= 1  # decrement
            print(f"Final encryption result: {result}")   
            print(f"Encrypted times: {initial_random_times}")
            return_to_menu()

        except ValueError:
            print("\n\033[91mPlease enter valid numbers!\033[0m")
            return_to_menu()

    # --- MODE 2: Insecurity (Told times) ---
    elif mode == "2":
        try:
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

            caesar_key = None
            if method == "6":
                while True:
                    input_key = input("Enter shift key (number): ").strip()
                    if input_key.isdigit():
                        caesar_key = int(input_key)
                        break
                    print("Invalid key! Must be a number.")

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
                    result = m(result).stringToMorse()

                elif method == "6":  # Caesar Cipher
                    if isinstance(result, bytes): result = result.decode(errors="ignore")
                    result = ''.join(
                        chr((ord(char) - 65 + caesar_key) % 26 + 65) if char.isupper() else
                        chr((ord(char) - 97 + caesar_key) % 26 + 97) if char.islower() else char
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
                    s = result.decode(errors="ignore") if isinstance(result, bytes) else str(result)
                    result = s.translate(str.maketrans(
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
                    ))

                elif method == "9":
                    return

                else:
                    print("Invalid method.")
                    continue
                encrypt_times -= 1  # decrement
            print(f"Final encryption result: {result}")   
            print(f"Encrypted times: {initial_times}")
            return_to_menu()

        except ValueError:
            print("\n\033[91mPlease enter a valid number!\033[0m")
            return_to_menu()

    # --- MODE 3: Untrust (Different methods) ---
    elif mode == "3":
        try:
            method_value = int(input("How many methods do you want to apply: ").strip())
            initial_value = method_value

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
    

            while method_value > 0:

                method = input("Choose method: ").strip()

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
                    result = m(result).stringToMorse()

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
                    s = result.decode(errors="ignore") if isinstance(result, bytes) else str(result)
                    result = s.translate(str.maketrans(
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
                    ))

                elif method == "9":
                    return

                else:
                    print("Invalid method.")
                    continue
                method_value -= 1  # decrement
            print(f"Final encryption result: {result}")
            print(f"Methods applied: {initial_value}")
            return_to_menu()

        except ValueError:
            print("\n\033[91mPlease enter a valid number!\033[0m")
            return_to_menu()

    # --- MODE 4: Paranoia (All methods) ---
    elif mode == "4":
        print("Paranoia mode not implemented yet")
        return_to_menu()

    # --- Return to Main Menu ---
    elif mode == "5":
        return

    else:
        print("\n\033[1;91m" + "*" * 30)
        print("        INVALID MODE")
        print("*" * 30 + "\033[0m\n")
        return_to_menu()

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
                try:
                    result = gzip.decompress(ast.literal_eval(text)).decode()
                    print(f"Gzip decryption result: {result}")
                    print(f"Text to decrypt: {text}")
                    return_to_menu()
                    break
                except Exception as e:
                    print(f"\n\033[91mError: {e}\033[0m")
                    print("Paste the exact bytes output from encryption (e.g. b'\\x1f\\x8b...')")
                    msvcrt.getch()
                    continue
            elif method == "1": # Bzip2
                text = get_string_input()
                try:
                    result = bz2.decompress(ast.literal_eval(text)).decode()
                except Exception as e:
                    print(f"\n\033[91mError: {e}\033[0m")
                    print("Paste the exact bytes output from encryption (e.g. b'BZh...')")
                    msvcrt.getch()
                    continue
                print(f"Bzip2 decryption result: {result}")
                print(f"Text to decrypt: {text}")
                return_to_menu()
                break
            elif method == "2": # Hex
                text = get_string_input()
                try:
                    result = bytes.fromhex(text).decode('utf-8')
                    print(f"Hex decryption result: {result}")
                    print(f"Text to decrypt: {text}")
                    return_to_menu()
                    break
                except Exception as e:
                    print(f"\n\033[91mError: {e}\033[0m")
                    print("Make sure input is valid hex (e.g. '48656c6c6f')")
                    print("Press any key to try again...")
                    msvcrt.getch()
                    continue
            elif method == "3": # Base64
                text = get_string_input()
                try:
                    result = base64.b64decode(text).decode()
                    print(f"Base64 decryption result: {result}")
                    print(f"Text to decrypt: {text}")
                    return_to_menu()
                    break
                except Exception as e:
                    print(f"\n\033[91mError: {e}\033[0m")
                    print("Make sure input is valid Base64 (e.g. 'SGVsbG8=')")
                    print("Press any key to try again...")
                    msvcrt.getch()
                    continue
            elif method == "4": # Binary
                text = get_string_input()
                try:
                    # Validate binary input
                    chunks = text.split()
                    if not all(set(chunk) <= {'0', '1'} for chunk in chunks):
                        raise ValueError("Invalid binary format - use only 0s and 1s")
        
                    # Check each chunk is 8 bits
                    if not all(len(chunk) == 8 for chunk in chunks):
                        raise ValueError("Each binary chunk must be 8 bits")
            
                    # Convert and validate character codes
                    result = ''
                    for chunk in chunks:
                        value = int(chunk, 2)
                        if value > 0x10FFFF:  # Maximum Unicode value
                            raise ValueError(f"Invalid character code: {value}")
                        result += chr(value)
            
                    print(f"Binary decryption result: {result}")
                    print(f"Text to decrypt: {text}")
                    return_to_menu()
                    break
        
                except ValueError as e:
                    print(f"\n\033[91mError: {e}\033[0m")
                    print("Make sure input is valid 8-bit binary (e.g. '01101000 01101001')")
                    print("Press any key to try again...")
                    msvcrt.getch()
                    continue
            elif method == "5": # Morse
                text = get_string_input()
                result = m(text).morseToString()
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
                return
            else:
                print("\n\033[1;91m" + "*" * 30)
                print("        INVALID")
                print("*" * 30 + "\033[0m\n")

    elif mode == "1":
        text = get_string_input()
        print("\n--- Bruteforce Decrypt Results ---")
        found = False

        # Gzip
        try:
            r = gzip.decompress(ast.literal_eval(text)).decode()
            print(f"[Gzip]          {text}  ->  {r}")
            found = True
        except Exception:
            pass

        # Bzip2
        try:
            r = bz2.decompress(ast.literal_eval(text)).decode()
            print(f"[Bzip2]         {text}  ->  {r}")
            found = True
        except Exception:
            pass

        # Hex
        try:
            r = bytes.fromhex(text).decode('utf-8')
            print(f"[Hex]           {text}  ->  {r}")
            found = True
        except Exception:
            pass

        # Base64
        try:
            r = base64.b64decode(text).decode()
            print(f"[Base64]        {text}  ->  {r}")
            found = True
        except Exception:
            pass

        # Binary
        try:
            chunks = text.split()
            if chunks and all(set(c) <= {'0', '1'} for c in chunks) and all(len(c) == 8 for c in chunks):
                r = ''.join(chr(int(c, 2)) for c in chunks)
                print(f"[Binary]        {text}  ->  {r}")
                found = True
        except Exception:
            pass

        # Morse
        try:
            r = m(text).morseToString()
            print(f"[Morse]         {text}  ->  {r}")
            found = True
        except Exception:
            pass

        # Caesar - all 25 shifts
        for shift in range(1, 26):
            try:
                r = ''.join(
                    chr((ord(c) - 65 - shift) % 26 + 65) if c.isupper() else
                    chr((ord(c) - 97 - shift) % 26 + 97) if c.islower() else c
                    for c in text
                )
                print(f"[Caesar shift={shift:2d}]  {text}  ->  {r}")
                found = True
            except Exception:
                pass

        # Atbash
        try:
            r = ''.join(
                chr(155 - ord(c)) if c.isupper() else
                chr(219 - ord(c)) if c.islower() else c
                for c in text
            )
            print(f"[Atbash]        {text}  ->  {r}")
            found = True
        except Exception:
            pass

        # ROT13
        try:
            r = text.translate(str.maketrans(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
            ))
            print(f"[ROT13]         {text}  ->  {r}")
            found = True
        except Exception:
            pass

        if not found:
            print("No successful decryption found.")
        print("\n--- Done ---")
        return_to_menu()
    else:
        print("Invalid method selected.")

def FileAnalyze():
    print("\nFile Analysis Modes:")
    print("0. Text / String Analysis")
    print("1. File Analysis")
    mode = input().strip()

    if mode == "0":
        text = get_string_input()
        print("\n--- String Analysis Results ---")

        # --- Gzip ---
        candidate = b""
        try:
            if text.startswith("b'") or text.startswith("b\""):
                candidate = ast.literal_eval(text)
            else:
                candidate = text.encode()

            if candidate[:2] == b"\x1f\x8b":
                print("[+] Looks like Gzip compressed data")
        except Exception:
            pass

        # --- Bzip2 ---
        try:
            if candidate[:3] == b"BZh":
                print("[+] Looks like Bzip2 compressed data")
        except Exception:
            pass

        # --- Hex ---
        try:
            if all(c in "0123456789abcdefABCDEF" for c in text) and len(text) % 2 == 0:
                binascii.unhexlify(text)
                print("[+] Looks like Hex encoding")
        except Exception:
            pass

        # --- Base64 ---
        try:
            if re.fullmatch(r"[A-Za-z0-9+/=]+", text) and len(text) % 4 == 0:
                base64.b64decode(text)
                print("[+] Looks like Base64 encoding")
        except Exception:
            pass

        # --- Binary ---
        if all(c in "01 " for c in text) and len(text.replace(" ", "")) % 8 == 0:
            print("[+] Looks like Binary encoding (8-bit ASCII)")

        # --- Morse ---
        if all(c in ".-/ " for c in text) and ("." in text or "-" in text):
            print("[+] Looks like Morse code")

        # --- Caesar Cipher Guess ---
        if text.isalpha() and (text.isupper() or text.islower()):
            print("[?] Could be Caesar Cipher (shifted text)")

        # --- Atbash ---
        if text.isalpha():
            print("[?] Could be Atbash Cipher (mirrored alphabet)")

        # --- ROT13 ---
        try:
            rot = text.translate(str.maketrans(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
            ))
            if rot.isalpha():
                print("[?] Could be ROT13")
        except Exception:
            pass

        print("\n--- Analysis Complete ---")
        return_to_menu()

    elif mode == "1":
        print("File Analysis not implemented yet")
        return_to_menu()

    else:
        print("\n\033[1;91m" + "*" * 30)
        print("        INVALID MODE")
        print("*" * 30 + "\033[0m\n")

class _ReturnToMenu(Exception):
    pass

def return_to_menu():
    print("\nPress 'M' to return to main menu or any other key to exit...")
    raw = msvcrt.getch()
    try:
        key = raw.decode('utf-8').upper()
    except UnicodeDecodeError:
        key = ''
    if key == 'M':
        raise _ReturnToMenu()
    else:
        exit()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_banner = pyfiglet.figlet_format("ExDcrypt")
        print(ascii_banner)
        print("Welcome to ExDcrypt, by: [    B1u3    ]")
        print("\nChoose your mode:")
        print("0. Encrypt")
        print("1. Dcrypt")
        print("2. File Analyze")
        print("3. How this works??")
        print("4. Exit")

        choice = input().strip()
        try:
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
            elif choice == "4":
                exit()
            else:
                print("Bruh choos a valid option or just alt + f4")
        except _ReturnToMenu:
            continue

if __name__ == "__main__":
    main()
