import pygame

class Player:
    def __init__(self, image: pygame.Surface, coords: tuple) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords    # (x,y)
        self.rect = self.image.get_rect()
        
        
class Monster:
    def __init__(self, image: pygame.Surface, coords: tuple) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.rect = self.image.get_rect()


class PlayerMissile:
    def __init__(self, image: pygame.Surface, coords: tuple) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.rect = self.image.get_rect()


class MonsterMissile:
    def __init__(self, image: pygame.Surface, coords: tuple) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.rect = self.image.get_rect()


class Coin:
    def __init__(self, image: pygame.Surface, coords: tuple) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.rect = self.image.get_rect()