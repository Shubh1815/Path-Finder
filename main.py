import pygame
from grid import Grid

pygame.init()
win = pygame.display.set_mode((800, 501))
pygame.display.set_caption("PATH FINDER")

RUNNING = True

win.fill((20, 39, 78))

grid = Grid(win, 50, 50)
grid.initialize()
grid.generate_maze()

while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    pygame.display.update()

pygame.quit()
