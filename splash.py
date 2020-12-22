import time, sys,os, colorama
from colorama import Fore
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

# redundant for this module;
def typingInput():
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value
# redundant for this module;

def clearScreen():
    os.system("cls")

typingPrint(Fore.RED + "#######################################\n")
typingPrint(Fore.YELLOW + "#######################################\n")
typingPrint(Fore.LIGHTYELLOW_EX + "###                                 ###\n")
typingPrint(Fore.GREEN + "###      Welcome to Py_Riddle!      ###\n")
typingPrint(Fore.LIGHTBLUE_EX + "###                                 ###\n")
typingPrint(Fore.BLUE + "#######################################\n")
typingPrint(Fore.MAGENTA + "#######################################\n")

print(Fore.RESET)

time.sleep(2)
clearScreen()