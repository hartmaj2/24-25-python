# THIS GAME WAS MADE ONLY USING CHATGPT
# (except adding the correct picture path)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (160, 82, 45)
LIGHT_BROWN = (210, 105, 30)
FONT = pygame.font.Font(None, 36)
COOKIE_SIZE = (200, 200)
BUTTON_SIZE = (200, 50)
FPS = 60
AUTO_CLICK_INTERVAL = 1000  # In milliseconds

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Load the cookie image
cookie_img = pygame.image.load("24_12_16/asteroidgraphics/asteroid.png")  # Replace with the path to your cookie image
cookie_img = pygame.transform.scale(cookie_img, COOKIE_SIZE)
cookie_rect = cookie_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game state
clicks = 0
auto_clicks = 0
click_power = 1
upgrade_cost = 50
click_power_upgrade_cost = 100

upgrade_button_rect = pygame.Rect(WIDTH // 2 - BUTTON_SIZE[0] // 2, HEIGHT // 2 + 150, *BUTTON_SIZE)
click_power_button_rect = pygame.Rect(WIDTH // 2 - BUTTON_SIZE[0] // 2, HEIGHT // 2 + 220, *BUTTON_SIZE)

# Event for auto-clicks
auto_click_event = pygame.USEREVENT + 1
pygame.time.set_timer(auto_click_event, AUTO_CLICK_INTERVAL)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos):
                clicks += click_power
            elif upgrade_button_rect.collidepoint(event.pos) and clicks >= upgrade_cost:
                clicks -= upgrade_cost
                auto_clicks += 1
                upgrade_cost = int(upgrade_cost * 1.5)
            elif click_power_button_rect.collidepoint(event.pos) and clicks >= click_power_upgrade_cost:
                clicks -= click_power_upgrade_cost
                click_power += 1
                click_power_upgrade_cost = int(click_power_upgrade_cost * 2)

        elif event.type == auto_click_event:
            clicks += auto_clicks

    # Drawing
    screen.fill(WHITE)
    
    # Draw the cookie
    screen.blit(cookie_img, cookie_rect)

    # Display click count
    click_text = FONT.render(f"Clicks: {clicks}", True, BLACK)
    screen.blit(click_text, (10, 10))

    # Display auto-click count
    auto_click_text = FONT.render(f"Auto Clicks: {auto_clicks}", True, BLACK)
    screen.blit(auto_click_text, (10, 50))

    # Display click power
    click_power_text = FONT.render(f"Click Power: {click_power}", True, BLACK)
    screen.blit(click_power_text, (10, 90))

    # Draw the auto-click upgrade button
    pygame.draw.rect(screen, LIGHT_BROWN, upgrade_button_rect)
    pygame.draw.rect(screen, BROWN, upgrade_button_rect, 3)
    upgrade_text = FONT.render(f"Upgrade Auto ({upgrade_cost} clicks)", True, BLACK)
    upgrade_text_rect = upgrade_text.get_rect(center=upgrade_button_rect.center)
    screen.blit(upgrade_text, upgrade_text_rect)

    # Draw the click power upgrade button
    pygame.draw.rect(screen, LIGHT_BROWN, click_power_button_rect)
    pygame.draw.rect(screen, BROWN, click_power_button_rect, 3)
    click_power_text = FONT.render(f"Upgrade Power ({click_power_upgrade_cost} clicks)", True, BLACK)
    click_power_text_rect = click_power_text.get_rect(center=click_power_button_rect.center)
    screen.blit(click_power_text, click_power_text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
