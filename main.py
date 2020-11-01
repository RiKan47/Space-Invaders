import pygame

# initialising the pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption("Space Invaders")
# game icon
icon = pygame.image.load("ufo_icon.png")
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # for background
    screen.fill((0,0,255))