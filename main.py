import pygame
import sys
from game_objects.ship import Ship
from game_objects.asteroid import Asteroid
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1000
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# Load assets
ship_img = "assets/spaceship.png"
bullet_img = "assets/bullet.png"
asteroid_img_1 = "assets/asteroid_1.png"
asteroid_img_2 = "assets/asteroid_2.png"

background_img = pygame.image.load("assets/background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Create game objects
ship = Ship(WIDTH // 2, HEIGHT // 2, ship_img, bullet_img)
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)

def spawn_asteroid():
    # Randomly choose the spawn location (edge of the screen)
    edge = random.choice(["left", "right", "top", "bottom"])

    if edge == "left":
        x = 0
        y = random.randint(0, HEIGHT)
    elif edge == "right":
        x = WIDTH
        y = random.randint(0, HEIGHT)
    elif edge == "top":
        x = random.randint(0, WIDTH)
        y = 0
    else:  # "bottom"
        x = random.randint(0, WIDTH)
        y = HEIGHT

    # Create an asteroid and add it to the sprite group
    asteroid_img = random.choice([asteroid_img_1, asteroid_img_2])
    asteroid = Asteroid(x, y, asteroid_img, ship.rect.x, ship.rect.y)  # Pass the ship's position as target
    all_sprites.add(asteroid)

# Main game loop
running = True
spawn_counter = 0
spawn_timer = 0
spawn_interval = FPS // 2

while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game objects
    spawn_counter += 1
    if spawn_counter % 120 == 0:  # Spawn an asteroid every 2 seconds (assuming 60 FPS)
        spawn_asteroid()

    # Update game objects
    spawn_timer += 1
    if spawn_timer % spawn_interval == 0:
        spawn_asteroid()
    all_sprites.update()

    # Check for bullet firing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet = ship.shoot()
        all_sprites.add(bullet)

    # Draw the background image
    screen.blit(background_img, (0, 0))

    # Render game objects
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
