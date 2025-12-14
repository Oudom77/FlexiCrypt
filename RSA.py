from FlexiCrypt import * #Import everthing in FlexiCrypt.py
from color import * #Import everthing in FlexiCrypt.py

#Define a class call RSA inherit from base class FlexiCryptSystem
class RSA(FlexiCryptSystem):
    #Define a parameterized constructor
    def __init__(self, key_size=512, input_file=None, output_file=None, private_key=None, public_key=None):
        if input_file or output_file:
            super().__init__(input_file=input_file, output_file=output_file)
        if key_size:
            self.key_size = key_size
        if private_key:
            self.private_key = private_key
        if public_key:
            self.public_key = public_key
    #Define a method call generate_key to generate public and private key in RSA
    def generate_keys(self):
        #Using try, except, else to handle error
        try:
            #Generate keys using newske method in rsa library
            public_key, private_key = newkeys(self.key_size)
            if not public_key or not private_key:
                raise ValueError("Cannot generate keys.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            self.public_key = public_key
            self.private_key = private_key
            return public_key, private_key
    #Define a method call process for encryption in RSA
    def process(self, message):
        #Using encrypt method in rsa library to encrypt plaintext by using public key
        return encrypt(message.encode(), self.public_key)
    #Define a method call reverse for decryption in RSA
    def reverse(self, ciphertext):
        #Using decrypt method in rsa library to decrypt ciphertext by using private key
        return decrypt(ciphertext, self.private_key).decode()
    #Define a method call save_keys for key saving options
    def save_keys(self, public_key, private_key):
        #Print save keys to file(s) options menu
        print_save_keys_options()
        #Let user choose save keys options
        choice = secure_input("Choose an option: ", [1,2,3])
        #User choose to save public key and private key in the same file
        if choice == 1:
            #Using try, except, else to handle error
            try:
                #It will pop file explorer window to let user choose file to save public key and private key
                file_path = FlexiCryptSystem().openFile(title = "Select File To Store (Public Key + Private Key)")
            except Exception as e:
                print_error(f"Error: {e}")
            else:    
                #Write public key and private key in a file seperate by new line
                with open(file_path, "w") as f:
                    f.write(public_key)
                    f.write("\n")
                    f.write(private_key)
                #Print to let user know ke saving is success
                print_success(f"Keys saved to {file_path} success.")
        #User choose to save public key and private key in the different files
        elif choice == 2:
            #Using try, except, else to handle error
            try:
                #It will pop file explorer window to let user choose file to save public key
                pub_file = FlexiCryptSystem().openFile(title = "Select File To Store Public Key")
                #It will pop file explorer window to let user choose file to save private key
                priv_file = FlexiCryptSystem().openFile(title = "Select File To Store Private Key")
            except Exception as e:
                print_error(f"Error: {e}")
            else:
                #Write public key in a file
                with open(pub_file, "w") as f:
                    f.write(public_key)
                #Write private key in a file
                with open(priv_file, "w") as f:
                    f.write(private_key)
                #Print to let user know ke saving is success
                print_success(f"Public key saved to {pub_file} success.")
                print_success(f"Private key saved to {priv_file} success.")
        else:
            #Print to let user know key is not save because invalid choice from user
            print_error("Invalid choice, keys not saved.")
#Define a method cal rsa_main. This is the main of RSA encrypt or decrypt method
def rsa_main():
    #Use while loop to make loop always run for user
    while True:
            #Print the RSA menu
            print_rsa_menu()
            #Let user choose rsa menu options
            operation = secure_input("Choose an option: ", [1, 2, 3, 4])
            #If user choose create key
            if operation == 1:
                #Use while loop to make loop always run for user
                while True:
                    #Using try, except, else and finally to handle error
                    try:
                        #Let user choose size of key from 2048 to 4096
                        size = int(print_input_normal("Enter the key size(2048-4096): "))
                        print(Style.RESET_ALL, end = "") #Reset the color of style
                        #Raise ValueError if not in range 2048 to 4096
                        if size not in range(2048, 4097):
                            raise ValueError()
                        #Create an object of RSA with the key size
                        rsa_obj = RSA(key_size = size)
                        #Generate public and private key
                        pub, priv = rsa_obj.generate_keys()
                        #Use save_pkcs1() to convert key into RSA format (return as bytes) then use decode() to convert bytes to readable key
                        pub_pem = pub.save_pkcs1().decode()
                        priv_pem = priv.save_pkcs1().decode()
                    #Print the ValueError
                    except ValueError:
                        print_error("Invalid size! Try again.")
                        continue
                    #Print success if key generate success
                    else:
                        print_success("Key generate success.")
                    #Print to let user know key generate process is completed
                    finally:
                        print_info("Key generate completed.")
                    #Using try, except, else and finally to handle error
                    try:
                        #Print the output key menu
                        print_output_key_options()
                        #Let user choose output key menu options
                        out_choice = secure_input("Choose an option: ", [1, 2, 3])
                    #Print Error
                    except Exception as e:
                        print_error(f"Error: {e}")
                    #Do next step if code in try block is not error
                    else:
                        #If user chooose display key in terminal
                        if out_choice == 1:
                            #Using try, except, else to handle error
                            try:
                                #Print the public key and private key
                                print_publickey_privatekey(pub_pem, priv_pem)
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Print success if nothing error in try block
                            else:
                                print_success("Key display success.")
                        #If user choose save key to file
                        elif out_choice == 2:
                            #Using try, except, else to handle error
                            try:
                                #Call save_keys method to let user choose key saving options
                                rsa_obj.save_keys(pub_pem, priv_pem)
                            #Print Error
                            except Exception as e:  
                                print_error(f"Error: {e}")
                            #Print success if nothing error in try block
                            else:
                                print_success("Key save to file success.")
                        #If user choose exit
                        elif out_choice == 3:
                            print_exit() #Print exit message
                            break
                        #If user choose wrong options
                        else:
                            print_error("Invalid choice.")
                            continue
                    #Always run the code
                    finally:
                        #If user choose to display key
                        if out_choice == 1:
                            print_info("Key display process completed")
                        #If user choose to save key to file(s)
                        elif out_choice == 2:
                            print_info("Key save to file process completed")
                    #Break the loop to go to main menu
                    break
            #If user choose encrypt
            elif operation == 2:
                #Use while loop to make loop always run for user
                while True:
                    #Using try, except, else and finally to handle error
                    try:
                        #Print the input key menu
                        print_key_input_options()
                        #Let user choose input key menu options
                        key_choice = secure_input("Choose an option: ", [1, 2, 3])
                    #Print Error
                    except Exception as e:
                        print_error(f"Error: {e}")
                    #Do next step if code in try block is not error
                    else:
                        #If user choose input key by paste in terminal
                        if key_choice == 1:
                            #Using try, except, else to handle error
                            try:
                                #Let user input key in terminal
                                lines = print_public_key_input()
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Do next step if code in try block is not error
                            else:
                                #Save public key to a variable
                                pub_key = PublicKey.load_pkcs1("\n".join(lines).encode())
                                #Tell user public key input is success
                                print_success("Key input success.")
                        #If user choose load key from file
                        elif key_choice == 2:
                            #Using try, except, else to handle error
                            try:
                                #It will pop file explorer window to let user choose the public key input file
                                key_file = FlexiCryptSystem().openFile("Select Public Key file")
                                #Open file to read the public key
                                with open(key_file, "r") as f:
                                    pub_key = PublicKey.load_pkcs1(f.read().encode())
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Do next step if code in try block is not error
                            else:
                                #Print success to let user know that ke input is success
                                print_success("Key input success.")
                        #If user choose exit print exit then break
                        elif key_choice == 3:
                            print_exit()
                            break
                        #If user choose invalid choice
                        else:
                            print_error("Invalid choice.")
                            continue
                    #Always run this code
                    finally:
                        #Print to let user know that key input process is completed
                        print_info("Key input completed.")
                    #Using try, except, else and finally to handle error
                    try:
                        #Create an object from RSA class with public key attribute
                        rsa_obj = RSA(public_key = pub_key)
                    #Print Error
                    except Exception as e:
                        print_error(f"Error: {e}")
                    #Do next step if code in try block is not error
                    else:
                        #Using try, except, else to handle error
                        try:
                            #Print plaintext input options menu
                            print_input_options()
                            #Let user choose plaintext input options menu options
                            input_type = secure_input("Choose an option: ", [1, 2, 3])
                        #Print Error
                        except Exception as e:
                            print_error(f"Error: {e}")
                        #Do next step if code in try block is not error
                        else:
                            #If user choose input plaintext in terminal
                            if input_type == 1:
                                #Using try, except, else to handle error
                                try:
                                    #Let user input the plaintext
                                    text = print_input_normal("Enter text to encrypt: ")
                                    print(Style.RESET_ALL, end = "")
                                #Print Error
                                except Exception as e:
                                    print_error(f"Error: {e}")
                                #Do next step if code in try block is not error
                                else:
                                    #Encrypt process using public key and plaintext
                                    cipher = rsa_obj.process(text)
                                    #Print to let user know that encrypt from text is success
                                    print_success("Encrypted from text success.")
                            #If user choose load plaintext from file
                            elif input_type == 2:
                                #Using try, except, else to handle error
                                try:
                                    #Let user choosing plaintext file from file explorer
                                    in_file = FlexiCryptSystem().openFile()
                                    print(Style.RESET_ALL, end = "")
                                #Print Error
                                except Exception as e:
                                    print_error(f"Error: {e}")
                                #Do next step if code in try block is not error
                                else:
                                    #Read plaintext from input file
                                    rsa_obj.input_file = in_file
                                    data = rsa_obj.read_file()
                                    #Encrypt the plaintext that read from input file
                                    cipher = rsa_obj.process(data)
                                    #Print to let user know that encrypt from file is success
                                    print_success("Encrypted from file success.")
                            #If user choose exit print exit message then break
                            elif input_type == 3:
                                print_exit()
                                break
                            #If user choose invalid choice
                            else:
                                print_error("Invalid choice.")
                                continue
                            #Using try, except, else to handle error
                            try:
                                #Print output encrypt menu
                                print_output_encrypt_options()
                                #Let user choose output encrypt menu options
                                output_choice = secure_input("Choose an option: ", [1, 2, 3])
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Do next step if code in try block is not error
                            else:  
                                #If user choose to display ciphertext in terminal 
                                if output_choice == 1:
                                    #Display the ciphertext in terminal
                                    print(Fore.YELLOW + f"Ciphertext bytes: ", end = "")
                                    print(Fore.CYAN + f"{cipher}")
                                    print(Style.RESET_ALL, end = "")
                                    #Print to let user know display is success
                                    print_success(f"Encrypted binary display success.")
                                #If user choose to save ciphertext as binary file
                                elif output_choice == 2:
                                    #Using try, except, else to handle error
                                    try:
                                    #It will pop file explorer window to let user choose the output binary file  
                                        out_file = FlexiCryptSystem().openFile("Select .bin file")
                                    #Print Error
                                    except Exception as e:
                                        print_error(f"Error: {e}")
                                    #Do next step if code in try block is not error
                                    else:
                                        #Write the ciphertext into binary file
                                        rsa_obj.output_file = out_file
                                        rsa_obj.write_file(message = cipher, binary = True)
                                        #Print to let user know that ciphertext write to file is success
                                        print_success(f"Encrypted binary saved to {out_file} success.")
                                #If user choose exit print exit message then break       
                                elif output_choice == 3:
                                    print_exit()
                                    break
                                #If user choose invalid choice
                                else:
                                    print_info("Invalid choice.")
                                    continue
                    #Always run this code
                    finally:
                        #Print to let user know that encrypted proccess is completed
                        print_info("Encrypted process completed.")
                    break
            #If user choose decrypt
            elif operation == 3:
                #Use while loop to make loop always run for user
                while True:
                    #Using try, except, else and finally to handle error
                    try:
                        #Print the input key menu
                        print_key_input_options()
                        #Let user choose input key menu options
                        key_choice = secure_input("Choose an option: ", [1, 2, 3])
                    #Print Error
                    except Exception as e:
                        print_error(f"Error {e}")
                    #Do next step if code in try block is not error
                    else:
                        #If user choose input key by paste in terminal
                        if key_choice == 1:
                            #Using try, except, else to handle error
                            try:
                                #Let user input key in terminal
                                lines = print_private_key_input()
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Do next step if code in try block is not error
                            else:
                                #Save private key to a variable
                                priv_key = PrivateKey.load_pkcs1("\n".join(lines).encode())
                                #Let user know that input key is success
                                print_success("Key input success.")
                        #If user choose to load private key from file
                        elif key_choice == 2:
                            #Using try, except, else to handle error
                            try:
                                #It will pop file explorer window to let user choose the private key file
                                key_file = FlexiCryptSystem().openFile("Select Private Key file")
                                #Open file to read the private key
                                with open(key_file, "r") as f:
                                    priv_key = PrivateKey.load_pkcs1(f.read().encode())
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Let user know that key input is success
                            else:
                                print_success("Key input success.")
                        #If user choose exit print exit message then break
                        elif key_choice == 3:
                            print_exit()
                            break
                        #If user choose invalid choice
                        else:
                            print_error("Invalid choice.")
                            continue
                    #Always run this code
                    finally:
                        #Print to let user know that key input process is completed
                        print_info("Key input completed.")
                    #Using try, except, else to handle error
                    try:
                        #Create an object from RSA class with private key attribute
                        rsa_obj = RSA(private_key = priv_key)
                    #Print Error
                    except Exception as e:
                        print_error(f"Error: {e}")
                    #Do next step if code in try block is not error
                    else:
                        #Using try, except, else to handle error
                        try:
                            #Print ciphertext input menu options
                            print_input_options()
                            #Let user choose ciphertext input menu options
                            input_type = secure_input("Choose an option: ", [1, 2, 3])
                        #Print Error
                        except Exception as e:
                            print_error(f"Error: {e}")
                        #Do next step if code in try block is not error
                        else:
                            #If user choose input ciphertext in terminal
                            if input_type == 1:
                                #Using try, except, else to handle error
                                try:
                                    #Decrypt process using private key and ciphertext
                                    cipher_input = print_input_normal("Enter ciphertext bytes (Python format): ")
                                    print(Style.RESET_ALL, end = "")
                                    #Convert string to bytes
                                    ciphertext = literal_eval(cipher_input)
                                #Print Error
                                except Exception as e:
                                    print_error(f"Error: {e}")
                                #Do next step if code in try block is not error
                                else:
                                    #Decrypt process using private key and ciphertext
                                    plain = rsa_obj.reverse(ciphertext)
                                    #Print to let user know that decrypt from ciphertext is success 
                                    print_success("Decrypted from ciphertext success.")
                            #If user choose to load ciphertext from binary file      
                            elif input_type == 2:
                                #Using try, except, else to handle error
                                try:
                                    #It will pop file explorer window to let user choose the ciphertext file(.bin)
                                    in_file = FlexiCryptSystem().openFile("Select .bin file")
                                #Print Error
                                except Exception as e:
                                    print_error(f"Error: {e}")
                                #Do next step if code in try block is not error
                                else:
                                    #Read ciphertext from input file
                                    rsa_obj.input_file = in_file
                                    data = rsa_obj.read_file(binary = True)
                                    #Decrypt ciphertext from file
                                    plain = rsa_obj.reverse(data)
                                    #Print to let user know that decrypt ciphertext from file is success
                                    print_success("Decrypted from file success.")
                            #If user choose exit print exit message then break
                            elif input_type == 3:
                                    print_exit()
                                    break
                            #If user choose invalid choice
                            else:
                                print_error("Invalid choice.")
                                continue
                            #Using try, except, else to handle error
                            try:
                                #Print output decrypt menu
                                print_output_decrypt_options()
                                #Let user choose output decrypt menu options
                                output_choice = secure_input("Choose an option: ", [1, 2, 3])
                            #Print Error
                            except Exception as e:
                                print_error(f"Error: {e}")
                            #Do next step if code in try block is not error
                            else:
                                #If user choose to display plaintext in terminal
                                if output_choice == 1:
                                    #Display the plaintext in terminal
                                    print(Fore.YELLOW + f"Decrypted text: ", end = "")
                                    print(Fore.CYAN + f"{plain}")
                                    print(Style.RESET_ALL, end = "")
                                    #Print to let user know that display plaintext is success
                                    print_success(f"Decrypted text display success.")
                                #If user choose to save plaintext as text file
                                elif output_choice == 2:
                                    #Using try, except, else to handle error
                                    try:
                                        #It will pop file explorer window to let user choose the output plaintext file(.txt)
                                        out_file = FlexiCryptSystem().openFile("Select .txt file")
                                    #Print Error
                                    except Exception as e:
                                        print_error(f"Error: {e}")
                                    #Do next step if code in try block is not error
                                    else:
                                        #Write the plaintext into text file
                                        rsa_obj.output_file = out_file
                                        rsa_obj.write_file(message = plain, binary = True)
                                        #Let user know that decrypt text has save to the file success
                                        print_success(f"Decrypted text saved to {out_file} success.")
                                #If user choose exit print exit message then break
                                elif output_choice == 3:
                                    print_exit()
                                    break
                                #If user choose invalid choice
                                else:
                                    print_info("Invalid choice.")
                                    continue
                    #Always run this code
                    finally:
                        #Print to let user know that decrypted process is completed
                        print_info("Decrypted process completed.")
                    #Break the loop
                    break
            #If user choose exit print exit message then break        
            elif operation == 4:
                print_exit()
                break
            #If user choose invalid choice
            else:
                print("Invalid choice.")
                continue
        
if __name__ == "__main__":
    rsa_main()