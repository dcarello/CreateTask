import random


class Hangman:
    def random_word(self):
        words = []
        # opens the file with all the words and puts it in an array
        f = open("wordList.txt", "r")
        for line in f:
            words.append(line[:-1])
        f.close
        # returns a random word from the array
        return random.choice(words)

    def hide_word(self, key_word):
        hidden_word = ""
        # for each letter in the key word it puts an underscore and a space for readability
        for letter in key_word:
            hidden_word = hidden_word + '*'
        return hidden_word

    # Gets a letter from the user and makes sure it is a valid letter.
    def user_guess(self, used_letters):
        valid_input = False
        while not valid_input:
            letter_guess = input("What letter do you think is in the word: ")
            if letter_guess.isalpha() and letter_guess not in used_letters and len(letter_guess) == 1:
                valid_input = True
        return letter_guess.lower()

    # checks if the letter inputed by the user is in the hidden word if not removes a chance
    def check_guess(self, letter_guess, key_word):
        wrong_guess = True
        for letter in range(len(key_word)):
            if key_word[letter] == letter_guess:
                self.hidden_word = self.hidden_word[:letter] + \
                    letter_guess + self.hidden_word[letter + 1:]
                wrong_guess = False
        if wrong_guess == True:
            self.chances = self.chances - 1
        return

    def check_win(self):
        if '*' not in self.hidden_word:
            return True

    def main(self):
        # initializes variables
        self.chances = 6
        used_letters = []
        key_word = self.random_word()
        self.hidden_word = self.hide_word(key_word)
        win = False
        # Runs through the game while the user hasn't won or chances doesn't equal 0
        while self.chances != 0 and win != True:
            print(self.hidden_word)
            print(f"Number of Chances: {self.chances}")
            letter_guess = self.user_guess(used_letters)
            used_letters.append(letter_guess)
            print(used_letters)
            self.check_guess(letter_guess, key_word)
            win = self.check_win()
        if self.chances == 0:
            print(f"The word was {key_word}.")
            print("Nice try please play again.")
            return 0
        elif win == True:
            print("Congrats you won!!!")
            return 0


if __name__ == "__main__":
    engine = Hangman()
    engine.main()
