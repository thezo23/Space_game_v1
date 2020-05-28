import pygame
import random

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.velocity = random.randrange(6, 10)
        self.image = pygame.image.load("asteroid.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(600, 1500)
        self.rect.y = 0
        self.attack = 1
        self.origin_image = self.image
        self.angle = 0



    def remove(self):
        self.game.all_asteroids.remove(self)
        print('removed - asteroid')

    def forward(self):
        for player in self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)

        else:
            self.rect.x -= self.velocity
            self.rect.y += self.velocity

    def respawn(self):
        self.rect.x = random.randrange(600, 1500)
        self.rect.y = 0
        print('respawn - asteroid')



