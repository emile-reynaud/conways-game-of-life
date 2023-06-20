import pygame

from Window import *

pygame.init()

DISPLAY = Window(1080, 720, "Conway's Game of Life")
CLOCK = pygame.time.Clock()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DISPLAY.quit()
        
        CLOCK.tick(60)
        DISPLAY.update()