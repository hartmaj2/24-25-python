import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

KITTEN_IMAGE = pygame.image.load("25_02_07/1ZombieShoter/kitten.png")
kitten_image = KITTEN_IMAGE

player_x = 0
player_y = 0

player_speed = 2

player_rotation = 0
player_scale = 0.25

def move():
    global player_y, player_x, keys
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

def limit_movement():
    global player_x, player_y
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT:
        player_y = SCREEN_HEIGHT
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH:
        player_x = SCREEN_WIDTH

def wraparound():
    global player_x, player_y
    if player_y < 0:
        player_y = SCREEN_HEIGHT
    if player_y > SCREEN_HEIGHT:
        player_y = 0
    if player_x < 0:
        player_x = SCREEN_WIDTH
    if player_x > SCREEN_WIDTH:
        player_x = 0

def handle_events():
    ...

while True:
    events = pygame.event.get()
    

    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

 
    
    # limit_movement()
    wraparound()
   
    keys = pygame.key.get_pressed()
    move()
    if keys[pygame.K_r]:
        player_rotation += 1
    
    if keys[pygame.K_s]:
        player_rotation += 1

    screen.fill("black")
    # pygame.draw.rect(screen,"green",kitten_rect)
    screen.blit(kitten_image,(player_x,player_y))
    kitten_image = pygame.transform.rotozoom(KITTEN_IMAGE,player_rotation,player_scale)
    pygame.display.update()


