import pygame

class Player:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.update_collision_box()
        self.has_shot_missile = False


    def update_collision_box(self):
        self.collision_box = pygame.Rect(
            self.coords[0],
            self.coords[1],
            self.size[0],
            self.size[1]
        )
        self.collision_box.inflate_ip((-self.size[0] * 0.2,-self.size[1] * 0.4))

    def move(self, direction: str, speed: int):
        if direction == "left":
            self.coords[0] -= speed
        elif direction == "right":
            self.coords[0] += speed
        elif direction == "up":
            self.coords[1] -= speed
        elif direction == "down":
            self.coords[1] += speed

        self.update_collision_box()

    def check_out_of_bounds(self, DISPLAY_SIZE):
        if self.coords[0] < 0:
            self.coords[0] = 0
        elif self.coords[0] + self.size[0] > DISPLAY_SIZE[0]:
            self.coords[0] = DISPLAY_SIZE[0] - self.size[0]

        if self.coords[1] < 0:
            self.coords[1] = 0
        elif self.coords[1] + self.size[1] > DISPLAY_SIZE[1]:
            self.coords[1] = DISPLAY_SIZE[1] - self.size[1]
        
        self.update_collision_box()
            
        
        
class Monster:
    def __init__(self, image: pygame.Surface, coords: list, DISPLAY_SIZE: tuple) -> None:
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords
        self.update_collision_box()
        self.detection_zone = pygame.Rect(self.coords[0],
                                          self.coords[1] + self.size[1],
                                          self.size[0],
                                          self.DISPLAY_SIZE[1] - self.coords[1] + self.size[1])
        self.time_last_shot_missile = 0

    def update_collision_box(self):
        self.collision_box = pygame.Rect(
            self.coords[0],
            self.coords[1],
            self.size[0],
            self.size[1]
        )
        self.collision_box.inflate_ip((-self.size[0] * 0.2,-self.size[1] * 0.2))

    def move(self, speed: int):
        self.coords[1] += speed
        self.update_collision_box()
        self.detection_zone.update(self.coords[0],
                                   self.coords[1] + self.size[1],
                                   self.size[0],
                                   self.DISPLAY_SIZE[1] - self.coords[1] + self.size[1])

    def is_out_of_bounds(self, DISPLAY_SIZE: tuple):
        if self.coords[1] > DISPLAY_SIZE[1]:
            return True
        return False