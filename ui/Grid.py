import pygame

from system.Cell import *

class Grid:
    def __init__(self, DISPLAY:pygame.Surface):
        self.DISPLAY = DISPLAY
        self.cell_size = 10

        self.width = int(self.DISPLAY.get_width()/self.cell_size + 1*self.cell_size)
        self.height = int(self.DISPLAY.get_height()/self.cell_size + 1*self.cell_size)

        self.create_grid()
        self.create_cell_grid()

    def create_grid(self):
        self.grid = []

        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(0)
            self.grid.append(row)

    def create_cell_grid(self):
        self.cell_grid = []

        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(Cell(self.DISPLAY, (self.cell_size*i + 1*i, self.cell_size*j + 1*j), self.cell_size))
            self.cell_grid.append(row)
    
    def update(self):
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                self.cell_grid[i][j].update()
                
                if self.cell_grid[i][j].dead:
                    self.grid[i][j] = 1
                else:
                    self.grid[i][j] = 0
