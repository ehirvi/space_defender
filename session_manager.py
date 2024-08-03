import pygame
import global_state as gs
from levels.first_level import FirstLevel

class SessionManager:
    def __init__(self) -> None:
       pygame.init()
       self.run()

    def run(self):
        FIRST_LEVEL = FirstLevel()
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            FIRST_LEVEL.update_state()
            pygame.display.flip()
            gs.GLOBAL_STATE.GAME_CLOCK.tick(60)