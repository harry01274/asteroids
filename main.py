import pygame
from constants import *
from logger import log_state

def main():
    # 1. Print starting messages
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # 2. Initialise all imported pygame modules
    pygame.init()

    # 3. Initialise the window/screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 5. Create clock to limit FPS
    clock = pygame.time.Clock()
    dt = 0.0


    # 4. Create game loop - Drawing game to screen
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
