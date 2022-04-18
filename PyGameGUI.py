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

# Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))  # This is supposed to be the image
        self.rect = self.surf.get_rect()

# settings, constants
pygame.display.set_caption("Chess")
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

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
        screen.fill((0, 0, 0))

        # create a surface. Inputs are its length and width
        # surf = pygame.Surface((50, 50))
        # surf.fill((50, 25, 0))
        # rect = surf.get_rect()  # access the surface's underlying rectangle

        # blit (block transfer) of the surface onto the screen. Tuple is draw location
        screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        # Flip display
        pygame.display.flip()

pygame.quit()


