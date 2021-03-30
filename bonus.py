import time, sys, os, colorama
from colorama import Fore, Back, Style
print(Style.RESET_ALL, Fore.RESET)

def typingPrint(text):
    """ Displays text incessantly using the time.sleep() method """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")


typingPrint(Fore.BLACK + Back.WHITE + "Bonus Round")
print(Fore.RESET, Back.RESET)
typingPrint(Fore.BLUE + "a.  I have lakes with no water, mountains with no stone and cities with no buildings. What am I?\n")
answer_a = str(input().lower())
if answer_a == "map":
     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
     print(Style.RESET_ALL, Fore.RESET)
elif answer_a == "a map":
     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
     print(Style.RESET_ALL, Fore.RESET)
elif answer_a == "maps":
    typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
    print(Style.RESET_ALL, Fore.RESET)
else:
    typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Maps' \nNext...\n")
    print(Style.RESET_ALL, Fore.RESET)


typingPrint(Fore.BLUE + "b. What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?\n")
answer_b = str(input().lower())
if answer_b == "nothing":
     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
     print(Style.RESET_ALL, Fore.RESET)
else:
    typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Nothing'\n")
    print(Style.RESET_ALL, Fore.RESET)

time.sleep(1.5)
clearScreen()
import bye
sys.exit()
