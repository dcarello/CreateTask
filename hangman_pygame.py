import pygame
from pygame.locals import *

screen_width = 1080
screen_height = 1080
screen = pygame.display.set_mode([screen_width, screen_height])
white = (255, 255, 255)
black = (0, 0, 0)


def draw_window():
    screen.fill(white)

    # # Draws the hangman board
    # pygame.draw.line(screen, black, (50, 275), (250, 275), 3)
    # pygame.draw.line(screen, black, (100, 275), (100, 50), 3)
    # pygame.draw.line(screen, black, (100, 50), (200, 50), 3)
    # pygame.draw.line(screen, black, (200, 50), (200, 100), 3)
    # pygame.draw.line(screen, black, (100, 75), (125, 50), 3)

    # # The hangman person
    # # head
    # pygame.draw.circle(screen, black, (200, 120), 20, 3)
    # # body
    # pygame.draw.line(screen, black, (200, 140), (200, 190), 3)
    # # left leg
    # pygame.draw.line(screen, black, (200, 190), (175, 225), 3)
    # # right leg
    # pygame.draw.line(screen, black, (200, 190), (225, 225), 3)
    # # left arm
    # pygame.draw.line(screen, black, (200, 155), (170, 155), 3)
    # # right arm
    # pygame.draw.line(screen, black, (200, 155), (230, 155), 3)

    # with multiples
    # Draws the hangman board
    pygame.draw.line(screen, black, (screen_width / 18, screen_height / 1.818182),
                     (screen_width / 3.6, screen_height / 1.818182), 3)
    pygame.draw.line(screen, black, (screen_width / 9, screen_height / 1.818182),
                     (screen_width / 9, screen_height / 10), 3)
    pygame.draw.line(screen, black, (screen_width / 9, screen_height / 10),
                     (screen_width / 4.5, screen_height / 10), 3)
    pygame.draw.line(screen, black, (screen_width / 4.5, screen_height / 10),
                     (screen_width / 4.5, screen_height / 5), 3)
    pygame.draw.line(screen, black, (screen_width / 9, screen_height / 6.6666667),
                     (screen_width / 7.2, screen_height / 10), 3)

    # The hangman person
    # head
    pygame.draw.circle(screen, black, (screen_width / 4.5,
                       screen_height / 4.1666667), screen_height / 25, 3)
    # body
    pygame.draw.line(screen, black, (screen_width / 4.5, screen_height / 3.5714285714),
                     (screen_width / 4.5, screen_height / 2.6315789474), 3)
    # left leg
    pygame.draw.line(screen, black, (screen_width / 4.5, screen_height / 2.6315789474),
                     (screen_width / 5.1428571429, screen_height / 2.22222222), 3)
    # right leg
    pygame.draw.line(screen, black, (screen_width / 4.5, screen_height / 2.6315789474),
                     (screen_width / 4, screen_height / 2.22222222), 3)
    # left arm
    pygame.draw.line(screen, black, (screen_width / 4.5, screen_height / 3.2258064516),
                     (screen_width / 5.2941176471, screen_height / 3.2258064516), 3)
    # right arm
    pygame.draw.line(screen, black, (screen_width / 4.5, screen_height / 3.2258064516),
                     (screen_width / 3.9130434783, screen_height / 3.2258064516), 3)

    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
