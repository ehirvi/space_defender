import pygame

class PlayerMissile:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.update_collision_box()

    def update_collision_box(self):
        self.collision_box = pygame.Rect(
            self.coords[0],
            self.coords[1],
            self.size[0],
            self.size[1]
        )
        self.collision_box.inflate_ip((-self.size[0] * 0.4,-self.size[1] * 0.4))

    def move(self, speed: int):
        self.coords[1] -= speed
        self.update_collision_box()

    def is_out_of_bounds(self):
        if self.coords[1] + self.size[1] < 0:
            return True
        return False


class MonsterMissile:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.update_collision_box()

    def update_collision_box(self):
        self.collision_box = pygame.Rect(
            self.coords[0],
            self.coords[1],
            self.size[0],
            self.size[1]
        )
        self.collision_box.inflate_ip((-self.size[0] * 0.4,-self.size[1] * 0.4))

    def move(self, speed: int):
        self.coords[1] += speed
        self.update_collision_box()

    def is_out_of_bounds(self, DISPLAY_SIZE: tuple):
        if self.coords[1] > DISPLAY_SIZE[1]:
            return True
        return False