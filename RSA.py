from FlexiCrypt import *

class RSA(FlexiCryptSystem):
    def __init__(self, key_size=512, input_file=None, output_file=None, private_key=None, public_key=None):
        if input_file or output_file:
            super().__init__(input_file=input_file, output_file=output_file)
        if key_size:
            self.key_size = key_size
        if private_key:
            self.private_key = private_key
        if public_key:
            self.public_key = public_key

    def generate_keys(self):
        try:
            public_key, private_key = newkeys(self.key_size)
            if not public_key or not private_key:
                raise ValueError("Cannot generate keys.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            self.public_key = public_key
            self.private_key = private_key
            return public_key, private_key
        

    def process(self, public_key, message):
        return encrypt(message.encode(), public_key)

    def reverse(self, ciphertext):
        return decrypt(ciphertext, self.private_key).decode()

    def save_keys(self, public_key, private_key):
        print_save_keys_options()
        choice = secure_input("Choose an option: ", [1,2,3])

        if choice == 1:
            file_path = FlexiCryptSystem().openFile(title = "Select File To Store (Public Key + Private Key)")
            with open(file_path, "w") as f:
                f.write(public_key)
                f.write("\n")
                f.write(private_key)
            print_success(f"Keys saved to {file_path}")

        elif choice == 2:
            pub_file = FlexiCryptSystem().openFile(title = "Select File To Store Public Key")
            priv_file = FlexiCryptSystem().openFile(title = "Select File To Store Private Key")
            with open(pub_file, "w") as f:
                f.write(public_key)
            with open(priv_file, "w") as f:
                f.write(private_key)
            print_success(f"Public key saved to {pub_file}")
            print_success(f"Private key saved to {priv_file}")
        else:
            print_error("Invalid choice, keys not saved.")