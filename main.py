import time
import pygame
import sys

from screeninfo import get_monitors

from lib.Color import *
from system.Cell import Cell
from ui.Grid import Grid

pygame.init()

for m in get_monitors():
    if m.is_primary:
        monitor = m

w_width = monitor.width
w_height = monitor.height
w_title = "Conway's Game of Life"
w_flags = pygame.FULLSCREEN

DISPLAY = pygame.display.set_mode((w_width, w_height), w_flags)
pygame.display.set_caption(w_title)

grid = Grid(DISPLAY)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        DISPLAY.fill(Color().BLACK)

        grid.update()
        
        pygame.display.update()
        pygame.display.flip()
        time.sleep(1/60)