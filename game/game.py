import pygame

class Game:
    def __init__(self, DISPLAY: pygame.surface) -> None:
        self.DISPLAY = DISPLAY

    def draw(self):
        self.DISPLAY.fill((0,0,0))