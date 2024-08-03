import pygame
import utils.config as config

class GlobalState:
    def __init__(self) -> None:
        self.GAME_DISPLAY = pygame.display.set_mode(config.DISPLAY_SIZE, pygame.SCALED)
        self.DEV_MODE = config.SETTINGS["dev_mode"]
        pygame.display.set_caption("Space Defender")
        self.GAME_CLOCK = pygame.time.Clock()


GLOBAL_STATE = GlobalState()