#Import section
import pyfiglet
import base64
import codecs
import random
import string

# --- Encryption/Decryption Methods ---

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def rot13(text):
    return codecs.encode(text, 'rot_13')

def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return "[Invalid Base64]"

def hex_encrypt(text):
    return text.encode().hex()

def hex_decrypt(text):
    try:
        return bytes.fromhex(text).decode()
    except Exception:
        return "[Invalid Hex]"

def atbash(text):
    def atbash_char(c):
        if c.isupper():
            return chr(90 - (ord(c) - 65))
        elif c.islower():
            return chr(122 - (ord(c) - 97))
        else:
            return c
    return ''.join(atbash_char(c) for c in text)

# --- Method Registry ---

ENCRYPT_METHODS = {
    "Caesar": caesar_encrypt,
    "ROT13": rot13,
    "Base64": base64_encrypt,
    "Hex": hex_encrypt,
    "Atbash": atbash,
}

DECRYPT_METHODS = {
    "Caesar": caesar_decrypt,
    "ROT13": rot13,
    "Base64": base64_decrypt,
    "Hex": hex_decrypt,
    "Atbash": atbash,
}

# --- UI and Main Logic ---

ascii_banner = pyfiglet.figlet_format("ExDcrypt")
print(ascii_banner)
print("Welcome to ExDcrypt, by: [              ]")

print("\nChoose your mode:")
print("0. Encrypt")
print("1. Dcrypt")

choice = input().strip()

def Encrypt():
    print("\nEncrypt Modes:")
    print("0. Normal")
    print("1. Insecurity (Random times)")
    print("2. Insecurity (Told times)")
    print("3. Untrust (Different methods)")
    mode = input().strip()

    text = input()

    if mode == "0":
        print("\nAvailable methods:", ', '.join(ENCRYPT_METHODS.keys()))
        method = input().strip().title()
        if method == "Caesar":
            shift = int(input())
            print("Encrypted:", caesar_encrypt(text, shift))
        elif method in ENCRYPT_METHODS:
            print("Encrypted:", ENCRYPT_METHODS[method](text))
        else:
            print("Unknown method.")

    elif mode == "1":
        method = input().strip().title()
        times = random.randint(2, 10)
        result = text
        for _ in range(times):
            if method == "Caesar":
                shift = random.randint(1, 25)
                result = caesar_encrypt(result, shift)
            elif method in ENCRYPT_METHODS:
                result = ENCRYPT_METHODS[method](result)
        print(f"Encrypted {times} times:", result)

    elif mode == "2":
        method = input().strip().title()
        times = int(input())
        result = text
        for _ in range(times):
            if method == "Caesar":
                shift = int(input())
                result = caesar_encrypt(result, shift)
            elif method in ENCRYPT_METHODS:
                result = ENCRYPT_METHODS[method](result)
        print(f"Encrypted {times} times:", result)

    elif mode == "3":
        methods = list(ENCRYPT_METHODS.keys())
        random.shuffle(methods)
        result = text
        sequence = []
        for method in methods:
            if method == "Caesar":
                shift = random.randint(1, 25)
                result = caesar_encrypt(result, shift)
                sequence.append(f"Caesar({shift})")
            else:
                result = ENCRYPT_METHODS[method](result)
                sequence.append(method)
        print("Final ciphertext:", result)
        print("Sequence used:", " -> ".join(sequence))

    else:
        print("Unknown encrypt mode.")

def Dcrypt():
    print("\nDecrypt Modes:")
    print("1. Bruteforce (all methods)")
    print("2. Normal (choose methods)")
    mode = input("Select decrypt mode: ").strip()

    text = input("Enter text to decrypt: ")

    if mode == "1":
        print("\nBruteforce results:")
        for method, func in DECRYPT_METHODS.items():
            if method == "Caesar":
                for shift in range(1, 26):
                    print(f"Caesar({shift}): {caesar_decrypt(text, shift)}")
            else:
                print(f"{method}: {func(text)}")

    elif mode == "2":
        print("\nAvailable methods:", ', '.join(DECRYPT_METHODS.keys()))
        chosen = input("Choose methods (comma separated): ").strip().title().split(",")
        for method in chosen:
            method = method.strip()
            if method == "Caesar":
                shift = int(input("Enter Caesar shift (1-25): "))
                print(f"Caesar({shift}): {caesar_decrypt(text, shift)}")
            elif method in DECRYPT_METHODS:
                print(f"{method}: {DECRYPT_METHODS[method](text)}")
            else:
                print(f"Unknown method: {method}")

    else:
        print("Unknown decrypt mode.")

if choice == "0":
    Encrypt()
elif choice == "1":
    Dcrypt()
else:
    print("Invalid choice. Please select 0 for Encrypt or 1 for Dcrypt.")
    exit(1)