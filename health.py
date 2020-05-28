import pygame
import random

class Health(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.velocity = 5
        self.image = pygame.image.load("health.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = self.game.ufo.rect.y
        self.origin_image = self.image
        self.angle = 0
        self.droped = False
    def rotate(self):
        self.angle += self.velocity
        self.image = pygame.transform.rotozoom(
        self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.game.all_healths.remove(self)

    def move(self):
        self.rect.y += self.velocity






