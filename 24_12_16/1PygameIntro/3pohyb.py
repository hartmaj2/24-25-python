import pygame

pygame.init() 

WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

player = pygame.image.load("24_12_16/graphics/Player/jump.png") 
player_x = 250
player_y = 350

# TODO: rozpohybuj postavicku smerem do prava

# TODO: Pri pohybu se postavicka na obrazovku vykresli na novou pozici ale nezmizi z te stare
# udelej neco s obrazovkou vzdy, nez vykreslis postavu na nove pozici, aby uz nebyla na te stare

# TODO: Pridej druhou postavu, ktera se bude hybat doleva

# TODO: Ovladej pozici prvni postavy ctenim vstupu od uzivatele pomoci input()
# Uzivatel tedy bude moci zadat, na jakou x souradnici bude chtit postavicku teleportovat
  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
     
    screen.blit(player,(player_x,player_y))
    
     
    pygame.display.flip() 


# BONUS TODO: Odeber stupidni ovladani a uprav kod tak, aby kdyz je postava mimo obrazovku se objevila zase na druhe strane

# EXTRA BONUS TODO: Zpusob, aby se postavicky pohybovali jako opila zelva
# (tady se hodi zalozit si promennou pro rotaci a pouzit funkce sinus a cosinus pro spocteni, o kolik se postavicka ma pri dane rotaci posunout po x a po y)
# (!) POZOR: uhel se zadava v radianech, pokud pouzivas math.sin() nebo math.cos()