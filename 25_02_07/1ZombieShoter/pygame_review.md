# What should be revised

- set_mode() function returns reference to the screen object (of type Surface)

- pygame.display.update() is better than flip (the name makes more sense)

- rect is just a 4-tuple describing a rectangular area (location_left, location_right , width, height) + its location + nice functions to work with it

- image is converted to some other format than svg internally -> when rotating, pygame tries to also preserve the corners and everything -> the picture size grows

- use clock to make the speed of the game same for all computers

## Useful keywords

functions:
- user interaction:
  - `pygame.event.get()`
  - `pygame.key.get_pressed()`
- display:
  - `pygame.display.set_mode()`
  - `screen.fill()`
  - `screen.blit()`
  - `pygame.display.update()`
- images:
  - `pygame.image.load()`
  - `player_image.get_rect()`
  - `pygame.transform.rotozoom()`
  
constants:
- `pygame.QUIT`, `pygame.KEYDOWN` etc.
- `pygame.K_LEFT`, `pygame.K_RIGHT` etc.

## Interesting

- `from pygame.locals import *` imports constants directly into the program namespace so we can write `K_LEFT` instead of `pygame.K_LEFT`