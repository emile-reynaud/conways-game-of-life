import pygame

from system.Cell import *

class Grid:
    def __init__(self, DISPLAY:pygame.Surface):
        self.DISPLAY = DISPLAY
        self.cell_size = 20

        self.width = int(self.DISPLAY.get_width()/self.cell_size)
        self.height = int(self.DISPLAY.get_height()/self.cell_size)