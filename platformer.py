import pygame, sys

from pygame.locals import *
pygame.init()

# game constants
pygame.display.set_caption("Platformer")
WINDOW_SIZE = (400,400)
FRAMERATE_CAP = 60
BACKGROUND_FILL_COLOR = (0,0,0)

# player constants
PLAYER_MOVE_RIGHT_KEY = pygame.K_RIGHT
PLAYER_MOVE_LEFT_KEY = pygame.K_LEFT

# game variables
clock = pygame.time.Clock()
run = True
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# player variables
player_image = pygame.image.load('./data/sprites/larry_lentil.png')
player_location = [50, 50]
player_y_momentum = 0
player_moving_right = False
player_moving_left = False
player_rect = pygame.Rect(
    player_location[0], 
    player_location[1],
    player_image.get_width(),
    player_image.get_height()
)

test_collisions = pygame.Rect(100,100,100,50)

while run:
    screen.fill(BACKGROUND_FILL_COLOR)

    screen.blit(player_image, player_location)

    if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    if player_moving_right:
        player_location[0] += 4
    if player_moving_left:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_collisions):
        pygame.draw.rect(screen, (255,0,0), test_collisions)
    else:
        pygame.draw.rect(screen, (0,0,0), test_collisions)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == PLAYER_MOVE_RIGHT_KEY:
                player_moving_right = True
            if event.key == PLAYER_MOVE_LEFT_KEY:
                player_moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == PLAYER_MOVE_RIGHT_KEY:
                player_moving_right = False
            if event.key == PLAYER_MOVE_LEFT_KEY:
                player_moving_left = False
            

    
    pygame.display.update()
    clock.tick(FRAMERATE_CAP)