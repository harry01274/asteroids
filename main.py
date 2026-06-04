import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    # Print starting messages
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialise all imported pygame modules
    pygame.init()

    # Initialise the window/screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock to limit FPS
    clock = pygame.time.Clock()
    dt = 0.0

    # Initiate Player in centre of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Create game loop - Drawing game to screen
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)



if __name__ == "__main__":
    main()
