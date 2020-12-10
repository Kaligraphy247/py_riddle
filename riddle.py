# Simple and interactive riddles written with python
# back links here
""" 
riddles from https://parade.com/947956/parade/riddles/ 

"""

#FUNCTIONS HERE
import splash, time, sys,os

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) # 0.5 for half a second... extra decimal places to make typePrint faster e.g 0.005

def clearScreen():
    os.system("cls")


# PROGRAM STARTS HERE...
typingPrint("Some Riddles to test your knowledge!\n")
time.sleep(2)
typingPrint("Some Riddles may have one word answers.\n")
time.sleep(1)
typingPrint("Let's start with something simple.\n")
time.sleep(1)


typingPrint("1. What has to be broken before you can use it?\n")
answer01 = str(input().lower())
if answer01 == "egg":
    typingPrint("Correct!\n")
elif answer01 == "an egg":
    typingPrint("Correct!\n")
elif answer01 == "eggs":
     typingPrint("Correct!\n")
else: 
    typingPrint("Wrong, correct answer is 'an Egg/Eggs'\nNext...\n")


typingPrint("2. I’m tall when I’m young, and I’m short when I’m old. What am I?\n")
answer02 = str(input().lower())
if answer02 == "candle":
    typingPrint("Correct!\n")
elif answer02 == "a candle":
    typingPrint("Correct!\n")
elif answer02 == "candles":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'candle'\nNext...\n")


typingPrint("3. What is full of holes but still holds water?\n")
answer03 = str(input().lower())
if answer03 == "sponge":
    typingPrint("Correct!\n")
elif answer03 == "a sponge":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, correct answer is 'a sponge' \nNext...\n")


typingPrint("4. What is always in front of you but can’t be seen?\n")
answer04 = str(input().lower())
if answer04 == "future":
    typingPrint("Correct!\n")
elif answer04 == "the future":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is ' the future' \nNext...\n")


typingPrint("5. What goes up but never comes down?\n")
answer05 =  str(input().lower())
if answer05 == "age":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Age'\n")
time.sleep(1.5)

typingPrint("Now, to hard Riddles.....")
time.sleep(2)
clearScreen()


typingPrint("1. What is so fragile that saying its name breaks it?\n")
answer11 = str(input().lower())
if answer11 == "silence":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Silence' \nNext...\n")


typingPrint("2. What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?\n")
answer12 = str(input().lower())
if answer12 == "river":
     typingPrint("Correct!\n")
elif answer12 == "a river":
     typingPrint("Correct!\n")
elif answer12 =="rivers":
    typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'River/Rivers' \nNext...\n")


typingPrint("3. What can fill a room but takes up no space?\n")
answer13 = str(input().lower())
if answer13 == "light":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Light' \nNext...\n")


typingPrint("4. If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?\n")
answer14 = str(input().lower())
if answer14 == "mirror":
     typingPrint("Correct!\n")
elif answer14 == "a mirror":
     typingPrint("Correct!\n")
elif answer14 == "mirrors":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Mirror/Mirrors' \nNext...\n")


typingPrint("5. The more you take, the more you leave behind. What are they?\n")
answer15 = str(input().lower())
if answer15 =="footsteps":
     typingPrint("Correct!\n")
elif answer15 =="footstep":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Footstep/Footsteps' \nNext...\n")


typingPrint("6. I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?\n")
answer16 = str(input().lower())
if answer16 =="key":
     typingPrint("Correct!\n")
elif answer16 == "a key":
     typingPrint("Correct!\n")
elif answer16 =="keys":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Key/Keys' \nNext...\n")


typingPrint("7.  People make me, save me, change me, raise me. What am I?\n")
answer17 = str(input().lower())
if answer17 =="money":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Money' \nNext...\n")


typingPrint("8. I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?\n")
answer18 = str(input().lower())
if answer18 == "fire":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Fire' \nNext...\n")


typingPrint("9. What goes through cities and fields, but never moves?\n")
answer19 = str(input().lower())
if answer19 == "road":
     typingPrint("Correct!\n")
elif answer19 == "roads":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Road/Roads' \nNext...\n")


typingPrint("10. With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?\n")
answer110 = str(input().lower())
if answer110 == "stapler":
     typingPrint("Correct!\n")
elif answer110 == "a stapler":
     typingPrint("Correct!\n")
elif answer110 == "staplers":
     typingPrint("Correct!\n")
else:
    typingPrint("Wrong, the right answer is 'Stapler/Staplers'\n")

time.sleep(2)
clearScreen()


typingPrint("Some Bonus Riddles 🎃😀😁\n")
time.sleep(1)
typingPrint("You may terminate now if you wish to stop.\n")
time.sleep(1)
typingPrint("Do you want to play bonus round? Yes/No\n" + ": ")
bonus_query = str(input().lower())
while bonus_query == "yes":
    import bonus

else:
    clearScreen()

import bye

#PROGRAM ENDS HERE...