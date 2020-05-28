import pygame
from player import Player
from obstacle import Obstacle
from asteroid import Asteroid
from satellite import Satellite
from os import path
from level import Level
from ground import Ground
from ufo import Ufo
from health import Health

class Game:

    def __init__(self):
        self.is_playing = False
        self.menu_display = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.ufo = Ufo(self)
        self.health = Health(self)
        self.level = Level(self)
        self.ground = Ground(self)
        self.obstacle = Obstacle(self)
        self.asteroid = Asteroid(self)
        self.satellite = Satellite(self)
        self.all_players.add(self.player)
        self.all_obstacles = pygame.sprite.Group()
        self.all_asteroids = pygame.sprite.Group()
        self.all_satellites = pygame.sprite.Group()
        self.load_data()

        self.pressed = {}

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, 'hightscore.txt'), "r") as f:
            try:
                self.hightscore = int(f.read())

            except:
                self.hightscore = 0

    def start(self):
        self.is_playing = True

        self.all_obstacles = pygame.sprite.Group()
        self.all_asteroids = pygame.sprite.Group()
        self.all_satellites = pygame.sprite.Group()
        self.all_ufos = pygame.sprite.Group()
        self.all_healths = pygame.sprite.Group()

        self.spawn_obstacle()
        self.spawn_asteroid()
        self.spawn_satellite()
        self.spawn_ufo()



    def update(self, screen):

        screen.blit(self.player.image, self.player.rect)

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        textsurface = myfont.render('Score: {}'.format(
            self.level.current_score), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))

        textsurface = myfont.render('Niveau {}'.format(
            self.level.current_level), False, (255, 255, 255))
        screen.blit(textsurface, (450, 100))

        print("================================================================")
        print("NIVEAU == {} ==".format(self.level.current_level))
        print("DIFFICULTEE == {} ==".format(self.level.difficulty))
        print("il reste {} obstacles".format(self.level.obstacle_remaining))
        print("il y'a {} obstacles".format(len(self.all_obstacles)))
        print("il y'a {} asteroid".format(len(self.all_asteroids)))
        print("il reste {} asteroid".format(self.level.asteroid_remaining))
        print("================================================================")

        for player in self.all_players:
            player.update_health_bar(screen)

            if player.rect.x < 0:
                player.damage(0.5)
                player.update_health_bar(screen)

        for obstacle in self.all_obstacles:
            if obstacle.rect.x < 0:
                self.level.obstacle_remaining -= 1
                obstacle.respawn()
                self.level.current_score += self.player.health
            else:
                obstacle.forward()

        for satellite in self.all_satellites:
            if satellite.rect.x < 1:
                satellite.respawn()
            else:
                satellite.forward()
                satellite.rotate()

        for ufo in self.all_ufos:
            if ufo.rect.x < 1:
                ufo.respawn()
            else:
                ufo.forward()
                ufo.drop()

        for health in self.all_healths:
            for player in self.check_collision(health, self.all_players):
                player.heal(50)
                health.remove()
            if health.rect.y < 650:
                health.move()


        for asteroid in self.all_asteroids:
            if asteroid.rect.y > 1000:
                self.level.asteroid_remaining -= 1
                asteroid.respawn()

            else:
                asteroid.forward()

        if self.level.obstacle_remaining == 0:
            self.obstacle.remove()
            self.level.next_level()

        if self.level.asteroid_remaining <= 0:
            self.all_asteroids = pygame.sprite.Group()
            

        self.ground.display(screen)
        self.all_obstacles.draw(screen)
        self.all_asteroids.draw(screen)
        self.all_satellites.draw(screen)
        self.all_ufos.draw(screen)
        self.all_healths.draw(screen)


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_obstacle(self):
        obstacle = Obstacle(self)
        self.all_obstacles.add(obstacle)

    def spawn_asteroid(self):
        asteroid = Asteroid(self)
        self.all_asteroids.add(asteroid)

    def spawn_ufo(self):
        ufo = Ufo(self)
        self.all_ufos.add(ufo)

    def spawn_satellite(self):
        satellite = Satellite(self)
        self.all_satellites.add(satellite)

    def spawn_health(self):
        health = Health(self)
        self.all_healths.add(health)

    def game_over(self):
        self.is_playing = False
        self.all_obstacles = pygame.sprite.Group()
        self.all_asteroids = pygame.sprite.Group()
        self.all_satellites = pygame.sprite.Group()
        self.all_ufos = pygame.sprite.Group()

        self.player.health = 100
        self.player.rect.x = 400
        self.level.current_level = 1
        self.level.current_score = 0
        self.level.obstacle_remaining = 1

