import pygame

screen = pygame.display.set_mode((800,800))

KITTEN_IMAGE = pygame.image.load("25_02_07/1ZombieShoter/kitten.png")
kitten_image = KITTEN_IMAGE
player_x = 0
player_y = 0


rotation = 0

while True:
    events = pygame.event.get()
    
    for event in events:
        if event.type == 256:
            player_x += 10
            # quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= 10

    screen.fill("black")
    # pygame.draw.rect(screen,"green",kitten_rect)
    screen.blit(kitten_image,(player_x,player_y))
    pygame.display.update()


