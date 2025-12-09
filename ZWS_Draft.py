zw0 = "\u200b"                                  # bit 0
zw1 = "\u200c"                                  # bit 1
seperators = {"\u200d", "\u2060", "\ufeff"}     # space

class ZWS():

    def zws_main(self):

        print("\nZero-Width-Space Stegonagraphy Tool\n")
        print("\n1. Encode")
        print("\n2. Decode")
        print("\n3. Exit")

        choice = int(input("\nEnter your choice: "))

        match (choice):

            case 1: self.process()
            case 2: self.reverse()
            case 3: print("Exiting Zero-Width-Space stegonagraphy tool...")
            case _: print("Invalid input, select choice (1-3)")

    def process(self):
        
        # Prompt the user for file path and bit length

        cover_path = input("Enter the cover file path: ")
        secret_path = input("Enter the secret file path: ")
        output_path = input("Enter the ouput file path: ")
        bit_length = int(input("Enter the bit length: "))

        with open(cover_path, 'r', encoding = "utf-8") as opfile: # Utf-8 is required for zero-width space character
            cover = opfile.read()
        with open(secret_path, 'r', encoding = "utf-8") as opfile: 
            secret = opfile.read()

        secret_bits = self.text_to_bits(secret, bit_length) # converts the secret message into bits
        secret_zws = self.bits_to_zws(secret_bits) # converts the secret_bits into zero width space format

        encoded_message = cover + secret_zws # combine the cover with the hidden zero width space message

        with open(output_path, 'w', encoding = "utf-8") as opfile:

            opfile.write(encoded_message)

        print("Encoding complete.")
        print(f"File has been written to: {output_path}")


    def reverse(self):

        cover_path = input("Enter the cover file path: ")
        output_path = input("Enter the output path: ")
        bit_length = int(input("Enter the bit length: "))

        with open(cover_path, 'r', encoding = "utf-8") as opfile:
            cover = opfile.read()

        secret = self.decode_bits(cover, bit_length)

        with open(output_path, 'w', encoding = "utf-8") as opfile:
            opfile.write(secret)

        print("Dencoding complete.")
        print(f"File has been written to: {output_path}")


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

    def decode_bits(self, text, size):
        
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

            bits = "" # Placeholder for a chunk converted into bit format

            for char in chunk:

                if char == zw0: bits += "0"
                elif char == zw1: bits += "1"

            bits_to_text += chr(int(bits, 2)) # Convert binary into integer then turned into a character

        return bits_to_text
            

zws1 = ZWS()
zws1.zws_main()