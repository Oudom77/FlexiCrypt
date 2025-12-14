import sys
import os
from FlexiCrypt import *
from color import*
from tkinter import Tk, filedialog

# ========= Zero-Width Characters =========

zw0 = "\u200b"                                  # bit 0
zw1 = "\u200c"                                  # bit 1
seperators = {"\u200d", "\u2060", "\ufeff"}     # separators between characters

# =========  ZWS Class =========

class ZWS(FlexiCryptSystem):

 # ========== MAIN MENU ==========

    def zws_main(self):

        while True:

            self.clear_screen()
            print_zws_menu()
            operation = secure_input("Choose an option: ", [1, 2, 3])
            if operation == 1:
                self.process()
                input(f"\nPress Enter to return to main menu...")

            elif operation == 2:
                self.reverse()
                input(f"\nPress Enter to return to main menu...")

            elif operation == 3:
                break
           

    # ========== Encode ==========

    def process(self):

        self.clear_screen()

        print_zws_banner()
        print_mode("ENCODE MODE")

        # Prompt for user's input
        # Step 1: Cover file
       
        print_step("[1/4]", " Select COVER file (visible text)")
        print("A file dialog will pop up. Choose the text file that will be the visible cover.\n")

        cover_path = self.openFile("Select COVER file (visible text)")
        
        if not cover_path:
            print_error("❌ No cover file selected. Operation cancelled.")
            return

        # Step 2: Secret file
        print_step("[2/4]", " Select SECRET file (hidden message)")
        print("Choose the text file that contains the secret message to hide.\n")

        secret_path = self.openFile("Select SECRET file (hidden text)")
        
        if not secret_path:
            print_error("❌ No secret file selected. Operation cancelled.")
            return

        # Step 3: Output file
        print_step ("[3/4]", " Choose OUTPUT file")
        print("Select where to save the encoded result (new text file).\n")

        output_path = self.saveFile("Save encoded output as")
        
        if not output_path:
            print_error("❌ No output file selected. Operation cancelled.")
            return

        # Step 4: Bit length
        print_step("[4/4]", " Configure encoding")
        print("Recommended bit length: 7 (ASCII) or 8 (extended ASCII).")

        # Add execption for value error below

        while True: 
            try:
                bit_length = int(print_input_normal("Enter bit length (7 or 8): ").strip())
                if bit_length not in (7, 8):
                    raise ValueError("Bit length must be 7 or 8")
                break
            except ValueError:
                print_error("❌ Invalid Bit length! Try again.")

        # Add exception for any errors below

        try:
            print_info("⚙️ Encoding in progress...\n")

            with open(cover_path, 'r', encoding="utf-8") as opfile:
                cover = opfile.read()

            with open(secret_path, 'r', encoding="utf-8") as opfile:
                secret = opfile.read()

            secret_bits = self.text_to_bits(secret, bit_length) # Convert the secret into binary/bits
            secret_zws = self.bits_to_zws(secret_bits) # Convert the bits from above into ZWS characters
            encoded_message = cover + secret_zws # The final encoded message is the cover + the hidden message converted as ZWS characters

            with open(output_path, 'w', encoding="utf-8") as opfile:
                opfile.write(encoded_message)

            print_success("✅ Encoding complete!")
            print_file_path("Output file: ",output_path)
           
        except Exception as e:
            print_error (f"❌ Encoding failed: {e}")

    # ========== Decode ==========

    def reverse(self):

        self.clear_screen()
    
        print_zws_banner()
        print_mode("DECODE MODE")
        print()

        # Prompts for user's input
        # Step 1: Encoded cover file
        print_step("[1/3]", " Select ENCODED COVER file")
        print("Choose the text file that contains the hidden message.\n")

        cover_path = self.openFile("Select ENCODED COVER file")

        if not cover_path:
            print_error("❌ No encoded file selected. Operation cancelled.")
            return

        # Step 2: Output file
        print_step("[2/3]", " Choose OUTPUT file for decoded secret")
        print("Select where to save the extracted secret text.\n")

        output_path = self.saveFile("Save decoded secret as")

        if not output_path:
            print_error("❌ No output file selected. Operation cancelled.")
            return

        # Step 3: Bit length
        print_step("[3/3]", " Bit length used during encoding")
        print("Use the same value as when you encoded (7 or 8 or 0[AUTO]).")

        # add exception for ValueError below

        while True:
            try:
                bit_length = int(print_input_normal("Enter bit length (7 or 8 or 0[AUTO]): ").strip())
                
                if bit_length not in (7, 8, 0):
                    raise ValueError("Bit length must be 7 or 8 or 0[AUTO]")
                break

            except ValueError:
                print_error("❌ Invalid Bit length! Try again.")

        with open(cover_path, 'r', encoding="utf-8") as opfile:
                cover = opfile.read()

        if bit_length == 0: # IF 0 then use auto_bit_length function

            print_info("Auto-detecting bit length...")

            bit_length = self.auto_bit_length(cover)
            print_success(f"✅ Auto-detected bit length: {bit_length}")

            print()

        # add exception for all errors

        try:
            print_info("🔎 Decoding in progress...")

            secret = self.decode_bits(cover, bit_length) # Decode to see the hidden message

            with open(output_path, 'w', encoding="utf-8") as opfile: # Write the into the output file
                opfile.write(secret)

            print_success("✅ Decoding complete!")
            print_file_path("Decoded secret saved to: ",output_path)

        except Exception as e:
            print_error(f"❌ Decoding failed: {e}")


    #========== Helper Functions ==========

    def text_to_bits(self, secret, bit_length): 

        # turn our secret message into bits and group them into 7 or 8 bit-length
        
        # secret message in binary format
        secret_bits = [] 

        for char in secret:

            bits = format(ord(char), f"0{bit_length}b") # turns char into an integer then formats into binary and adds leading zeros if the resulted bit-length is less than size
            secret_bits.append(bits)

        return secret_bits

    def bits_to_zws(self, secret_bits):

        # Convert the bits(1 & 0) into ZWS characters and add seperators for each chunk

        secret_zws = ""
        seperators = "\u200d"
        
        # Loops through the list of character which are in binary format (secret_bits)
        for i, bits in enumerate(secret_bits): 
            # Loops through bits of the character
            for bit in bits: 

                if bit == "0": secret_zws += zw0    # If the bit = 0 then append zw0
                elif bit == "1": secret_zws += zw1  # If the bit = 1 then append zw1
            
            # If we still have more characters in the list to encode then add a seperator, if not skip adding a seperator
            if i < len(secret_bits) - 1: 

                secret_zws += seperators

        return secret_zws

    def decode_bits(self, text, bit_length):
        
        secret_zws = ""

        # If a character is any of the zero-width-space characters extract them into a new string to decode below
        for char in text:
            if ((char == zw0) or (char == zw1) or (char in seperators)): 

                secret_zws += char

        # List of chunks (7 or 8 bit length)
        chunks = []
        # Current chunk being extracted from the entire zws string         
        current_chunk = ""

        # Loop through the extracted zws string
        for char in secret_zws:

            # If the current character is any of the seperators append the current chunk into the list of chunks
            if char in seperators: 

                chunks.append(current_chunk)
                current_chunk = "" # Reset the current chunk

            else:
                
                # Add any zws character that isnt a seperator into the current chunk
                current_chunk += char 

        # Append the last chunk into the list of chunks
        if current_chunk: 
            chunks.append(current_chunk)

        # Holds the hidden message
        bits_to_text = "" 

        for chunk in chunks:

            # Skips any chunk with the incorrect bit_length
            if len(chunk) != bit_length: 
                
                print(f"⚠️ Warning: Skipping chunk with invalid size: {len(chunk)} bits (expected {bit_length})")
                continue
            
            # Placeholder for a chunk converted into bit format
            bits = ""

            for char in chunk:

                if char == zw0: bits += "0"
                elif char == zw1: bits += "1"

            # Convert binary into an integer then turn it into a character which is added to the final string
            bits_to_text += chr(int(bits, 2)) 

        return bits_to_text # resulted decoded message
    
    
    def auto_bit_length(self, cover_text):
    
        # Auto-detect whether the hidden message was encoded using 7-bit or 8-bit.
        # We detect based on chunk sizes
        # Returns: 7 or 8
    

        # Extract only zero-width characters and separators from the cover text
        secret_zws = ""
        for char in cover_text:
            if char == zw0 or char == zw1 or char in seperators:
                secret_zws += char

        # Split into chunks using separators (each chunk = one encoded char)
        chunks = []
        current = ""

        for char in secret_zws:
            if char in seperators: # If we detect a seperator append the current chunk into the list of chuncks

                if current: # avoid adding empty chunks
                    chunks.append(current)

                current = "" # Reset current chunk after adding into the list of chunks

            else:
                current += char

        # If the last chunk is not empty add it into the list of chunks
        if current: 
            chunks.append(current)

        # Count how many chunks match 7 vs 8
        valid7 = 0
        valid8 = 0

        for c in chunks:

            if len(c) == 7:

                valid7 += 1

            elif len(c) == 8:
                
                valid8 += 1

        # Decide if more chunks are 8 bits, choose 8; otherwise choose 7.
        return 8 if valid8 > valid7 else 7



# ========= Entry point =========

if __name__ == "__main__":
    zws_tool = ZWS()
    zws_tool.zws_main()


