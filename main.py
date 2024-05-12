import pygame
import utils.config as config
from game.space_defender import SpaceDefender

dev_mode = False

def main():
    pygame.init()
    DISPLAY_SIZE = config.load_settings()
    GAME_DISPLAY = pygame.display.set_mode((DISPLAY_SIZE))
    pygame.display.set_caption("Space Defender")

    game = SpaceDefender(GAME_DISPLAY, DISPLAY_SIZE, dev_mode)
    game_running = True
    game_clock = pygame.time.Clock()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        game.update_state()
        pygame.display.flip()
        game_clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()