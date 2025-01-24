import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player_image = pygame.image.load("25_01_24/1ZombieShooter/player.svg")
player_rect = player_image.get_rect()
player_rect.midbottom = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2)

while True:


    keys_pressed = pygame.key.get_pressed()


    dx,dy = 0,0

    if keys_pressed[pygame.K_w]:
        dy -= 1
    if keys_pressed[pygame.K_s]:
        dy += 1
    if keys_pressed[pygame.K_a]:
        dx -= 1
    if keys_pressed[pygame.K_d]:
        dx += 1

    player_rect.x += dx
    player_rect.y += dy

    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse clicked")

        

        if event.type == pygame.QUIT:
            
            # print(event.type)
            # print("quitting the game")
            quit()

    screen.fill("black")
    screen.blit(player_image,player_rect)
    pygame.display.flip()
    clock.tick(60)