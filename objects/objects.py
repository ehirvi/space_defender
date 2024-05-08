import pygame

class Player:
    def __init__(self, image: pygame.Surface, coords: tuple) -> None:
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.coords = coords    # (x,y)
        
        
