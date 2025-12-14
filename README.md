# FlexiCrypt

# RSA Encryption Module

## Overview
The RSA module is part of the **FlexiCrypt** project.  
It provides **public-key encryption and decryption** for securing text and files using the RSA cryptographic algorithm.

This module allows users to:
- Generate RSA key pairs
- Encrypt text or files using a public key
- Decrypt encrypted data using a private key

---

## Features
- RSA key pair generation (configurable key size)
- Public key encryption
- Private key decryption
- Supports text and file-based encryption
- Save and load RSA keys from files
- Menu-driven command-line interface

---

## Requirements
- Python 3.x
- Required files:
  - `FlexiCrypt.py`
  - `color.py`
  - `RSA.py`
- Required Python libraries:
  - `rsa`

Install the RSA library if needed:
```bash
pip install rsa
```

# Zero-Width Space (ZWS) Steganography Module

## Overview
The Zero-Width Space (ZWS) module is part of the **FlexiCrypt** project.  
It allows users to hide secret messages inside normal text files using invisible Unicode characters without changing the visible content of the text.

The module supports both **manual encoding/decoding** and **automatic bit-length detection**.


## Features
- Hide secret messages inside text files using zero-width Unicode characters
- Supports **7-bit** and **8-bit** encoding
- Automatic bit-length detection during decoding
- File-based input and output
- Simple command-line interface with file selection GUI


## Requirements
- Python 3.x
- Required files:
  - `FlexiCrypt.py`
  - `color.py`
  - `ZWS.py`


## How to Run
From the project directory, run:

```bash
python ZWS.py
