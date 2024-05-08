import pygame
import objects.objects

class Game:
    def __init__(self, DISPLAY: pygame.Surface, DISPLAY_SIZE: tuple) -> None:
        self.DISPLAY = DISPLAY
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.load_sprites()
        # self.PLAYER = objects.objects.Player(self.PLAYER_IMAGE, (0,0))
        self.MONSTER = objects.objects.Monster(self.MONSTER_IMAGE, (0,0))

    def draw(self):
        self.DISPLAY.fill((0,0,0))
        # self.DISPLAY.blit(self.PLAYER.image, self.PLAYER.coords)
        self.DISPLAY.blit(self.MONSTER.image, self.MONSTER.coords)

    def load_sprites(self):
        PLAYER_IMAGE_FULL = pygame.image.load("assets/images/player_512px.png").convert()
        self.PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE_FULL, (PLAYER_IMAGE_FULL.get_width() / 8, PLAYER_IMAGE_FULL.get_height() / 8))

        MONSTER_IMAGE_FULL = pygame.image.load("assets/images/monster_512px.png").convert()
        self.MONSTER_IMAGE = pygame.transform.scale(MONSTER_IMAGE_FULL, (MONSTER_IMAGE_FULL.get_width() / 8, MONSTER_IMAGE_FULL.get_height() / 8))

        PLAYER_MISSILE_IMAGE = pygame.image.load("assets/images/player_missile_512px.png").convert()
        MONSTER_MISSILE_IMAGE = pygame.image.load("assets/images/monster_missile_512px.png").convert()
        COLLECTABLE_ITEM = pygame.image.load("assets/images/coin_512px.png").convert()
