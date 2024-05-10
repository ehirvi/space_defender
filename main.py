import pygame
import utils.config as config
from game.space_defender import SpaceDefender


def main():
    pygame.init()
    DISPLAY_SIZE = config.load_settings()
    GAME_DISPLAY = pygame.display.set_mode((DISPLAY_SIZE))
    pygame.display.set_caption("Space Defender")
    GAME_CLOCK = pygame.time.Clock()

    game = SpaceDefender(GAME_DISPLAY, DISPLAY_SIZE)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        game.update_state()
        game.draw_graphics()
        pygame.display.flip()
        GAME_CLOCK.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()  