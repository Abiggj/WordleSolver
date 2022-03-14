import wordle
import random

class Solver:
    def __init__(self):
        self.words = self.get_words()
        self.guess = 'arise'

    def get_words(self):
        filepath = "words.txt"
        with open(filepath, 'r') as file:
            return [word.strip() for word in file.readlines()]

    def solve(self, score, guess="arise"):
        skip = ""
        for ind in range(0, 5):
            if score[ind] == 2:
                for word in self.words[:]:
                    if guess[ind] != word[ind]:
                        self.words.remove(word)
            elif score[ind] == 1:
                if guess.count(guess[ind]) > 1:
                    skip = guess[ind]
                for word in self.words[:]:
                    if word[ind] == guess[ind]:
                        self.words.remove(word)
                    elif guess[ind] not in word:
                        self.words.remove(word)
            elif score[ind] == 0 and skip != guess[ind]:
                for word in self.words[:]:
                    if guess[ind] in word:
                        self.words.remove(word)
        return str(random.choice(self.words))


if __name__ == "__main__":
    wdl = wordle.Wordle()
    slv = Solver()
    guess = "arise"
    while wdl.chance > 0:
        score = wdl.play(guess)
        print(guess, score)
        guess = slv.solve(score, guess)
    if wdl.chance == -1:
        print("You won")
    else:
        print("NO!!")
    print(wdl.wordle)
