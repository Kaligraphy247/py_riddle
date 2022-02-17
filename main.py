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
    print("goodbye")
    exit()
else:
    tp(f"{chalk.white_bright('Didnt get that, Try again some other time ?')}", sec)
    time.sleep(1)
    tp("Goodbye", sec)
    time.sleep(2.5)
    clearScreen()
    quit()


# typingPrint(Fore.YELLOW + "3. What is full of holes but still holds water?\n")
# answer03 = str(input().lower())
# if answer03 == "sponge":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
# elif answer03 == "a sponge":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
#     print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, correct answer is 'a sponge' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "4. What is always in front of you but can’t be seen?\n")
# answer04 = str(input().lower())
# if answer04 == "future":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
# elif answer04 == "the future":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is ' the future' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "5. What goes up but never comes down?\n")
# answer05 =  str(input().lower())
# if answer05 == "age":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Age'\n")
#     print(Style.RESET_ALL, Fore.RESET)
# time.sleep(1.5)


# typingPrint(Style.DIM + Fore.RED + "Now, to hard Riddles.....")
# print(Style.RESET_ALL)
# time.sleep(2)
# clearScreen()


# # Hard Riddles
# typingPrint(Fore.YELLOW + "1. What is so fragile that saying its name breaks it?\n")
# answer11 = str(input().lower())
# if answer11 == "silence":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Silence' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "2. What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?\n")
# answer12 = str(input().lower())
# if answer12 == "river":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer12 == "a river":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer12 =="rivers":
#     typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#     print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'River/Rivers' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "3. What can fill a room but takes up no space?\n")
# answer13 = str(input().lower())
# if answer13 == "light":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Light' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "4. If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?\n")
# answer14 = str(input().lower())
# if answer14 == "mirror":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer14 == "a mirror":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer14 == "mirrors":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Mirror/Mirrors' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "5. The more you take, the more you leave behind. What are they?\n")
# answer15 = str(input().lower())
# if answer15 =="footsteps":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer15 =="footstep":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Footstep/Footsteps' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "6. I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?\n")
# answer16 = str(input().lower())
# if answer16 =="key":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer16 == "a key":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer16 =="keys":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Key/Keys' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "7.  People make me, save me, change me, raise me. What am I?\n")
# answer17 = str(input().lower())
# if answer17 =="money":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Money' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "8. I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?\n")
# answer18 = str(input().lower())
# if answer18 == "fire":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Fire' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "9. What goes through cities and fields, but never moves?\n")
# answer19 = str(input().lower())
# if answer19 == "road":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer19 == "roads":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Road/Roads' \nNext...\n")
#     print(Style.RESET_ALL, Fore.RESET)


# typingPrint(Fore.YELLOW + "10. With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?\n")
# answer110 = str(input().lower())
# if answer110 == "stapler":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer110 == "a stapler":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# elif answer110 == "staplers":
#      typingPrint(Fore.GREEN + Style.BRIGHT + "Correct!\n")
#      print(Style.RESET_ALL, Fore.RESET)
# else:
#     typingPrint(Style.BRIGHT + Fore.RED + "Wrong, the right answer is 'Stapler/Staplers'\n")
#     print(Style.RESET_ALL, Fore.RESET)

# time.sleep(2)
# clearScreen()


# # BONUS CONTENT
# typingPrint(Fore.MAGENTA + "Some Bonus Riddles 🎃😀😁\n")
# time.sleep(1)
# typingPrint("You may terminate now if you wish to stop.\n")
# time.sleep(1)
# typingPrint("Do you want to play bonus round? Yes/No: ")
# bonus_query = str(input().lower())
# print(Fore.RESET)
# while bonus_query == "yes":
#     import bonus

# else:
#     clearScreen()

# import bye
# #PROGRAM ENDS