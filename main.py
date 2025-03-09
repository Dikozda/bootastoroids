from constants import *
import pygame


def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000)
        pygame.display.flip()

if __name__ == "__main__":
    main()