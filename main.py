import pygame
import math
from ground import Ground
from game import Game
from obstacle import Obstacle
from level import Level


res = (990, 720)


pygame.init()


screen = pygame.display.set_mode(res)

background = pygame.image.load("background.jpg")

play_button = pygame.image.load('play.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 7)
play_button_rect.y = math.ceil(screen.get_height() / 4)

easy_button = pygame.image.load('easy.png')
easy_button_rect = easy_button.get_rect()
easy_button_rect.x = 400
easy_button_rect.y = 300
easy_button = pygame.transform.scale(easy_button, (200, 40))

normal_button = pygame.image.load('normal.png')
normal_button_rect = normal_button.get_rect()
normal_button_rect.x = 400
normal_button_rect.y = 400
normal_button = pygame.transform.scale(normal_button, (200, 40))


hard_button = pygame.image.load('hard.png')
hard_button_rect = hard_button.get_rect()
hard_button_rect.x = 400
hard_button_rect.y = 500
hard_button = pygame.transform.scale(hard_button, (200, 40))



game = Game()


game.player.isJump = False



launched = True



while launched:



    screen.blit(background,(0, -200))

    if game.is_playing:
        game.update(screen)



    elif game.menu_display == True:
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(easy_button, (easy_button_rect.x, easy_button_rect.y))
        screen.blit(normal_button, (normal_button_rect.x, normal_button_rect.y))
        screen.blit(hard_button, (hard_button_rect.x, hard_button_rect.y))

    else:
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        if game.level.current_score > game.hightscore:
            print("HIGHT SCORE !!")

            game.hightscore = game.level.current_score
            textsurface = myfont.render("NEW HIGHT SCORE", False, (255, 255, 255))
            game.screen.blit(textsurface, (550, 550))

        else:
            textsurface = myfont.render("HIGHT SCORE: {} ".format(game.hightscore), False, (255, 255, 255))
            screen.blit(textsurface, (585, 300))
            print("NO HIGHT SCORE")


    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            pygame.quit()

        keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and game.player.rect.x > 0:
        game.player.move_left()

    if keys[pygame.K_RIGHT] and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    if game.player.isJump == False:

        if keys[pygame.K_SPACE]:
            game.player.isJump = True

    else:

        if game.player.jumpCount >= -10:
            neg = 1

            if game.player.jumpCount < 0:
                neg = -1
            game.player.rect.y -= (game.player.jumpCount ** 2) * 0.2 * neg
            game.player.jumpCount -= 0.3

        else:
            game.player.isJump = False
            game.player.jumpCount = 10
            game.player.rect.y = 606

    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button_rect.collidepoint(event.pos):
            game.menu_display = True

        elif easy_button_rect.collidepoint(event.pos) and game.menu_display == True:
            game.start()
            game.level.difficulty = 0

        elif normal_button_rect.collidepoint(event.pos) and game.menu_display == True:
            game.start()
            game.level.difficulty = 1

        elif hard_button_rect.collidepoint(event.pos) and game.menu_display == True:
            game.start()
            game.level.difficulty = 2
