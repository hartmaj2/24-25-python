import pygame
import math

## CLOCK

clock = pygame.time.Clock()

## SCREEN

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

## PLAYER

PLAYER_IMAGE_SCALE = 0.5
image = pygame.image.load("25_02_07/1ZombieShoter/player.svg")
# image = pygame.image.load("25_02_07/1ZombieShoter/kitten.png")
PLAYER_IMAGE_BASE = pygame.transform.rotozoom(image,0,PLAYER_IMAGE_SCALE)
PLAYER_SPEED = 5

player_image = PLAYER_IMAGE_BASE
player_rect = player_image.get_rect()
player_x = SCREEN_WIDTH//2
player_y = SCREEN_HEIGHT//2
player_rect.center = (player_x,player_y)
player_rotation = 0

## GAME LOOP

while True:

    ## event loop

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_rotation += 15
            if keys[pygame.K_RIGHT]:
                player_rotation -= 15
    
    ## movement

    player_image = pygame.transform.rotozoom(PLAYER_IMAGE_BASE,player_rotation,1)
    player_rect = player_image.get_rect(center=(player_x,player_y))

    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_d]:
        dx += 1
    if keys[pygame.K_s]:
        dy += 1
    if keys[pygame.K_w]:
        dy -= 1

    step_length = math.sqrt(dx*dx+dy*dy)
    # print(step_length)
    if step_length != 0:
        dx /= step_length
        dy /= step_length

    player_x += dx * PLAYER_SPEED
    player_y += dy * PLAYER_SPEED

    # collision with walls

    if player_rect.left < 0:
        player_rect.left = 0
        player_x = player_rect.centerx
    if player_rect.right > SCREEN_WIDTH:
        player_rect.right = SCREEN_WIDTH
        player_x = player_rect.centerx
    if player_rect.top < 0:
        player_rect.top = 0
        player_y = player_rect.centery
    if player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT
        player_y = player_rect.centery

    ## rendering

    screen.fill("cyan")
    # pygame.draw.rect(screen,"green",player_rect)
    screen.blit(player_image,player_rect)
    pygame.display.update()
    clock.tick(60)