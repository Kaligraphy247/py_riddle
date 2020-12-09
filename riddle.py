# Simple and interactive riddles written with python
# back links here

import splash, time, sys,os

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) # 0.5 for half a second... extra decimal places to make typePrint faster e.g 0.005

def clearScreen():
    os.system("cls")

typingPrint("Some Riddles to test your knowledge!\n")
typingPrint("Some Riddles will have one word answers\n")
typingPrint("Let's start with something simple.\n")

typingPrint("1. What has to be broken before you can use it?\n")
answer01 = str(input().lower())
if answer01 == "egg":
    typingPrint("Correct")
if answer01 == "an egg":
    typingPrint("Correct\n")
else: 
    typingPrint("Wrong, correct answer is 'an egg'\n ")
    typingPrint("next\n")

typingPrint("2. I’m tall when I’m young, and I’m short when I’m old. What am I?\n")
answer02 = str(input().lower())
if answer02 == "candle":
    typingPrint("Correct\n")

typingPrint("3. What is full of holes but still holds water?\n")
answer03 = str(input().lower())

typingPrint("4. What is always in front of you but can’t be seen?\n")
answer04 = str(input().lower())

typingPrint("5. What goes up but never comes down?\n")
answer05 =  str(input().lower())

