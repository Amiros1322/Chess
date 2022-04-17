import pygame

# init pygame
pygame.init()

# start window
screen = pygame.display.set_mode((500, 500))

# settings
pygame.display.set_caption("Chess")

# run loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fill background with white
        screen.fill((255, 255, 255))

        # Draw a blue circle in the center
        pygame.draw.circle(screen, (0,0,255), (250, 250), 75)

        # Flip display
        pygame.display.flip()

pygame.quit()


