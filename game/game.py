import pygame

class Game:
    def __init__(self, DISPLAY: pygame.Surface, DISPLAY_SIZE: tuple) -> None:
        self.DISPLAY = DISPLAY
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.load_sprites()

    def draw(self):
        self.DISPLAY.fill((0,0,0))
        

    def load_sprites(self):
        self.PLAYER_IMAGE = pygame.image.load("player_256px.png").convert()
        self.MONSTER_IMAGE = pygame.image.load("monster_256px.png").convert()
        self.PLAYER_MISSILE_IMAGE = pygame.image.load("player_missile_24px.png").convert()
        self.MONSTER_MISSILE_IMAGE = pygame.image.load("monster_missile_64px.png").convert()
        self.COLLECTABLE_ITEM = pygame.image.load("collectable_item_48px.png").convert()
