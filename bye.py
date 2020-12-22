import time, sys,os, colorama
from colorama import Fore

def typingPrint(text):
    """ Displays text incessantly using the time.sleep() method """
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

typingPrint(Fore.MAGENTA + "#######################################\n") # THIS IS SUPPOSED TO REFLECT PURPLE 😅
typingPrint(Fore.BLUE + "#######################################\n") # THIS IS SUPPOSED TO REFLECT INDIGO 😅
typingPrint(Fore.LIGHTBLUE_EX + "###                                 ###\n")
typingPrint(Fore.GREEN + "###              Bye!!!             ###\n")
typingPrint(Fore.LIGHTYELLOW_EX + "###                                 ###\n")
typingPrint(Fore.YELLOW + "#######################################\n") # THIS IS SUPPOSED TO REFLECT ORANGE 😅
typingPrint(Fore.RED + "#######################################\n") 
print(Fore.RESET) # so your terminal doesn't retain the last color printed...🤔
time.sleep(2)

clearScreen()
