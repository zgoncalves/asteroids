import pygame
from constants import *
from logger import log_state
from cicleshape import *
from player import *

def main():
    pygame.init()

    #FPS
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player(x, y)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
# starting new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: # infit loop
        for event in pygame.event.get():
            log_state()
            screen.fill("black")
            player.draw(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            if event.type == pygame.QUIT:
                return
        pass



if __name__ == "__main__":
    main()
