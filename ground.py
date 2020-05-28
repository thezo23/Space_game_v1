import pygame

class Ground(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.rect = pygame.Rect(0, 700, 1100, 170)

    def display(self, surface):
        pygame.draw.rect(surface, (110, 107, 98), self.rect)
