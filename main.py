import pygame
import random
import math

# initialising the pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption(r"Space Invaders")
# game icon
icon = pygame.image.load(r"images\ufo_icon.png")
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load(r"images\rocket_player.png")
player_x = 368
player_y = 480
player_change = 6


def player(x, y):
    # draw player image on screen
    screen.blit(player_img, (x, y))


# enemy
enemy_img = pygame.image.load(r"images\monster_enemy.png")
enemy_x = random.randint(5, 731)
enemy_y = random.randint(10, 200)
# enemy_y = 396
enemy_change = 2.5


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# bullet
bullet_img = pygame.image.load(r"images\stick1_icon.png")
is_bullet_shooting = False
bullet_x = 0
bullet_y = 0
bullet_change = 8


def bullet(x, y):
    screen.blit(bullet_img, (x, y))


# collision
def collision(ene_x, ene_y, bul_x, bul_y):
    temp_x = ene_x - bul_x
    temp_y = ene_y - bul_y
    if math.sqrt(temp_x ** 2 + temp_y ** 2) < 32:
        return True
    return False


# background
background_img = pygame.image.load(r"images\bg.png")

# text on screen
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
font_score = pygame.font.Font('freesansbold.ttf', 20)


def show_score(x, y):
    score = font_score.render("Score : " + str(score_value), True, (128, 128, 128))
    screen.blit(score, (x, y))


# clock
clock = pygame.time.Clock()

# game loop
# pygame.key.set_repeat(1, 25)
running = True
while running:
    clock.tick(30)
    # for background
    screen.fill((0, 128, 0))
    screen.blit(background_img, (0, 0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score(10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x = player_x - player_change
        if player_x < 5:
            player_x = 5
        player(player_x, player_y)
    if keys[pygame.K_RIGHT]:
        player_x = player_x + player_change
        if player_x > 731:
            player_x = 731
        player(player_x, player_y)
    if keys[pygame.K_SPACE]:
        if not is_bullet_shooting:
            is_bullet_shooting = True
            bullet_x = player_x + 16
            bullet_y = player_y - 16

    if is_bullet_shooting:
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change
        if bullet_y < 10:
            is_bullet_shooting = False
        else:
            if collision(enemy_x + 32, enemy_y + 32, bullet_x + 16, bullet_y):
                score_value += 1
                is_bullet_shooting = False

    enemy_x = enemy_x + enemy_change
    if enemy_x >= 731 or enemy_x <= 5:
        enemy_change = -enemy_change
        enemy_y += 20
    if enemy_y >= 416:
        game_over = font.render("Game Over! LOL", True, (255, 0, 0))
        screen.blit(game_over, (300, 300))
    pygame.display.update()
