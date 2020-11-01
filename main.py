import pygame
import random

# initialising the pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption("Space Invaders")
# game icon
icon = pygame.image.load("ufo_icon.png")
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load("rocket_player.png")
player_x = 736
player_y = 480
player_change = 5


def player(x, y):
    # draw player image on screen
    screen.blit(player_img, (x, y))


# enemy
enemy_img = pygame.image.load("monster_enemy.png")
enemy_x = random.randint(5, 731)
enemy_y = random.randint(10, 200)
# enemy_y = 396
enemy_change = .15


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# text on screen
font = pygame.font.Font('freesansbold.ttf', 32)
font_score = pygame.font.Font('freesansbold.ttf', 20)


def show_score(x, y):
    score = font_score.render("Score : ", True, (128, 0, 0))
    screen.blit(score, (x, y))


# game loop
pygame.key.set_repeat(1, 25)
running = True
while running:
    # for background
    screen.fill((0, 128, 0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score(10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x = player_x - player_change
                if player_x < 5:
                    player_x = 5
                player(player_x, player_y)
            if event.key == pygame.K_RIGHT:
                player_x = player_x + player_change
                if player_x > 731:
                    player_x = 731
                player(player_x, player_y)
    enemy_x = enemy_x + enemy_change
    if enemy_x >= 731 or enemy_x <= 5:
        enemy_change = -enemy_change
        enemy_y += 20
    if enemy_y >= 416:
        game_over = font.render("Game Over! LOL", True, (255, 0, 0))
        screen.blit(game_over, (300, 300))
    pygame.display.update()
