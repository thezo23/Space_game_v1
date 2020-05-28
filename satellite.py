import pygame
import random

class Satellite(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.velocity = 0.2
        self.satellites_images = ["satellite.png", "satellite2.png"]
        self.image = pygame.image.load(random.choice(self.satellites_images))
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.randrange(0, 400)
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += self.velocity
        self.image = pygame.transform.rotozoom(
        self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.game.all_satellites.remove(self)
        print('removed - satellite')

    def forward(self):
            self.rect.x -= self.velocity

    def respawn(self):
        self.rect.x = 1000
        self.rect.y = random.randrange(0, 400)
        print('respawn - satellite')