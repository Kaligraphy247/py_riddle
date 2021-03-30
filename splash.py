import time, sys,os, colorama
from colorama import Fore

def typingPrint(text):
    """ Displays text incessantly using the time.sleep() method """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

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