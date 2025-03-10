from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame


def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroid_field = AsteroidField()
    dt = 0
    game = True
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        screen.fill(000)
        for i in drawable:
            i.draw(screen)
        for i in asteroids:
            shot_test = False
            test = i.check_collision(player)
            if test:
                print ("Game over!")
                return
            for s in shots:
                shot_test = s.check_collision(i)
                if shot_test:
                    i.split()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()