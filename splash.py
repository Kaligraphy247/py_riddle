import time, sys,os

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01) # 0.5 for half a second... extra decimal places to make typePrint faster e.g 0.005

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
typingPrint("###      Welcome to Py_Riddle!      ###\n")
typingPrint("###                                 ###\n")
typingPrint("#######################################\n")
typingPrint("#######################################\n")

time.sleep(1)
clearScreen()