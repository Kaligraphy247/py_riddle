import time, sys,os

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

typingPrint("#######################################\n")
typingPrint("#######################################\n")
typingPrint("###                                 ###\n")
typingPrint("###      Welcome to Py_Riddle!      ###\n")
typingPrint("###                                 ###\n")
typingPrint("#######################################\n")
typingPrint("#######################################\n")

time.sleep(2)
clearScreen()