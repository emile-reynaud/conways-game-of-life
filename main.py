import pygame
import sys

from lib.Color import *
from system.Cell import Cell

pygame.init()

w_width, w_height = 1080, 720
w_title = "Conway's Game of Life"
w_flags = pygame.RESIZABLE

DISPLAY = pygame.display.set_mode((w_width, w_height), w_flags)
pygame.display.set_caption(w_title)
CLOCK = pygame.time.Clock()
cell = Cell(DISPLAY, 20)
cell.add((w_width/2, w_height/2))

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(Color().BLACK)

        cell.draw()
        
        pygame.display.update()
        pygame.display.flip()
        CLOCK.tick(30)