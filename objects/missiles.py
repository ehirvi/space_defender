import pygame

class PlayerMissile:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.collision_box = pygame.Rect((self.coords[0], self.coords[1]), (self.size[0], self.size[1]))

    def move(self, speed: int):
        self.coords[1] -= speed
        self.collision_box.update((self.coords[0], self.coords[1]), (self.size[0], self.size[1]))

    def is_out_of_bounds(self):
        if self.coords[1] + self.size[1] < 0:
            return True
        return False


class MonsterMissile:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.collision_box = pygame.Rect((self.coords[0], self.coords[1]), (self.size[0], self.size[1]))

    def move(self, speed: int):
        self.coords[1] += speed
        self.collision_box.update((self.coords[0], self.coords[1]), (self.size[0], self.size[1]))

    def is_out_of_bounds(self, DISPLAY_SIZE: tuple):
        if self.coords[1] > DISPLAY_SIZE[1]:
            return True
        return False