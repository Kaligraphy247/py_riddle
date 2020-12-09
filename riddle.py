# Simple and interactive riddles written with python
# back links here
""" 
riddles from https://parade.com/947956/parade/riddles/ 

"""

import splash, time, sys,os

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) # 0.5 for half a second... extra decimal places to make typePrint faster e.g 0.005

def clearScreen():
    os.system("cls")

typingPrint("Some Riddles to test your knowledge!\n")
time.sleep(2)
typingPrint("Some Riddles may have one word answers.\n")
time.sleep(1)
typingPrint("Let's start with something simple.\n")
time.sleep(1)

"""
typingPrint("1. What has to be broken before you can use it?\n")
answer01 = str(input().lower())
if answer01 == "egg":
    typingPrint("Correct!\n")
elif answer01 == "an egg":
    typingPrint("Correct!\n")
elif answer01 =="eggs":
     typingPrint("Correct!\n")
else: 
    typingPrint("Wrong, correct answer is 'an Egg/Eggs'\n Next...\n")
    typingPrint("next\n")


typingPrint("2. I’m tall when I’m young, and I’m short when I’m old. What am I?\n")
answer02 = str(input().lower())
if answer02 == "candle":
    typingPrint("Correct!\n")
elif answer02 == "a candle":
    typingPrint("Correct!\n")
elif answer02 == "candles":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'candle'\n Next...\n")


typingPrint("3. What is full of holes but still holds water?\n")
answer03 = str(input().lower())
if answer03 == "sponge":
    typingPrint("Correct!\n")
elif answer03 == "a sponge":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, correct answer is 'a sponge' \n Next...\n")


typingPrint("4. What is always in front of you but can’t be seen?\n")
answer04 = str(input().lower())
if answer04 == "future":
    typingPrint("Correct!\n")
elif answer04 == "the future":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is ' the future' \n Next...\n")

"""
typingPrint("5. What goes up but never comes down?\n")
answer05 =  str(input().lower())
if answer05 == "age":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Age' \n Next...\n")

typingPrint("Now, to hard Riddles.....")
time.sleep(2)
clearScreen()


typingPrint("1. What is so fragile that saying its name breaks it?\n")
answer11 = str(input().lower())
if answer11 == "silence":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Silence' \n Next...\n")

"""
typingPrint("2. What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?\n")
answer12 = str(input().lower())
if answer12 == "river":
     typingPrint("Correct!\n")
elif answer12 == "a river":
     typingPrint("Correct!\n")
elif answer12 =="rivers":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'River/Rivers' \n Next...\n")


typingPrint("3. What can fill a room but takes up no space?\n")
answer13 = str(input().lower())
if answer13 == "light":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Light' \n Next...\n")


typingPrint("4. If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?\n")
answer14 = str(input().lower())
if answer14 == "mirror":
     typingPrint("Correct!\n")
elif answer14 == "a mirror":
     typingPrint("Correct!\n")
elif answer14 == "mirrors":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Mirror/Mirrors' \n Next...\n")


typingPrint("5. The more you take, the more you leave behind. What are they?\n")
answer15 = str(input().lower())
if answer15 =="footsteps":
     typingPrint("Correct!\n")
elif answer15 =="footstep":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Footstep/Footsteps' \n Next...\n")


typingPrint("6. I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?\n")
answer16 = str(input().lower())
if answer16 =="key":
     typingPrint("Correct!\n")
elif answer16 == "a key":
     typingPrint("Correct!\n")
elif answer16 =="keys":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Key/Keys' \n Next...\n")


typingPrint("7.  People make me, save me, change me, raise me. What am I?\n")
answer17 = str(input().lower())
if answer17 =="money":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Money' \n Next...\n")


typingPrint("8. I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?\n")
answer18 = str(input().lower())
if answer18 == "fire":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Fire' \n Next...\n")


typingPrint("9. What goes through cities and fields, but never moves?\n")
answer19 = str(input().lower())
if answer19 == "road":
     typingPrint("Correct!\n")
elif answer19 == "roads":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Road/Roads' \n Next...\n")

"""
typingPrint("10. With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?\n")
answer110 = str(input().lower())
if answer110 == "stapler":
     typingPrint("Correct!\n")
elif answer110 == "a stapler":
     typingPrint("Correct!\n")
elif answer110 == "staplers":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Stapler/Staplers' \n Next...\n")


clearScreen()


typingPrint("Some Bonus Riddle, you may terminate now if you wish to stop")
time.sleep(2)
typingPrint("You may terminate now if you wish to stop")
clearScreen()


typingPrint("a.  I have lakes with no water, mountains with no stone and cities with no buildings. What am I?\n")
answer_a = str(input().lower())
if answer_a == "map":
     typingPrint("Correct!\n")
elif answer_a == "a map":
     typingPrint("Correct!\n")
elif answer_a == "maps":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Maps' \n Next...\n")


typingPrint("b. What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?\n")
answer_b = str(input().lower())
if answer_b == "nothing":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Nothing' \n Next...\n")
import bye

