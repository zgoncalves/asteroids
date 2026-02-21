import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
# starting new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: # infit loop
        for event in pygame.event.get():
            log_state()
            screen.fill("black")
            pygame.display.flip()
            if event.type == pygame.QUIT:
                return
        pass



if __name__ == "__main__":
    main()
