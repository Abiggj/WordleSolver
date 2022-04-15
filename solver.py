import wordle
import random


def get_words():
    # gets the word stored in file to actual word list
    filepath = "words.txt"
    with open(filepath, 'r') as file:
        return [word.strip() for word in file.readlines()]


class Solver:
    def __init__(self):
        # gets list of all possible 5 letter words for instance
        self.words = get_words()

    def solve(self, score, guess="arise"):
        # start with the word arise
        skip = ""  # if more than 2 same letters, then skip one
        for ind in range(0, 5):
            if guess.count(guess[ind]) > 1:
                continue
            # if letter present at the same position,
            #   then remove all the other without the same
            if score[ind] == 2:
                for word in self.words[:]:
                    if guess[ind] != word[ind]:
                        self.words.remove(word)
            # if the letter is present but a different position,
            #     remove all with the letter at the position,
            #       except if another of the same letter is in word
            elif score[ind] == 1:
                for word in self.words[:]:
                    if word[ind] == guess[ind]:
                        self.words.remove(word)
                    elif guess[ind] not in word:
                        self.words.remove(word)
            # if the letter is not present,
            #     then remove all the words with the word
            elif score[ind] == 0 and skip != guess[ind]:
                for word in self.words[:]:
                    if guess[ind] in word:
                        self.words.remove(word)
        return str(random.choice(self.words))  # send back a random word from the list of narrowed down words


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
