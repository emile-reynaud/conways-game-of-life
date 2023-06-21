import pygame

from ui.Grid import Grid

class SimulationEngine:
    def __init__(self, DISPLAY:pygame.Surface):
        self.DISPLAY = DISPLAY

        self.grid = Grid(self.DISPLAY)

        self.running = False

        self.gen = 0

        self.alive_cells = 0

    def reset(self):
        self.gen = 0
        self.grid.reset_grid()
        self.grid.reset_cell_grid()

    def find_neighbors(self, i:int, j:int):
        if i != 0:
            if j != 0:
                if i != len(self.grid.grid)-1:
                    if j != len(self.grid.grid[i])-1:
                        neighbors = [self.grid.grid[i-1][j-1], self.grid.grid[i-1][j], self.grid.grid[i-1][j+1],
                                     self.grid.grid[i][j-1],                             self.grid.grid[i][j+1], 
                                     self.grid.grid[i+1][j-1], self.grid.grid[i+1][j], self.grid.grid[i+1][j+1]]
                    else:
                        neighbors = [self.grid.grid[i-1][j-1], self.grid.grid[i-1][j],
                                     self.grid.grid[i][j-1], 
                                     self.grid.grid[i+1][j-1], self.grid.grid[i+1][j]]
                else:
                    if j != len(self.grid.grid[i])-1:
                        neighbors = [self.grid.grid[i-1][j-1], self.grid.grid[i-1][j], self.grid.grid[i-1][j+1],
                                     self.grid.grid[i][j-1],                             self.grid.grid[i][j+1]]
                    else:
                        neighbors = [self.grid.grid[i-1][j-1], self.grid.grid[i-1][j],
                                     self.grid.grid[i][j-1]]
            else:
                if i != len(self.grid.grid)-1:
                    neighbors = [self.grid.grid[i-1][j], self.grid.grid[i-1][j+1],
                                                           self.grid.grid[i][j+1], 
                                 self.grid.grid[i+1][j], self.grid.grid[i+1][j+1]]
                else:
                    neighbors = [self.grid.grid[i-1][j], self.grid.grid[i-1][j+1],
                                                           self.grid.grid[i][j+1]]
        else:
            if j != 0:
                if j != len(self.grid.grid[i])-1:
                    neighbors = [self.grid.grid[i][j-1],                             self.grid.grid[i][j+1], 
                                 self.grid.grid[i+1][j-1], self.grid.grid[i+1][j], self.grid.grid[i+1][j+1]]
                else:
                    neighbors = [self.grid.grid[i][j-1], 
                                 self.grid.grid[i+1][j-1], self.grid.grid[i+1][j]]
            else:
                neighbors = [                          self.grid.grid[i][j+1], 
                             self.grid.grid[i+1][j], self.grid.grid[i+1][j+1]]
        
        return neighbors
    
    # def previous_gen(self):
    #     self.gen -= 1
    #     self.alive_cells = 0
    #     self.grid.grid = self.saved_grid
        
    #     for i in range(len(self.grid.grid)):
    #         for j in range(len(self.grid.grid[i])):
    #             if self.grid.grid[i][j] == 1:
    #                 self.alive_cells += 1

    #     self.grid.update()

    def next_gen(self):
        self.gen += 1
        self.alive_cells = 0
        self.saved_grid = self.grid.grid
        for i in range(len(self.saved_grid)):
            for j in range(len(self.saved_grid[i])):
                neighbors = self.find_neighbors(i, j)
                alive_neighbors = 0
                dead_neighbors = 0

                for cell in neighbors:
                    if cell == 1:
                        alive_neighbors += 1
                    elif cell == 0:
                        dead_neighbors += 1
                
                if self.saved_grid[i][j] == 0:
                    if alive_neighbors == 3:
                        self.grid.grid[i][j] = 1
                elif self.saved_grid[i][j] == 1:
                    if alive_neighbors != 2:
                        if alive_neighbors != 3:
                            self.grid.grid[i][j] = 0
        
        for i in range(len(self.grid.grid)):
            for j in range(len(self.grid.grid[i])):
                if self.grid.grid[i][j] == 1:
                    self.alive_cells += 1

        self.grid.update()