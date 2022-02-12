from yachalk import chalk
from timey import Timey as tp
import time, random

def riddle():
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
        "1. What has to be broken before you can use it?",
        "2. I’m tall when I’m young, and I’m short when I’m old. What am I?",
        "3. What is full of holes but still holds water?",
        "4. What is always in front of you but can’t be seen",
        "5. What goes up but never comes down?"
    ]

    answers = {
        questions[0]: ["egg", "an egg", "eggs"],
        questions[1]: ["candle", "a candle", "candles"],
        questions[2]: ["sponge", "a sponge"],
        questions[3]: ["future", "the future"],
        questions[4]: ["age"]
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

