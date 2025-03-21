import pygame

# SCREEN

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# PLAYER

PLAYER_IMAGE_SCALE = 0.5
# image = pygame.image.load("25_02_07/1ZombieShoter/player.svg")
image = pygame.image.load("25_02_07/1ZombieShoter/kitten.png")
PLAYER_IMAGE_BASE = pygame.transform.rotozoom(image,0,PLAYER_IMAGE_SCALE)

player_image = PLAYER_IMAGE_BASE
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
player_rotation = 0

# GAME LOOP

while True:

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
    

    player_image = pygame.transform.rotozoom(PLAYER_IMAGE_BASE,player_rotation,1)
    player_rect = player_image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
    screen.fill("cyan")
    # pygame.draw.rect(screen,"green",player_rect) # TODO uncomment this line 
    screen.blit(player_image,player_rect)
    pygame.display.update()
