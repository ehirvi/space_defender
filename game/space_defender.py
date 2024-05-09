import pygame
from objects import characters, missiles, misc

class SpaceDefender:
    def __init__(self, DISPLAY: pygame.Surface, DISPLAY_SIZE: tuple) -> None:
        self.DISPLAY = DISPLAY
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.load_images()
        # self.MONSTER = objects.characters.Monster(self.MONSTER_IMAGE_SCALED, (0,0))
        # self.PLAYER_MISSILE = objects.missiles.PlayerMissile(self.PLAYER_MISSILE_IMAGE_SCALED, (0,0))
        # self.MONSTER_MISSILE = objects.missiles.MonsterMissile(self.MONSTER_MISSILE_IMAGE_SCALED, (0,0))
        # self.COIN = objects.misc.Coin(self.COIN_IMAGE_SCALED, (0,0))
        self.start_level()


    def draw_graphics(self):
        self.DISPLAY.fill((0,0,0))
        self.DISPLAY.blit(self.player.image, self.player.coords)
        for missile in self.PLAYER_MISSILES:
            self.DISPLAY.blit(missile.image, missile.coords)
        # self.DISPLAY.blit(self.PLAYER_MISSILE.image, self.PLAYER_MISSILE.coords)
        # self.DISPLAY.blit(self.MONSTER.image, self.MONSTER.coords)
        # self.DISPLAY.blit(self.MONSTER_MISSILE.image, self.MONSTER_MISSILE.coords)
        # self.DISPLAY.blit(self.COIN.image, self.COIN.coords)


    def load_images(self):
        PLAYER_IMAGE_ORIG = pygame.image.load("assets/images/player_512px.png").convert()
        self.PLAYER_IMAGE_SCALED = pygame.transform.scale(PLAYER_IMAGE_ORIG, (PLAYER_IMAGE_ORIG.get_width() / 8, PLAYER_IMAGE_ORIG.get_height() / 8))

        MONSTER_IMAGE_ORIG = pygame.image.load("assets/images/monster_512px.png").convert()
        self.MONSTER_IMAGE_SCALED = pygame.transform.scale(MONSTER_IMAGE_ORIG, (MONSTER_IMAGE_ORIG.get_width() / 8, MONSTER_IMAGE_ORIG.get_height() / 8))

        PLAYER_MISSILE_IMAGE_ORIG = pygame.image.load("assets/images/player_missile_512px.png").convert()
        self.PLAYER_MISSILE_IMAGE_SCALED = pygame.transform.scale(PLAYER_MISSILE_IMAGE_ORIG, (PLAYER_MISSILE_IMAGE_ORIG.get_width() / 16, PLAYER_MISSILE_IMAGE_ORIG.get_height() / 16))

        MONSTER_MISSILE_IMAGE_ORIG = pygame.image.load("assets/images/monster_missile_512px.png").convert()
        self.MONSTER_MISSILE_IMAGE_SCALED = pygame.transform.scale(MONSTER_MISSILE_IMAGE_ORIG, (MONSTER_MISSILE_IMAGE_ORIG.get_width() / 16, MONSTER_MISSILE_IMAGE_ORIG.get_height() / 16))

        COIN_IMAGE_ORIG = pygame.image.load("assets/images/coin_512px.png").convert()
        self.COIN_IMAGE_SCALED = pygame.transform.scale(COIN_IMAGE_ORIG, (COIN_IMAGE_ORIG.get_width() / 24, COIN_IMAGE_ORIG.get_height() / 24))

    
    def start_level(self):
        self.player = characters.Player(self.PLAYER_IMAGE_SCALED,
                                        [self.DISPLAY_SIZE[0] / 2 - self.PLAYER_IMAGE_SCALED.get_width() / 2, 
                                         self.DISPLAY_SIZE[1] - self.PLAYER_IMAGE_SCALED.get_height() - self.DISPLAY_SIZE[1] /  10],
                                         self.DISPLAY_SIZE)
        self.player_has_shot_missile = False
        self.PLAYER_MISSILES = []
        self.MONSTERS = []
        self.MONSTER_MISSILES = []


    def check_user_inputs(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.move("left", 5)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.move("right", 5)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.player.move("up", 5)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.player.move("down", 5)

        self.player.check_out_of_bounds()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if not self.player_has_shot_missile:
                self.player_shoot_missile()
                self.player_has_shot_missile = True
        else:
            self.player_has_shot_missile = False


    def player_shoot_missile(self):
        self.PLAYER_MISSILES.append(missiles.PlayerMissile(self.PLAYER_MISSILE_IMAGE_SCALED,
                                                           [self.player.coords[0] + self.player.size[0] / 2 - self.PLAYER_MISSILE_IMAGE_SCALED.get_width() / 2,
                                                            self.player.coords[1] - self.PLAYER_MISSILE_IMAGE_SCALED.get_height()]))


    def move_npc(self):
        for missile in self.PLAYER_MISSILES:
            missile.move(10)


    def detect_collisions(self):
        None


    def update_state(self):
        self.check_user_inputs()
        self.move_npc()
        self.detect_collisions()
