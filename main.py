import pygame

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
player_x = 370
player_y = 480
player_change = 5


def player(x, y):
    # draw player image on screen
    screen.blit(player_img, (x, y))


# game loop
pygame.key.set_repeat(1, 25)
running = True
while running:
    # for background
    screen.fill((0, 128, 0))
    player(player_x, player_y)

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

    pygame.display.update()
