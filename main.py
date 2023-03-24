import pygame
import sys
import random

from game_objects.ship import Ship
from game_objects.asteroid import Asteroid
from config import HEIGHT, WIDTH, FPS

class Game:
    def __init__(self):
        pygame.init()

        # Create the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("AIsteroids")
        self.clock = pygame.time.Clock()

        # Load assets
        self.background_img = pygame.image.load("assets/background.jpg")
        self.background_img = pygame.transform.scale(self.background_img, (WIDTH, HEIGHT))
        self.ship_img = "assets/spaceship_2.png"
        self.bullet_img = "assets/bullet.png"
        self.asteroid_img_1 = "assets/asteroid_1.png"
        self.asteroid_img_2 = "assets/asteroid_2.png"

        # Create game objects
        self.ship = Ship(WIDTH // 2, HEIGHT // 2, self.ship_img, self.bullet_img)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def run(self):
        # Main game loop
        self.running = True
        self.spawn_timer = 0
        self.spawn_interval = FPS // 15
        self.score = 0
        self.lives = 5

        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.handle_collisions_bullets()
            self.handle_collisions_ship()
            self.update()
            self.draw()
        print(self.score)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Check for bullet firing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet = self.ship.shoot()
            self.bullets.add(bullet)

    def update(self):
        # Update game objects
        self.spawn_timer += 1
        if self.spawn_timer % self.spawn_interval == 0:
            self.spawn_asteroid()
        self.all_sprites.update()
        self.asteroids.update()
        self.bullets.update()

    def draw(self):
        # Draw the background image
        self.screen.blit(self.background_img, (0, 0))

        # Render game objects
        self.all_sprites.draw(self.screen)
        self.asteroids.draw(self.screen)
        self.bullets.draw(self.screen)
        self.draw_score()
        self.draw_lives()
        pygame.display.flip()

    def spawn_asteroid(self):
        # Randomly choose the spawn location (edge of the screen)
        self.edge = random.choice(["left", "right", "top", "bottom"])

        if self.edge == "left":
            x = 0
            y = random.randint(0, HEIGHT)
        elif self.edge == "right":
            x = WIDTH
            y = random.randint(0, HEIGHT)
        elif self.edge == "top":
            x = random.randint(0, WIDTH)
            y = 0
        else:  # "bottom"
            x = random.randint(0, WIDTH)
            y = HEIGHT

        # Create an asteroid and add it to the sprite group
        self.asteroid_img = random.choice([self.asteroid_img_1, self.asteroid_img_2])
        self.asteroid = Asteroid(x, y, self.asteroid_img, self.ship.rect.x, self.ship.rect.y)
        self.asteroids.add(self.asteroid)

    def handle_collisions_bullets(self):
        self.collisions = pygame.sprite.groupcollide(self.asteroids, self.bullets, True, True)
        for asteroid in self.collisions:
            self.score += 1

    def handle_collisions_ship(self):
        self.collisions = pygame.sprite.groupcollide(self.asteroids, self.all_sprites, True, False)
        for asteroid in self.collisions:
            self.lives -= 1
        
        if self.lives == 0:
            print(self.score)
            #pygame.quit()
            #sys.exit()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = f"Score: {self.score}"
        score_surface = font.render(score_text, True, (255, 255, 255))
        score_rect = score_surface.get_rect(topleft=(10, 10))
        self.screen.blit(score_surface, score_rect)

    def draw_lives(self):
        font = pygame.font.Font(None, 36)
        lives_text = f"Lives: {self.lives}"
        lives_surface = font.render(lives_text, True, (255, 255, 255))
        lives_rect = lives_surface.get_rect(topright=(WIDTH-10, 10))
        self.screen.blit(lives_surface, lives_rect)

if __name__ == '__main__':
    game = Game()
    game.run()
