import pygame

class Player:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords    # [x,y]
        self.rect = self.image.get_rect()
        
        
class Monster:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.rect = self.image.get_rect()