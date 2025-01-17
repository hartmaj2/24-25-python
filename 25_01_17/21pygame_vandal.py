import pygame

pygame.init() 

screen = pygame.display.set_mode((1000,700))
i = 0

while True:
    for event in pygame.event.get(): 
        if event.type == 256:
            file = open(f"/Users/janhartman/Desktop/vandal{i}.txt","w")
            file.write("You have been trolled!")
            i += 1
        
