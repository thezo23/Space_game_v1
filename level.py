import pygame
import random

class Level():

    def __init__(self, game):
        super().__init__()

        self.game = game
        self.obstacle_remaining = 1
        self.asteroid_remaining = 1
        self.current_level = 1
        self.current_score = 0
        self.difficulty = 0



    def next_level(self):

        self.current_level += 1
        self.obstacle_remaining += self.current_level * 3
        self.asteroid_remaining += 1
        self.game.all_obstacles = pygame.sprite.Group()
        for obstacle in range(self.current_level):
            self.game.spawn_obstacle()
        for asteroid in range(int(self.current_level / 2)):
            self.game.spawn_asteroid()

    def special_level(self):
        self.all_asteroids = pygame.sprite.Group()
        self.game.all_obstacles = pygame.sprite.Group()
        self.game.spawn_asteroid()
        self.asteroid_remaining -= 1
