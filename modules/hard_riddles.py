from yachalk import chalk
from modules.timey import Timey as tp
import time, random

def riddle():
    '''Riddle Function'''
    # sleep settings
    sec = 0.005

    def sad():
        for x in random.choice(sad_emoji):
            return x

    def happy():
        for x in random.choice(happy_emoji):
            return x

    def right_ans(text):
        return chalk.blue.bold.italic(text)

    def wrong_ans(text):
        return chalk.red.bold(text)

    def correct(text):
        return chalk.green.bold(text)

    def question(text):
        return chalk.yellow.bold(text)

    def list_answer(list) -> list:
        return [print(f"'{chalk.green.bold(x)}'", end=' ') for x in list]

    correct_counter = 0
    wrong_counter   = 0

    sad_emoji = ['😢', '😔', '😓', '😥', '😢', '💔']
    happy_emoji = ['😀', '😁', '😊', '😂', '🥳', '🍾']

    questions = [
        "1. What is so fragile that saying its name breaks it?",
        "2. What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?",
        "3. What can fill a room but takes up no space?",
        "4. If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?",
        "5. The more you take, the more you leave behind. What are they?",
        "6. I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?",
        "7. People make me, save me, change me, raise me. What am I?",
        "8. I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?",
        "9. What goes through cities and fields, but never moves?",
        "10. With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?"
    ]

    answers = {
        questions[0]: ["silence"],
        questions[1]: ["river", "a river", "rivers"],
        questions[2]: ["light"],
        questions[3]: ["mirror", "a mirror", "mirrors"],
        questions[4]: ["footsteps", "footstep", "steps"],
        questions[5]: ["key", "a key", "keys"],
        questions[6]: ["money"],
        questions[7]: ["fire"],
        questions[8]: ["road", "roads"],
        questions[9]: ["a stapler", "stapler", "staplers"]
    }


    for key, value in answers.items():
        tp(question(key), sec)
        quest = str(input(":: ").lower().strip())
        if quest in value:
            tp(f"Your answer '{right_ans(quest)}' is correct {happy()}", sec)
            tp(f"{correct('You are right!!!')}\nNext...\n", sec)
            correct_counter += 1


        else:
            tp(f"Your answer '{wrong_ans(quest)}' is wrong {sad()} The right answer should be...", sec)
            wrong_counter += 1
            time.sleep(1.0)
            list_answer(list=value)
            time.sleep(1.5)
            tp("\nNext...\n", sec)
    tp(f"Your total score in this round is {correct_counter} out of {len(questions)}", sec)
