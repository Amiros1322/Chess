import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,

)

# init pygame
pygame.init()

# settings, constants
pygame.display.set_caption("Chess")
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# run loop
running = True
while running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        # Fill background with white
        screen.fill((255, 255, 255))

        # create a surface. Inputs are its length and width
        surf = pygame.Surface((50, 50))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()  # access the surface's underlying rectangle

        # blit (block transfer) of the surface onto the screen. Tuple is draw location
        screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        # Flip display
        pygame.display.flip()

pygame.quit()


