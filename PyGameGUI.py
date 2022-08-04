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
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
king_img = pygame.image.load('images/King.png')
print(king_img)
#king_img.set_colorkey((250, 250, 250))
images_2d = [[], [], [], [], [], [], [], []]  # surfaces on that are squares in the game
SQUARE_LENGTH = 85

for row in range(8):
    for col in range(8):
        images_2d[row].append(pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH)))
        if (row + col) % 2 == 0:
            images_2d[row][col].fill((250, 250, 250))
        else:
            images_2d[row][col].fill((128, 128, 128))

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
        images_2d[4][3].blit(king_img, (SQUARE_LENGTH/2 - 15,SQUARE_LENGTH/2 - 15))
        for row in range(8):
            for col in range(8):
                screen.blit(images_2d[row][col], (row*SQUARE_LENGTH, col*SQUARE_LENGTH))
        # blit (block transfer) of the surface onto the screen. Tuple is draw location
        #screen.blit(King_img, (0, 0))

        # Flip display
        pygame.display.flip()

pygame.quit()


