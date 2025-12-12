import sys
import os
from tkinter import Tk, filedialog

# ========= Zero-Width Constants =========

zw0 = "\u200b"                                  # bit 0
zw1 = "\u200c"                                  # bit 1
seperators = {"\u200d", "\u2060", "\ufeff"}     # separators between chars


# ========= Simple Color Helper (ANSI) =========

class Color:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else: 
        os.system("clear")


# ========= Main ZWS Class =========

class ZWS:

    # ---------- File dialog helpers ----------

    def openFile(self, title="Select file"):
        root = Tk()
        root.withdraw()
        root.lift()
        root.attributes("-topmost", True)   # keep dialog on top

        filepath = filedialog.askopenfilename(
            parent=root,
            title=title,
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        root.destroy()
        return filepath

    def saveFile(self, title="Save file as"):
        root = Tk()
        root.withdraw()
        root.lift()
        root.attributes("-topmost", True)

        filepath = filedialog.asksaveasfilename(
            parent=root,
            title=title,
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        root.destroy()
        return filepath

    # ---------- CLI interface ----------

    def print_banner(self):

        print(Color.CYAN + "=" * 50 + Color.RESET)
        print(Color.BOLD + "   Zero-Width-Space Steganography Tool".center(50) + Color.RESET)
        print(Color.CYAN + "=" * 50 + Color.RESET)

    def print_menu(self):

        self.print_banner()
        print()
        print(f"{Color.BOLD}{Color.BLUE}Main Menu{Color.RESET}")
        print()
        print("  [1] Encode")
        print("  [2] Decode")
        print("  [3] Exit")
        print()

    def zws_main(self):

        while True:

            clear_screen()
            self.print_menu()

            choice = input(f"{Color.YELLOW}Select an option (1-3): {Color.RESET}").strip()

            if choice == "1":
                self.process()
                input(f"\nPress Enter to return to main menu...")

            elif choice == "2":
                self.reverse()
                input(f"\nPress Enter to return to main menu...")

            elif choice == "3":
                print("\nExiting... Goodbye!")
                sys.exit(0)

            else:
                print(f"{Color.RED}Invalid choice. Please enter 1, 2, or 3.{Color.RESET}")
                input("Press Enter to try again...")

    # ---------- Encode ----------

    def process(self):

        clear_screen()

        self.print_banner()
        print(f"{Color.BOLD}{Color.GREEN} ENCODE MODE {Color.RESET}")
        print()

        # Step 1: Cover file
        print(f"{Color.BLUE}[1/4]{Color.RESET} Select COVER file (visible text)")
        print("A file dialog will pop up. Choose the text file that will be the visible cover.\n")

        cover_path = self.openFile("Select COVER file (visible text)")
        
        if not cover_path:
            print(f"{Color.RED}❌ No cover file selected. Operation cancelled.{Color.RESET}")
            return

        # Step 2: Secret file
        print(f"\n{Color.BLUE}[2/4]{Color.RESET} Select SECRET file (hidden message)")
        print("Choose the text file that contains the secret message to hide.\n")

        secret_path = self.openFile("Select SECRET file (hidden text)")
        
        if not secret_path:
            print(f"{Color.RED}❌ No secret file selected. Operation cancelled.{Color.RESET}")
            return

        # Step 3: Output file
        print(f"\n{Color.BLUE}[3/4]{Color.RESET} Choose OUTPUT file")
        print("Select where to save the encoded result (new text file).\n")

        output_path = self.saveFile("Save encoded output as")
        
        if not output_path:
            print(f"{Color.RED}❌ No output file selected. Operation cancelled.{Color.RESET}")
            return

        # Step 4: Bit length
        print(f"\n{Color.BLUE}[4/4]{Color.RESET} Configure encoding")
        print("Recommended bit length: 7 (ASCII) or 8 (extended ASCII).")

        # Look here <--

        bit_length = int(input("Enter bit length (7 or 8): ").strip())

        # To here add execption for value error <--

        # From here <--

        print(f"\n{Color.YELLOW}⚙️ Encoding in progress...{Color.RESET}\n")

        with open(cover_path, 'r', encoding="utf-8") as opfile:
            cover = opfile.read()
        with open(secret_path, 'r', encoding="utf-8") as opfile:
            secret = opfile.read()

        secret_bits = self.text_to_bits(secret, bit_length)
        secret_zws = self.bits_to_zws(secret_bits)
        encoded_message = cover + secret_zws

        with open(output_path, 'w', encoding="utf-8") as opfile:
            opfile.write(encoded_message)

        print(f"{Color.GREEN}✅ Encoding complete!{Color.RESET}")
        print(f"Output file: {Color.BOLD}{output_path}{Color.RESET}")

        # To here add exception for any errors <--

    # ---------- Decode ----------

    def reverse(self):

        clear_screen()
    
        self.print_banner()
        print(f"{Color.BOLD}{Color.GREEN} DECODE MODE {Color.RESET}")
        print()

        # Step 1: Encoded cover file
        print(f"{Color.BLUE}[1/3]{Color.RESET} Select ENCODED COVER file")
        print("Choose the text file that contains the hidden message.\n")

        cover_path = self.openFile("Select ENCODED COVER file")

        if not cover_path:
            print(f"{Color.RED}❌ No encoded file selected. Operation cancelled.{Color.RESET}")
            return

        # Step 2: Output file
        print(f"\n{Color.BLUE}[2/3]{Color.RESET} Choose OUTPUT file for decoded secret")
        print("Select where to save the extracted secret text.\n")

        output_path = self.saveFile("Save decoded secret as")

        if not output_path:
            print(f"{Color.RED}❌ No output file selected. Operation cancelled.{Color.RESET}")
            return

        # Step 3: Bit length
        print(f"\n{Color.BLUE}[3/3]{Color.RESET} Bit length used during encoding")
        print("Use the same value as when you encoded (7 or 8 typically).")

        # From here <--

        bit_length = int(input("Enter bit length: ").strip())

        # To here add exception for ValueError

        print(f"\n{Color.YELLOW}🔎 Decoding in progress...{Color.RESET}\n")

        # From here <--

        with open(cover_path, 'r', encoding="utf-8") as opfile:
            cover = opfile.read()

        secret = self.decode_bits(cover, bit_length)

        with open(output_path, 'w', encoding="utf-8") as opfile:
            opfile.write(secret)

        print(f"{Color.GREEN}✅ Decoding complete!{Color.RESET}")
        print(f"Decoded secret saved to: {Color.BOLD}{output_path}{Color.RESET}")

        # To here add exception for all errors

# Helper Functions

    def text_to_bits(self, secret, bit_length): # turn our secret message into bits and group them into 7 or 8 bit-length
        
        secret_bits = [] # secret message in binary format

        for char in secret:

            bits = format(ord(char), f"0{bit_length}b") # turns char into an integer then formats into binary and adds leading zeros if the resulted bit-length is less than size
            secret_bits.append(bits)

        return secret_bits

    def bits_to_zws(self, secret_bits):

        secret_zws = ""
        seperators = "\u200d"

        for i, bits in enumerate(secret_bits): # Loops through the list of character which are in binary format (secret_bits)
            for bit in bits: # Loops through bits of the character 

                if bit == "0": secret_zws += zw0    # If the bit = 0 then append zw0
                elif bit == "1": secret_zws += zw1  # If the bit = 1 then append zw1
            
            if i < len(secret_bits) - 1: # If we still have more characters in the list to encode then add a seperator

                secret_zws += seperators

        return secret_zws

    def decode_bits(self, text, bit_length):
        
        secret_zws = ""

        for char in text:
            if ((char == zw0) or (char == zw1) or (char in seperators)): # If char is any of the zero-width-space characters extract them into a new string

                secret_zws += char

        chunks = []             # List of chunks (7 or 8 bit length)
        current_chunk = ""      # Current chunk being extracted from the entire zws string

        for char in secret_zws: # Loop through the extracted zws string

            if char in seperators: # If the char is a seperator append the current chunk into the list of chunks

                chunks.append(current_chunk)
                current_chunk = ""

            else:

                current_chunk += char # Add any zws character that isnt a seperator into the current chunk

        if current_chunk: # Append the last chunk into the list of chunks
            chunks.append(current_chunk)

        bits_to_text = "" # Holds the hidden message

        for chunk in chunks:

            if len(chunk) != bit_length: # Skips any chunk with the incorrect bit_length
                
                print(f"⚠️ Warning: Skipping chunk with invalid size: {len(chunk)} bits (expected {bit_length})")
                continue

            bits = "" # Placeholder for a chunk converted into bit format

            for char in chunk:

                if char == zw0: bits += "0"
                elif char == zw1: bits += "1"

            bits_to_text += chr(int(bits, 2)) # Convert binary into integer then turned into a character

        return bits_to_text


# ========= Entry point =========

if __name__ == "__main__":
    zws_tool = ZWS()
    zws_tool.zws_main()


