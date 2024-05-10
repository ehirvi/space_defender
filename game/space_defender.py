import pygame
from random import randint
from objects import characters, missiles, misc

class SpaceDefender:
    def __init__(self, DISPLAY: pygame.Surface, DISPLAY_SIZE: tuple) -> None:
        self.DISPLAY = DISPLAY
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.load_images()
        self.start_level()


    def draw_graphics(self):
        self.DISPLAY.fill((0,0,0))
        # pygame.draw.rect(self.DISPLAY, (0, 255, 0), self.player.collision_box)
        self.DISPLAY.blit(self.player.image, self.player.coords)

        for monster in self.MONSTERS:
            # pygame.draw.rect(self.DISPLAY, (255, 0, 0), monster.collision_box)
            # pygame.draw.rect(self.DISPLAY, (100, 100, 100), monster.detection_zone)
            self.DISPLAY.blit(monster.image, monster.coords)

        for missile in self.PLAYER_MISSILES:
            # pygame.draw.rect(self.DISPLAY, (255, 0, 0), missile.collision_box)
            self.DISPLAY.blit(missile.image, missile.coords)

        for missile in self.MONSTER_MISSILES:
            self.DISPLAY.blit(missile.image, missile.coords)


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
                                         self.DISPLAY_SIZE[1] - self.PLAYER_IMAGE_SCALED.get_height() - self.DISPLAY_SIZE[1] /  10])
        self.PLAYER_MISSILES = []
        self.MONSTERS = []
        self.MONSTER_MISSILES = []
        self.COINS = []


    def check_user_inputs(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.move("left", 5)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.move("right", 5)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.player.move("up", 5)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.player.move("down", 5)

        self.player.check_out_of_bounds(self.DISPLAY_SIZE)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if not self.player.has_shot_missile:
                self.player_shoot_missile()
                self.player.has_shot_missile = True
        else:
            self.player.has_shot_missile = False


    def player_shoot_missile(self):
        self.PLAYER_MISSILES.append(missiles.PlayerMissile(self.PLAYER_MISSILE_IMAGE_SCALED,
                                                           [self.player.coords[0] + self.player.size[0] / 2 - self.PLAYER_MISSILE_IMAGE_SCALED.get_width() / 2,
                                                            self.player.coords[1] - self.PLAYER_MISSILE_IMAGE_SCALED.get_height()]))
        
    
    def monster_shoot_missile(self, monster: characters.Monster):
        if monster.detection_zone.colliderect(self.player.collision_box):
            time_now = pygame.time.get_ticks()
            if (time_now - monster.time_last_shot_missile >= 500):
                self.MONSTER_MISSILES.append(missiles.MonsterMissile(self.MONSTER_MISSILE_IMAGE_SCALED,
                                                                     [monster.coords[0] + monster.size[0] / 2 - self.MONSTER_MISSILE_IMAGE_SCALED.get_width() / 2,
                                                                     monster.coords[1] + monster.size[1]]))
                monster.time_last_shot_missile = time_now


    def spawn_monsters(self):
        if randint(1, 70) == 1:
            self.MONSTERS.append(characters.Monster(self.MONSTER_IMAGE_SCALED,
                                                    [randint(0, self.DISPLAY_SIZE[0] - self.MONSTER_IMAGE_SCALED.get_width()),
                                                     0 - self.MONSTER_IMAGE_SCALED.get_height()],
                                                     self.DISPLAY_SIZE))


    def move_npc(self):
        for monster in self.MONSTERS:
            monster.move(2)
            self.monster_shoot_missile(monster)
            if monster.is_out_of_bounds(self.DISPLAY_SIZE):
                self.MONSTERS.remove(monster)

        for missile in self.PLAYER_MISSILES:
            missile.move(10)
            if missile.is_out_of_bounds():
                self.PLAYER_MISSILES.remove(missile)

        for missile in self.MONSTER_MISSILES:
            missile.move(4)
            if missile.is_out_of_bounds(self.DISPLAY_SIZE):
                self.MONSTER_MISSILES.remove(missile)


    def detect_collisions(self):
        monster_collision_boxes = [monster.collision_box for monster in self.MONSTERS]
        monster_missile_collision_boxes = [monster_missile.collision_box for monster_missile in self.MONSTER_MISSILES]

        for missile in self.PLAYER_MISSILES:
            collisions = missile.collision_box.collidelistall(monster_collision_boxes)
            if len(collisions) != 0:
                pygame.quit()
                # remove the monster from monsters list

        if self.player.collision_box.collidelist(monster_missile_collision_boxes) != -1:
            pygame.quit()

        if self.player.collision_box.collidelist(monster_collision_boxes) != -1:
            pygame.quit()   # think of something better than crashing the game


    def update_state(self):
        self.check_user_inputs()
        self.spawn_monsters()
        self.move_npc()
        self.detect_collisions()
