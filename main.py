from RSA import *
from ZWS import*
from color import *
import sys
import os

#Use to clear terminal
def clear_screen():
        if os.name == "nt":
            os.system("cls")
        else: 
            os.system("clear")
#Main of the system
def main():
    #While loop to always run interface for user
    while True:
        clear_screen()
        #Print banner of system and the menu
        print_banner()
        print_main_menu()
        #Let user choose the option
        method = secure_input("Choose an option: ", [1, 2, 3])
        #If user choose RSA run rsa_main()
        if method == 1:
            rsa_main()
        #If user choose ZWS create an object of ZWS then call zws_main() method
        elif method == 2:
                zws1 = ZWS()
                zws1.zws_main()
        #If user choose to exit the system
        elif method == 3:
            print_exit()
            sys.exit(0)

if __name__ == "__main__":
    main()
    