import pygame
import utils.config as config
from game.first_level import FirstLevel

dev_mode = False

def main():
    pygame.init()
    DISPLAY_SIZE = config.load_settings()
    GAME_DISPLAY = pygame.display.set_mode((DISPLAY_SIZE), pygame.SCALED)
    pygame.display.set_caption("Space Defender")

    GAME_FIRST_LEVEL = FirstLevel(GAME_DISPLAY, DISPLAY_SIZE, dev_mode)
    GAME_CLOCK = pygame.time.Clock()
    # game_running = True

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            # game_running = False
            pygame.quit()
            quit()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         game_running = False
        GAME_FIRST_LEVEL.update_state()
        pygame.display.flip()
        GAME_CLOCK.tick(60)


if __name__ == "__main__":
    main()