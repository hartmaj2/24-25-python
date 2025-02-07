import pygame

screen = pygame.display.set_mode((800,800))

kitten = pygame.image.load("25_02_07/1ZombieShoter/kitten.png")
kitten_rect = kitten.get_rect()
kitten_rect.center = (400,400)


while True:
    events = pygame.event.get()
    
    for event in events:
        if event.type == 256:
            kitten = pygame.transform.rotate(kitten,45)
            kitten_rect = kitten.get_rect()
            kitten_rect.center = (400,400)
            # quit()

    screen.fill("black")
    pygame.draw.rect(screen,"green",kitten_rect)
    screen.blit(kitten,kitten_rect)
    pygame.display.update()


