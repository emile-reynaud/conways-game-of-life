import pygame

from system.Cell import *

class Grid:
    def __init__(self, DISPLAY:pygame.Surface):
        self.DISPLAY = DISPLAY
        self.cell_size = 15

        self.width = int(self.DISPLAY.get_width()/self.cell_size + 1*self.cell_size)
        self.height = int(self.DISPLAY.get_height()/self.cell_size + 1*self.cell_size)

        self.reset_grid()
        self.reset_cell_grid()

    def reset_grid(self):
        self.grid = []

        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(0)
            self.grid.append(row)

    def reset_cell_grid(self):
        self.cell_grid = []

        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(Cell(self.DISPLAY, (self.cell_size*i + 1*i, self.cell_size*j + 1*j), self.cell_size))
            self.cell_grid.append(row)
    
    def update(self):
        self.check_cell_click()
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                if self.grid[i][j] == 0:
                    self.cell_grid[i][j].dead = True
                elif self.grid[i][j] == 1:
                    self.cell_grid[i][j].dead = False
                
                self.cell_grid[i][j].update()                

    def check_cell_click(self):
        for i in range(len(self.cell_grid)):
            for j in range(len(self.cell_grid[i])):
                if self.cell_grid[i][j].is_hovered():
                    if self.cell_grid[i][j].is_clicked():
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = 1
                        elif self.grid[i][j] == 1:
                            self.grid[i][j] = 0
