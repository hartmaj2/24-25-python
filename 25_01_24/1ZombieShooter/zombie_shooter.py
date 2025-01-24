import pygame
import math

pygame.init()

# Screen setup

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game_clock = pygame.time.Clock()

# Map setup

BACKGROUND_COLOR = pygame.color.Color(60, 74, 55)

# Player

PLAYER_IMAGE = pygame.image.load("25_01_24/1ZombieShooter/player.svg")
PLAYER_IMAGE_CENTER_OFFSET = 14
PLAYER_SPEED = 3

class Player:

    def __init__(self, coord : tuple):
        print("player was created")
        self.rotation = 0
        self.x_pos = coord[0]
        self.y_pos = coord[1]
        self.image = PLAYER_IMAGE
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (self.x_pos,self.y_pos)
        self.collider = pygame.rect.Rect(self.image_rect.left,self.image_rect.top,self.image_rect.height, self.image_rect.height)

    def render(self,screen : pygame.surface.Surface):
        screen.blit(self.image,self.image_rect)
        
        # TEST PRINT
        # surf = pygame.surface.Surface((self.collider.height,self.collider.height))
        # surf.fill("green")
        # screen.blit(surf,self.collider)

        # TEST 2
        # surf = pygame.surface.Surface((self.image_rect.width,self.image_rect.height))
        # surf.fill("blue")
        # screen.blit(surf,self.image_rect)

    def update(self, keys_pressed, mouse_pos):
        self.move(keys_pressed)
        self.rotate(mouse_pos)
            
    def move(self,keys_pressed):

        print(f"Player pos: X[{self.x_pos}], Y[{self.y_pos}]")

        dx,dy = 0,0

        if keys_pressed[pygame.K_w]:
            dy -= 1
        if keys_pressed[pygame.K_s]:
            dy += 1
        if keys_pressed[pygame.K_a]:
            dx -= 1
        if keys_pressed[pygame.K_d]:
            dx += 1
        
        length = math.sqrt(dx*dx+dy*dy)

        if length != 0:
            dx /= length
            dy /= length

        self.x_pos += dx * PLAYER_SPEED
        self.y_pos += dy * PLAYER_SPEED   

        self.collider.center = (self.x_pos,self.y_pos)
        self.image_rect.center = self.collider.center

    def rotate(self,mouse_pos):
        x_mouse_dist = mouse_pos[0]-self.collider.centerx
        y_mouse_dist = self.collider.centery-mouse_pos[1]

        # if x_mouse_dist != 0:
        #     self.rotation = math.atan(y_mouse_dist/x_mouse_dist)
        #     if x_mouse_dist < 0:
        #         self.rotation += math.pi

        self.rotation = math.atan2(y_mouse_dist,x_mouse_dist)
        
        self.image = pygame.transform.rotate(PLAYER_IMAGE,360 * self.rotation / (2 * math.pi))

        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = (self.collider.centerx + PLAYER_IMAGE_CENTER_OFFSET * math.cos(self.rotation))
        self.image_rect.centery = (self.collider.centery - PLAYER_IMAGE_CENTER_OFFSET * math.sin(self.rotation))
 

# Zombie

ZOMBIE_IMAGE = pygame.image.load("25_01_24/1ZombieShooter/zombie.svg")
ZOMBIE_SPEED = 1

class Zombie:

    def __init__(self, coord : tuple):
        print("zombie was created")
        self.image = ZOMBIE_IMAGE
        self.image_rect = self.image.get_rect()
        
        self.rotation = 0
        self.x_pos = coord[0]
        self.y_pos = coord[1]
        self.image_rect.center = (self.x_pos,self.y_pos)
        self.collider = pygame.rect.Rect(self.image_rect.left,self.image_rect.top,self.image_rect.height, self.image_rect.height)
    
    def render(self,screen : pygame.surface.Surface):
        screen.blit(self.image,self.image_rect)
        
        # TEST PRINT
        # surf = pygame.surface.Surface((self.collider.height,self.collider.height))
        # surf.fill("green")
        # screen.blit(surf,self.collider)

        # TEST 2
        # surf = pygame.surface.Surface((self.image_rect.width,self.image_rect.height))
        # surf.fill("blue")
        # screen.blit(surf,self.image_rect)

    def update(self,player_pos):

        self.move()
        self.rotate(player_pos)
         
    def move(self):

        self.x_pos += ZOMBIE_SPEED * math.cos(self.rotation)
        self.y_pos -= ZOMBIE_SPEED * math.sin(self.rotation)

        self.collider.center = (self.x_pos,self.y_pos)
        self.image_rect.center = self.collider.center

    def rotate(self,player_pos):
        x_player_dist = player_pos[0]-self.x_pos
        y_player_dist = self.y_pos-player_pos[1]
        self.rotation = math.atan2(y_player_dist,x_player_dist)
        self.image = pygame.transform.rotate(ZOMBIE_IMAGE,360 * self.rotation / (2 * math.pi))

        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.collider.center
 
# Game logic

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("goodbye")
            quit()

def update():
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    player.update(keys,mouse_pos)
    # zombie.update((player.collider.centerx,player.collider.centery))

def render():
    global screen, player
    screen.fill(BACKGROUND_COLOR)
    player.render(screen)
    zombie.render(screen)
    pygame.display.flip()

player = Player((SCREEN_WIDTH//2,SCREEN_HEIGHT/2))
zombie = Zombie((100,100))

while True:

    handle_events()

    update()
    render()
    
    game_clock.tick(60)
