import random
import pygame

from hangman_pygame import draw_window


class Hangman:
    def init(self):
        pygame.init()
        # Try to stick with screen size (1000, 1000)
        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode(
            [self.screen_width, self.screen_height])
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def draw_window(self):
        self.screen.fill(self.white)

        # with multiples
        # Draws the hangman board
        pygame.draw.line(self.screen, self.black, (self.screen_width / 18, self.screen_height / 1.818182),
                         (self.screen_width / 3.6, self.screen_height / 1.818182), 3)
        pygame.draw.line(self.screen, self.black, (self.screen_width / 9, self.screen_height / 1.818182),
                         (self.screen_width / 9, self.screen_height / 10), 3)
        pygame.draw.line(self.screen, self.black, (self.screen_width / 9, self.screen_height / 10),
                         (self.screen_width / 4.5, self.screen_height / 10), 3)
        pygame.draw.line(self.screen, self.black, (self.screen_width / 4.5, self.screen_height / 10),
                         (self.screen_width / 4.5, self.screen_height / 5), 3)
        pygame.draw.line(self.screen, self.black, (self.screen_width / 9, self.screen_height / 6.6666667),
                         (self.screen_width / 7.2, self.screen_height / 10), 3)

        # The hangman person
        # head
        pygame.draw.circle(self.screen, self.black, (self.screen_width / 4.5,
                                                     self.screen_height / 4.1666667), self.screen_height / 25, 3)
        # body
        pygame.draw.line(self.screen, self.black, (self.screen_width / 4.5, self.screen_height / 3.5714285714),
                         (self.screen_width / 4.5, self.screen_height / 2.6315789474), 3)
        # left leg
        pygame.draw.line(self.screen, self.black, (self.screen_width / 4.5, self.screen_height / 2.6315789474),
                         (self.screen_width / 5.1428571429, self.screen_height / 2.22222222), 3)
        # right leg
        pygame.draw.line(self.screen, self.black, (self.screen_width / 4.5, self.screen_height / 2.6315789474),
                         (self.screen_width / 4, self.screen_height / 2.22222222), 3)
        # left arm
        pygame.draw.line(self.screen, self.black, (self.screen_width / 4.5, self.screen_height / 3.2258064516),
                         (self.screen_width / 5.2941176471, self.screen_height / 3.2258064516), 3)
        # right arm
        pygame.draw.line(self.screen, self.black, (self.screen_width / 4.5, self.screen_height / 3.2258064516),
                         (self.screen_width / 3.9130434783, self.screen_height / 3.2258064516), 3)

        # Hidden word on the screen
        font = pygame.font.SysFont('comicsans', 90)
        Hidden_Word = font.render(self.hidden_word, 1, self.black)
        self.screen.blit(Hidden_Word, (self.screen_width /
                         2.3529411765, self.screen_height / 2))

        font = pygame.font.SysFont('comicsans', 90)
        Chances = font.render(self.chances, 1, self.black)
        self.screen.blit(Chances, (550, 250))

        pygame.display.update()

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
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.hidden_word, 1, self.black)
        self.screen.blit(text, (0, 0))
        pygame.display.update()
        return

    def check_win(self):
        if '*' not in self.hidden_word:
            return True

    def main(self):
        self.init()
        # initializes variables
        self.chances = 6
        used_letters = []
        key_word = self.random_word()
        self.hidden_word = self.hide_word(key_word)
        # Starts running the pygame window
        win = False
        # Runs through the game while the user hasn't won or chances doesn't equal 0
        while self.chances != 0 and win != True:
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                self.draw_window()
                # self.display_word()
            pygame.quit()
            print(self.hidden_word)
            print(f"Number of Chances: {self.chances}")
            # print(key_word)
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
