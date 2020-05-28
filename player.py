import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 606
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.jumpCount = 10

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def heal(self, amount):
        if self.health + amount > self.max_health:
            self.health = self.max_health
        else:
            self.health += amount


    def move_right(self):
        if self.game.check_collision(self, self.game.all_obstacles):

            self.rect.x -= 10
        else:
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):

        bar_color = (27, 158, 55)
        back_bar_color = (84, 84, 84)

        bar_position = [self.rect.x , self.rect.y - 10 , self.health, 5]
        back_bar_position = [self.rect.x ,self.rect.y -10, self.max_health, 5]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

