import pygame
import math
import random

from config import HEIGHT, WIDTH, FPS

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, image, target_x, target_y):
        super().__init__()
        self.original_image = pygame.image.load(image)
        #self.original_image = pygame.transform.scale(self.original_image, (64, 64))
        self.size = random.randint(32, 80)
        self.original_image = pygame.transform.scale(self.original_image, (self.size, self.size))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Calculate the direction vector towards the target
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx**2 + dy**2)
        self.direction = (dx / distance, dy / distance)

        self.speed = random.randint(100, 500)  # Pixels per second
        self.rotation_speed = random.randint(-10, 10)  # Rotation speed in degrees per frame

    def update(self):
        self.rotate()
        self.move()

        # Remove the asteroid if it goes off-screen
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()

    def move(self):
        # Move the asteroid towards the target
        self.rect.x += self.direction[0] * self.speed / FPS
        self.rect.y += self.direction[1] * self.speed / FPS

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, -self.rotation_speed)
        self.rotation_speed = (self.rotation_speed + 2) % 360
        self.rect = self.image.get_rect(center=self.rect.center)
