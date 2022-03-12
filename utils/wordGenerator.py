import requests
import random
import time

# https://github.com/rsalmei/alive-progress
from alive_progress import alive_bar as bar


class Word():
    def __init__(self):
        pass

    def randomWord(self):
        while True:  # Try to get a word that has more than three characters.
            with bar(theme='classic', elapsed=True, monitor=True, stats=True):
                # Public API that gets a random word in Portuguese.
                url = 'https://api.dicionario-aberto.net/random'
                self.word = requests.get(url=url).json()['word'].title()

                if len(self.word) > 3:
                    time.sleep(2)
                    return self.word

                bar()  # Increases the bar loading.

    def blurWord(self):
        blurKey = '_'  # The character that will replace the letter.
        numbers = [random.randint(1, len(self.word)),
                   random.randint(1, len(self.word))]

        for count, character in enumerate(self.word, start=1):
            if count == numbers[0]:
                self.word = self.word.replace(character, blurKey, 1)
            elif count == numbers[1]:
                self.word = self.word.replace(character, blurKey, 1)

        return self.word
