# ExDcrypt

## Overview
ExDcrypt is a Python-based tool for encryption, decryption, and file analysis. It supports multiple encryption methods, including Gzip, Bzip2, Hex, Base64, Binary, Morse, Caesar Cipher, Atbash Cipher, and ROT13. The tool offers various modes to apply these methods, such as single encryption, repeated encryption with a single method, or applying multiple different methods.

## Features
- **Encryption Modes**:
  - **Single**: Apply one encryption method to your input.
  - **Self Insecurity**: Apply a chosen method a random number of times.
  - **Insecurity**: Apply a chosen method a specific number of times.
  - **Untrust**: Apply different encryption methods sequentially.
  - **Paranoia**: (Not yet implemented) Apply all methods in sequence.
- **Decryption**: Supports decryption for all listed encryption methods (bruteforce mode not yet implemented).
- **File Analysis**: (Not yet implemented) Planned for text and file analysis.
- **User Interface**: Interactive CLI with a clear menu system and ASCII art banner.

## Requirements
- Python 3.13.7 and above
- Required Python libraries:
  - `pyfiglet`
  - `morse3`
- Standard Python libraries (included in Python):
  - `base64`
  - `codecs`
  - `random`
  - `string`
  - `itertools`
  - `os`
  - `msvcrt`
  - `gzip`
  - `bz2`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/BlankW100/ExDcrypt.git
   ```
2. Install the required dependencies:
   ```bash
   pip install pyfiglet morse3
   ```
3. Ensure you have Python 3.x installed.
4. Run the script:
   ```bash
   python exdcrypt.py
   ```

## Usage
1. Run the script to see the main menu with the following options:
   - **0. Encrypt**: Choose from various encryption modes and methods.
   - **1. Dcrypt**: Decrypt text using a chosen method.
   - **2. File Analyze**: (Not implemented) Analyze text or files.
   - **3. How this works??**: Display a brief explanation of the tool.
2. Follow the prompts to select modes, input text, and choose encryption/decryption methods.
3. After each operation, press 'M' to return to the main menu or any other key to exit.

## Example
To encrypt a string using Base64:
1. Select `0` (Encrypt) from the main menu.
2. Choose mode `0` (Single).
3. Select method `3` (Base64).
4. Enter your string (e.g., "Hello").
5. View the Base64-encoded result.

## Author
- **B1u3**

## License
<a href="https://github.com/BlankW100/ExDcrypt.git">ExDcrypt</a> © 2025 by <a href="https://github.com/BlankW100">Woon Yu Hern (B1u3_)</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">

## Notes
- The `Paranoia` and `Bruteforce` modes are not yet implemented.
- The `File Analyze` feature is currently a placeholder and not functional.
- The tool uses `msvcrt` for keypress detection, which is Windows-specific. To run on other platforms, replace `msvcrt.getch()` with a cross-platform alternative (e.g., `input()`).
- For GitHub hosting, ensure the script file is named `exdcrypt.py` and included in the repository alongside this README.
