import random

class Wordle:

    def __init__(self, wordle=None):
        self.words = None
        self.chance = 4
        self.get_words()
        self.wordle = random.choice(self.words) if not wordle else wordle
        self.guess = ""
        self.score = list()

    def get_words(self):
        filepath = "words.txt"
        with open(filepath, 'r') as file:
            self.words = [word.strip() for word in file.readlines()]

    def play(self, guess):
        if self.chance > 0:
            self.score.clear()
            self.guess = guess
            try:
                self.words.index(self.guess)
            except ValueError:
                return False

            else:
                for ind in range(0, 5):
                    if self.wordle[ind] == self.guess[ind]:
                        self.score.append(2)
                    elif self.guess[ind] in self.wordle:
                        self.score.append(1)
                    else:
                        self.score.append(0)
                if self.score == [2, 2, 2, 2, 2]:
                    self.chance = -1
                else:
                    self.chance -= 1
                return self.score


if __name__ == "__main__":
    wdl = Wordle("sword")
    print(wdl.wordle)
