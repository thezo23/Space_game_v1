import pygame
import random

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        if game.level.difficulty == 0:
            self.velocity = random.randrange(2, 4)
        elif game.level.difficulty == 1:
            self.velocity = random.randrange(4, 5)
        elif game.level.difficulty == 2:
            self.velocity = random.randrange(6, 8)

        self.image = pygame.image.load("stone.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(2000, 3000)
        self.rect.y = random . randrange(580, 630)
        self.attack = 1
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        self.angle += self.velocity
        self.image = pygame.transform.rotozoom(
        self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.game.all_obstacles.remove(self)
        print('removed')

    def forward(self):

        for player in self.game.check_collision(self, self.game.all_players):
            self.game.player.rect.x -= 10
            self.game.player.damage(self.attack)
            self.rotate()

        else:
            self.rect.x -= self.velocity
            self.rotate()

    def respawn(self):
        self.rect.x = random.randrange(2000, 3000)
        self.rect.y = random.randrange(580, 630 )
        print('respawn')



