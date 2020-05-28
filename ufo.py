import pygame
import random
import math
class Ufo(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.velocity = 1
        self.image = pygame.image.load("ufo.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(5000, 10000)
        self.rect.y = 300
        self.origin_image = self.image
        self.angle = 0
        self.y = 0
        self.t = 0

    def remove(self):
        self.game.all_ufos.remove(self)

    def forward(self):
        self.rect.x -= self.velocity
        self.t = pygame.time.get_ticks() / 2 % 20000
        self.y = math.sin(self.t / 200.0) * 100 + 200
        self.rect.y = int(self.y)

    def respawn(self):
        self.rect.x = random.randrange(5000, 10000)
        self.rect.y = 300

    def drop(self):
        if self.rect.x == 500:
            self.game.spawn_health()


