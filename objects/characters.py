import pygame

class Player:
    def __init__(self, image: pygame.Surface, coords: list, DISPLAY_SIZE: tuple) -> None:
        self.DISPLAY_SIZE = DISPLAY_SIZE
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords    # [x,y]
        self.collision_box = pygame.Rect((self.coords[0], self.coords[1]), (self.size[0] - self.size[0] / 100, self.size[1] - self.size[1] / 100))

    def move(self, direction: str, speed: int):
        if direction == "left":
            self.coords[0] -= speed
            self.collision_box.move_ip(-speed, 0)
        elif direction == "right":
            self.coords[0] += speed
            self.collision_box.move_ip(speed, 0)
        elif direction == "up":
            self.coords[1] -= speed
            self.collision_box.move_ip(0, -speed)
        elif direction == "down":
            self.coords[1] += speed
            self.collision_box.move_ip(0, speed)

    def check_out_of_bounds(self):
        if self.coords[0] < 0:
            self.coords[0] = 0
        elif self.coords[0] + self.size[0] > self.DISPLAY_SIZE[0]:
            self.coords[0] = self.DISPLAY_SIZE[0] - self.size[0]

        if self.coords[1] < 0:
            self.coords[1] = 0
        elif self.coords[1] + self.size[1] > self.DISPLAY_SIZE[1]:
            self.coords[1] = self.DISPLAY_SIZE[1] - self.size[1]
            
        
        
class Monster:
    def __init__(self, image: pygame.Surface, coords: list) -> None:
        self.image = image
        self.size = self.image.get_size()
        self.coords = coords