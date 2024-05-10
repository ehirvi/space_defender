import pygame

class PlayerMissile:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.collision_box = pygame.Rect((self.coords[0], self.coords[1]), (self.size[0] - self.size[0] / 100, self.size[1] - self.size[1] / 100))

    def move(self, speed: int):
        self.coords[1] -= speed
        self.collision_box.move_ip(0, -speed)

    def is_out_of_bounds(self):
        if self.coords[1] + self.size[1] < 0:
            return True
        return False


class MonsterMissile:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords