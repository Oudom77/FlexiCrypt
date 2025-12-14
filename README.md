# FlexiCrypt

## Overview
**FlexiCrypt** is a Python-based command-line security tool that provides two different methods for protecting text-based data:

- **RSA Cryptography** – strong encryption for confidentiality  
- **Zero-Width Space (ZWS) Steganography** – hidden communication inside normal text  

The system allows users to choose the appropriate security technique based on different security requirements, demonstrating both encryption and information hiding concepts.

---

## Features
- Modular security system design  
- RSA public-key encryption and decryption  
- Zero-Width Space (ZWS) text steganography  
- Menu-driven command-line interface  
- File-based input and output  
- Automatic bit-length detection for ZWS decoding  
- Extensible architecture for future security methods  

---

## Project Structure

```
FlexiCrypt/
│
├── CODE/
│   └── FlexiCryptSystem/
│       ├── main.py              # Program entry point
│       ├── FlexiCrypt.py        # Core system controller
│       ├── RSA.py               # RSA key generation, encryption & decryption
│       ├── ZWS.py               # Zero Width Space encoding/decoding
│       ├── FileHandling.py      # Read/write file utilities
│       └── color.py             # Terminal color formatting
│
├── FILE/
│   ├── plaintext.txt            # Original message
│   ├── encrypt.txt              # Encrypted output
│   ├── decrypt.txt              # Decrypted output
│   ├── encode.txt               # ZWS encoded text
│   ├── decode.txt               # ZWS decoded text
│   ├── secret.txt               # Hidden message for ZWS
│   └── cover.txt                # Cover text for steganography
│
├── KEY/
│   ├── publickey.txt            # RSA public key
│   ├── privatekey.txt           # RSA private key
│   └── key.txt                  # Key storage reference
│
└── README.md
```
---

## Requirements
- Python 3.x  
- Required Python libraries:
  - `os`
  - `sys`
  - `rsa`
  - `colorama`
  - `pyfiglet`
  - `tkinter` (usually included with Python)

Install required libraries if needed:
```bash
pip install rsa colorama pyfiglet
```
## How to Run
From the project directory, run:

```bash
python main.py
```

