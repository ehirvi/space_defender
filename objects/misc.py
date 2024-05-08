import pygame

class Coin:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.rect = self.image.get_rect()