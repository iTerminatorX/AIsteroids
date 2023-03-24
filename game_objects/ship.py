import pygame
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = pygame.image.load(image)
        #self.original_image = pygame.transform.scale(self.original_image, (64, 64))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rotate(-8)
        if keys[pygame.K_RIGHT]:
            self.rotate(8)
        if keys[pygame.K_UP]:
            self.move_forward()
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, delta_angle):
        self.angle += delta_angle
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def move_forward(self):
        # Calculate the new position based on the ship's angle
        speed = 8
        dx = math.sin(math.radians(self.angle)) * speed
        dy = -math.cos(math.radians(self.angle)) * speed  # Note the negative sign, as Pygame's y-axis is inverted

        # Update the ship's position
        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        # Add logic to create and shoot bullets
        pass
