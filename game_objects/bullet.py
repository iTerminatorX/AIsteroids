import pygame
import math

WIDTH, HEIGHT = 1920, 1000
FPS = 60

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, image, speed=800):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (8, 8))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.angle = angle
        self.speed = speed

    def update(self):
        # Calculate the new position based on the bullet's angle and speed
        dx = math.sin(math.radians(self.angle)) * self.speed / FPS
        dy = -math.cos(math.radians(self.angle)) * self.speed / FPS  # Note the negative sign, as Pygame's y-axis is inverted

        # Update the bullet's position
        self.rect.x += dx
        self.rect.y += dy

        # Remove the bullet if it goes off-screen
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()
