
from colorama import init, Fore, Back, Style
import pyfiglet

# Initialize colorama
init(autoreset=True)


def print_banner():
    banner = pyfiglet.figlet_format("FlexiCrypt", font="slant")
    print(Fore.MAGENTA + banner)
    print(Fore.CYAN + "="*80)
    print(Fore.YELLOW + "Welcome to FlexiCrypt! Encrypt/Encode or Decrypt/Decode your data securely.")
    print(Fore.CYAN + "="*80 + "\n")

def print_main_menu():
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " RSA Encryption / Decryption")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Zero Width Space Encoding / Decoding")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")
def print_rsa_menu():
    print(Fore.YELLOW + "RSA Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Create Key")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Encrypt")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Decrypt")
    print(Fore.CYAN + "[4]" + Style.BRIGHT + " Exit")
def print_output__key_options():
    print(Fore.YELLOW + "Output Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Display keys(Terminal)")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Save keys to file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")
def print_input_options():
    print(Fore.YELLOW + "Input Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Write or Paste(Terminal)")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Load from file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")
def print_key_file():
    key_file = input(Fore.YELLOW + "Enter public key file path: " + Fore.CYAN)
    return key_file
def print_publickey_privatekey(public_key = None, private_key = None):
    print(Fore.YELLOW + "\nPublic Key:\n")
    print(Fore.CYAN + public_key)
    print(Fore.YELLOW + "Private Key:\n")
    print(Fore.CYAN + private_key)
def print_key_input_options():
    print(Fore.YELLOW + "Key Input Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Write or Paste(Terminal)")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Load from file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")
def print_save_keys_options():
        print(Fore.YELLOW + "\nKeys saving operation")
        print(Fore.CYAN + "[1]" + Style.BRIGHT + " Single file (public + private)")
        print(Fore.CYAN + "[2]" + Style.BRIGHT + " Separate files (public, private)")
        print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")
def print_public_key_input(prompt_color=Fore.YELLOW, input_color=Fore.CYAN):
    lines = []
    print(prompt_color + "Paste the public key (blank line to finish):")
    while True:
        line = input(input_color)
        if line.strip() == "":
            break
        lines.append(line)
    return lines
def print_input_normal(prompt = None):
    return input(Fore.YELLOW + prompt + Fore.CYAN)
    

def print_exit():
    print(Fore.YELLOW + "Exit. Thank You!")


def print_separator():
    print(Fore.BLUE + "-"*80)

def print_success(message):
    print(Fore.GREEN + "[SUCCESS] " + message)

def print_error(message):
    print(Fore.RED + "[ERROR] " + message)

def print_info(message):
    print(Fore.YELLOW + "[INFO] " + message)

def input_cli(prompt = "Choose an option: "):
    return int(input(Fore.YELLOW + prompt + Fore.CYAN).strip())

from colorama import Fore, Style

def print_error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)

def print_prompt(msg):
    print(Fore.CYAN + msg + Style.RESET_ALL, end="")

def secure_input(prompt = None, valid_choices = None, attempts=3):

    for i in range(attempts):
        choice = input_cli(prompt)
        if choice:
            choice_int = int(choice)
            if choice_int in valid_choices:
                return choice_int
        print(Fore.RED + f"Invalid choice! ({attempts - i - 1} attempts left)" + Style.RESET_ALL)
    print(Fore.RED + "Too many invalid attempts. Exiting..." + Style.RESET_ALL)
    exit()


