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


    sad_emoji = ['😢', '😔', '😓', '😥', '😢', '💔']
    happy_emoji = ['😀', '😁', '😊', '😂', '🥳', '🍾']

    questions = [
        "a. I have lakes with no water, mountains with no stone and cities with no buildings. What am I",
        "b. What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?"
    ]

    answers = {
        questions[0]: ["map", "a map", "maps"],
        questions[1]: ["nothing"],
    }


    for key, value in answers.items():
        tp(question(key), sec)
        quest = str(input(":: ").lower().strip())
        if quest in value:
            tp(f"Your answer '{right_ans(quest)}' is correct {happy()}", sec)
            tp(f"{correct('You are right!!!')}\nNext...\n", sec)

        else:
            tp(f"Your answer '{wrong_ans(quest)}' is wrong {sad()} The right answer should be...", sec)
            #tp("")
            time.sleep(1.0)
            list_answer(list=value)
            time.sleep(1.5)
            tp("\nNext...\n", sec)
    tp("Oops, that's all for now 😁", sec)

