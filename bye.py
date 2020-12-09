import time, sys,os

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

typingPrint("#######################################\n")
typingPrint("#######################################\n")
typingPrint("###                                 ###\n")
typingPrint("###               Bye!!             ###\n")
typingPrint("###                                 ###\n")
typingPrint("#######################################\n")
typingPrint("#######################################\n")
time.sleep(2)

clearScreen()