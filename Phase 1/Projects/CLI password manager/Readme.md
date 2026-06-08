# 🔐 CLI Password Manager

A secure, fast, and simple Command Line Interface (CLI) password manager written in Python. 

This tool allows users to create a master account and securely store their passwords for different websites or applications. It uses **Fernet symmetric encryption** to ensure that even if someone opens the data file, they cannot read your stored passwords.

## ✨ Features
* **Secure Login & Sign Up:** Uses `hashlib` to hash your master password.
* **Strong Encryption:** Uses the `cryptography.fernet` module to encrypt stored passwords.
* **Local Storage:** Safely saves your encrypted data in a local `password.json` file.
* **Manage Passwords:** Add, Retrieve, List, and Delete passwords directly from your terminal.
* **Hidden Inputs:** Uses the `getpass` module so your master password is never shown on the screen while typing.

## ⚙️ Prerequisites

Before running this project, you need to have Python installed on your system. You also need to install the required external library for encryption.

Open your terminal and run:
```bash
pip install cryptography