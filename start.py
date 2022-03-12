import os
import time

from utils.wordGenerator import Word
from utils.tipsGenerator import Tips


def askQuestion(correct: str, word: str, tips, count=0, wins=0):
    anwser = input(f'Que palavra é essa? {word} ')

    if anwser.upper() == correct.upper():  # When the user answers correctly.
        wins += 1

        os.system('cls')
        print(f'Você conseguiu! A palavra era {correct}.')
        print(f'Vamos tentar outra palavra? Você conseguiu {wins} vitorias.')

        time.sleep(3)
        startGame(count, wins)

    elif anwser.upper() == 'AGAIN':  # Restart the game with other word.
        print(f'Você desistiu com {count} tentativas e {wins} acertos...')
        print(f'Inclusive, a palavra era certa era {correct}...')

        time.sleep(3)
        return startGame()

    elif anwser.upper() == 'TIPS':
        if tips:
            if len(tips) > 1:
                os.system('cls')
                print('Você tem dicas! Vamos revelar apenas uma por vez.')
                print(tips.pop(0))
                askQuestion(correct, word, tips, count, wins)

            else:
                os.system('cls')
                print('Você tem uma dica! Vamos revelar ela pra você.')
                print(tips.pop(0))
                askQuestion(correct, word, tips, count, wins)

        else:
            os.system('cls')
            print('Você está sem dicas no momento.')
            askQuestion(correct, word, tips, count, wins)

    elif anwser.upper() == 'EXIT':
        print(f'Você estava em uma sequência de {wins} acertos.')
        print(f'A palavra correta era: {correct}... Adeus, amigo!')

        time.sleep(3)
        os.system('cls')
        os.system('exit')

    else:
        # When the user answers wrongly.
        # The game keeps the word and restart the question.
        count += 1  # Adds one more attempt.
        os.system('cls')
        print(f'Errado, tente de novo! (Tentativas: {count})')
        askQuestion(correct, word, tips, count, wins)


def startGame(count=0, wins=0):
    os.system('cls')
    print('Buscando palavras difíceis na internet...')

    word = Word()
    correct = word.randomWord()
    blurred = word.blurWord()
    tips = Tips(correct).tipAbout()

    os.system('cls')
    askQuestion(correct, blurred, tips, count, wins)


if __name__ == '__main__':
    startGame()  # Let's play!
