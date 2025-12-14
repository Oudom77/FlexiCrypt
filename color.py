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


def print_file_path(message, path):
    print(Fore.YELLOW + message + Style.BRIGHT + path)


def input_cli(prompt = "Choose an option: "):
    try:
        option_input = int(input(Fore.YELLOW + prompt + Fore.CYAN).strip())
    except Exception as e:
        print_error(f"Error: {e}")
    else:
        return option_input

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


#-----------------------RSA------------------------------------

def print_rsa_menu():
    print(Fore.CYAN + "="*80)
    print(Fore.YELLOW + "RSA".center(80))
    print(Fore.CYAN + "="*80 + "\n")
    print(Fore.YELLOW + Style.BRIGHT + "RSA Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Create Key")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Encrypt")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Decrypt")
    print(Fore.CYAN + "[4]" + Style.BRIGHT + " Exit")

def print_output_key_options():
    print(Fore.YELLOW + "Output Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Display keys(Terminal)")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Save keys to file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")

def print_input_options():
    print(Fore.YELLOW + "Input Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Write or Paste(Terminal)")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Load from file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")

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

def print_public_key_input(prompt_color=Fore.YELLOW, input_color=Fore.CYAN):
    lines = []
    print(prompt_color + "Paste the public key (blank line to finish):")
    while True:
        line = input(input_color)
        if line.strip() == "":
            break
        lines.append(line)
    return lines

def print_private_key_input(prompt_color = Fore.YELLOW, input_color = Fore.CYAN):
    lines = []
    print(prompt_color + "Paste the private key (blank line to finish):")
    while True:
        line = input(input_color)
        if line.strip() == "":
            break
        lines.append(line)
    return lines

def print_output_encrypt_options():
    print(Fore.YELLOW + "Output Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Display ciphertext")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Save ciphertext as binary file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")

def print_output_decrypt_options():
    print(Fore.YELLOW + "Output Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Display plaintext")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Save plaintext as text file")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")



#----------------------ZWS----------------------------

def print_zws_banner():
    print(Fore.CYAN + "="*80)
    print(Fore.YELLOW + "Zero-Width-Space Steganography Tool".center(80))
    print(Fore.CYAN + "="*80 + "\n")

def print_zws_menu():
    print_zws_banner()
    print(Fore.YELLOW + Style.BRIGHT+ "ZWS Menu")
    print(Fore.CYAN + "[1]" + Style.BRIGHT + " Encode")
    print(Fore.CYAN + "[2]" + Style.BRIGHT + " Decode")
    print(Fore.CYAN + "[3]" + Style.BRIGHT + " Exit")  

def print_mode(message):
    print(Fore.GREEN + Style.BRIGHT + message + "\n")

def print_step(step, message):
    print(Fore.CYAN + step + Fore.RESET + message)   