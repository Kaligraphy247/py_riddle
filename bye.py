import time, sys,os, colorama
from colorama import Fore, Back, Style

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def typingInput():
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value

def clearScreen():
    os.system("cls")

typingPrint(Fore.RED + "#######################################\n")
typingPrint(Fore.YELLOW + "#######################################\n") # THIS IS SUPPOSED TO REFLECT ORANGE 😅
typingPrint(Fore.LIGHTYELLOW_EX + "###                                 ###\n")
typingPrint(Fore.GREEN + "###              Bye!!!             ###\n")
typingPrint(Fore.LIGHTBLUE_EX + "###                                 ###\n")
typingPrint(Fore.BLUE + "#######################################\n") # THIS IS SUPPOSED TO REFLECT INDIGO 😅
typingPrint(Fore.MAGENTA + "#######################################\n") # THIS IS SUPPOSED TO REFLECT PURPLE 😅
time.sleep(2)

clearScreen()
