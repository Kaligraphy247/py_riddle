# Simple and interactive riddles written with python
# back links here
""" 
riddles from https://parade.com/947956/parade/riddles/ 

"""


# import splash, time, sys, os, colorama
import time, sys, os
from modules.timey import Timey as tp
from modules import starter_riddle, hard_riddles, bonus_riddles
from yachalk import chalk
import splash, bye
#time for secs param
sec = 0.005

#FUNCTIONS HERE
def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

def bold_and_underline(text):
    return chalk.white.bold.underline(text)

splash.splash()
tp(bold_and_underline("Some Riddles to test your knowledge!"), sec)
time.sleep(1.5)
tp(bold_and_underline("Some Riddles may have one word answers."), sec)
time.sleep(1.5)
tp(bold_and_underline("Let's start with something simple."), sec)
time.sleep(1.5)
clearScreen()

starter_riddle.riddle()
time.sleep(5)
clearScreen()

tp(f"Now to some {chalk.red.bold('Hard Riddles')} ... ", sec)
time.sleep(2)
clearScreen()

hard_riddles.riddle()
time.sleep(3)
clearScreen()
tp(f"{chalk.bg_gray.white('Some Bonus Riddles')}🎃😀😁\n ", sec)
tp(f"{chalk.yellow('Do you want to play bonus round? (y/n)')}", sec)

query =  str(input("")).lower().strip()

if query == 'y':
    bonus_riddles.riddle()
elif query == 'n':
    bye.bye()
else:
    tp(f"{chalk.white_bright('Didnt get that, Try again some other time ?')}", sec)
    time.sleep(1)
    tp("Goodbye", sec)
    time.sleep(2.5)
    clearScreen()
    bye.bye()

